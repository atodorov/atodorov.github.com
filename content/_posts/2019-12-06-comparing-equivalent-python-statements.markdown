Title: Comparing equivalent Python statements
Headline: and learning how various operators work
date: 2019-12-06 22:19
comments: true
Tags: fedora.planet, QA, Python
og_image: images/equivalent_python_statements.jpg
twitter_image: images/equivalent_python_statements.jpg

![Equivalent Python statements](/images/equivalent_python_statements.jpg "Equivalent Python statements")

While teaching one of my Python classes yesterday I noticed a conditional expression
which can be written in several ways. All of these are equivalent in their behavior:

    :::python
    if os.path.isdir(path) is False:
        pass
    
    if os.path.isdir(path) is not True:
        pass
    
    if os.path.isdir(path) == False:
        pass
    
    if os.path.isdir(path) != True:
        pass
    
    if not os.path.isdir(path):
        pass


My preferred style of writing is the last one (`not os.path.isdir()`) because it
looks the most pythonic of all. However the 5 expressions are slightly different
behind the scenes so they must also have different speed of execution
(click operator for link to documentation):

- [`is`](https://docs.python.org/3/reference/expressions.html#is) - identity operator,
  e.g. both arguments are the same object as determined by the
  [`id()`](https://docs.python.org/3/library/functions.html#id) function. In CPython
  that means both arguments point to the same address in memory
- [`is not`](https://docs.python.org/3/reference/expressions.html#is) -
  yields the inverse truth value of `is`, e.g. both arguments are not the same
  object (address) in memory
- [`==`](https://docs.python.org/3/library/stdtypes.html#comparisons) - equality
  operator, e.g. both arguments have the same value
- [`!=`](https://docs.python.org/3/library/stdtypes.html#comparisons) - non-equality
  operator, e.g. both arguments have different values
- [`not`](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) -
  boolean operator

In my [initial tweet](https://twitter.com/atodorov_/status/1202504284400750592) I mentioned
that I think `is False` should be the fastest. [Kiwi TCMS](http://kiwitcms.org) team
member [Zahari](https://twitter.com/real_zahari) countered with `not` to be the fastest
but didn't provide any reasoning!

My initial reasoning was as follows:

- `is` is essentially comparing addresses in memory so it should be as fast as it gets
- `==` and `!=` should be roughly the same but they do need to "read" values
  from memory which would take additional time before the actual comparison of
  these values
- `not` is a boolean operator but honestly I have no idea how it is implemented
  so I don't have any opinion as to its performance

Using the following performance test script we get the average of 100 repetitions
from executing the conditional statement 1 million times:

    :::python
    #!/usr/bin/env python
    
    import statistics
    import timeit
    
    t = timeit.Timer(
    """
    if False:
    #if not result:
    #if result is False:
    #if result is not True:
    #if result != True:
    #if result == False:
        pass
    """
    ,
    """
    import os
    result = os.path.isdir('/tmp')
    """
    )
    
    execution_times = t.repeat(repeat=100, number=1000000)
    average_time = statistics.mean(execution_times)
    
    print(average_time)


**Note:** in none of these variants the body of the if statement is executed so
the results must be pretty close to how long it takes to calculate the
conditional expression itself!


Results (ordered by speed of execution):

- `False _______ 0.009309015863109380` - baseline
- `not result __ 0.011714859132189304` - +25.84%
- `is False ____ 0.018575656899483876` - +99.54%
- `is not True _ 0.018815848254598680` - +102.1%
- `!= True _____ 0.024881873669801280` - +167.2%
- `== False ____ 0.026119318689452484` - +180.5%


Now these results weren't exactly what I was expecting. I thought `not` will come in
last but instead it came in first! Although `is False` came in second it is almost
twice as slow compared to baseline. Why is that ?

After digging around in
[CPython](https://github.com/python/cpython) I found the following definition
for comparison operators:


    :::c Python/ceval.c
    static PyObject * cmp_outcome(int op, PyObject *v, PyObject *w)
    {
        int res = 0;
        switch (op) {
        case PyCmp_IS:
            res = (v == w);
            break;
        case PyCmp_IS_NOT:
            res = (v != w);
            break;
        /* ... skip PyCmp_IN, PyCmp_NOT_IN, PyCmp_EXC_MATCH ... */
        default:
            return PyObject_RichCompare(v, w, op);
        }
        v = res ? Py_True : Py_False;
        Py_INCREF(v);
        return v;
    }


where `PyObject_RichCompare` is defined as follows (definition order reversed
in actual sources):

    :::c Objects/object.c
    /* Perform a rich comparison with object result.  This wraps do_richcompare()
       with a check for NULL arguments and a recursion check. */
    PyObject * PyObject_RichCompare(PyObject *v, PyObject *w, int op)
    {
        PyObject *res;
    
        assert(Py_LT <= op && op <= Py_GE);
        if (v == NULL || w == NULL) {
            if (!PyErr_Occurred())
                PyErr_BadInternalCall();
            return NULL;
        }
        if (Py_EnterRecursiveCall(" in comparison"))
            return NULL;
        res = do_richcompare(v, w, op);
        Py_LeaveRecursiveCall();
        return res;
    }
    
    /* Perform a rich comparison, raising TypeError when the requested comparison
       operator is not supported. */
    static PyObject * do_richcompare(PyObject *v, PyObject *w, int op)
    {
        richcmpfunc f;
        PyObject *res;
        int checked_reverse_op = 0;
    
        if (v->ob_type != w->ob_type &&
            PyType_IsSubtype(w->ob_type, v->ob_type) &&
            (f = w->ob_type->tp_richcompare) != NULL) {
            checked_reverse_op = 1;
            res = (*f)(w, v, _Py_SwappedOp[op]);
            if (res != Py_NotImplemented)
                return res;
            Py_DECREF(res);
        }
        if ((f = v->ob_type->tp_richcompare) != NULL) {
            res = (*f)(v, w, op);
            if (res != Py_NotImplemented)
                return res;
            Py_DECREF(res);
        }
        if (!checked_reverse_op && (f = w->ob_type->tp_richcompare) != NULL) {
            res = (*f)(w, v, _Py_SwappedOp[op]);
            if (res != Py_NotImplemented)
                return res;
            Py_DECREF(res);
        }
    
        /**********************************************************************
    
            IMPORTANT: actual execution enters the next block because the bool
            type doesn't implement it's own `tp_richcompare` function, see:
            Objects/boolobject.c PyBool_Type (near the bottom of that file)
    
        ***********************************************************************/
    
        /* If neither object implements it, provide a sensible default
           for == and !=, but raise an exception for ordering. */
        switch (op) {
        case Py_EQ:
            res = (v == w) ? Py_True : Py_False;
            break;
        case Py_NE:
            res = (v != w) ? Py_True : Py_False;
            break;
        default:
            PyErr_Format(PyExc_TypeError,
                         "'%s' not supported between instances of '%.100s' and '%.100s'",
                         opstrings[op],
                         v->ob_type->tp_name,
                         w->ob_type->tp_name);
            return NULL;
        }
        Py_INCREF(res);
        return res;
    }


The `not` operator is defined in `Objects/object.c` as follows (definition order
reverse in actual sources):

    :::c Objects/object.c
    /* equivalent of 'not v'
       Return -1 if an error occurred */
    int PyObject_Not(PyObject *v)
    {
        int res;
        res = PyObject_IsTrue(v);
        if (res < 0)
            return res;
        return res == 0;
    }
    
    /* Test a value used as condition, e.g., in a for or if statement.
       Return -1 if an error occurred */
    int PyObject_IsTrue(PyObject *v)
    {
        Py_ssize_t res;
        if (v == Py_True)
            return 1;
        if (v == Py_False)
            return 0;
        if (v == Py_None)
            return 0;
        /*
            IMPORTANT: skip the rest because we are working with bool so this
            function will return after the first or the second if statement!
        */
    }


So a rough overview of calculating the above expressions is:

- `not` - call 1 function which compares the argument with `Py_True/Py_False`,
  compare its result with 0
- `is/is not` - do a switch/case/break, compare the result to `Py_True/Py_False`,
   call 1 function (`Py_INCREF`)
- `==/!=` - switch/default (that is evaluate all case conditions before that),
   call 1 function (`PyObject_RichCompare`), which performs couple of
   checks and calls another function (`do_richcompare`), which does a few more checks
   before executing switch/case/compare to `Py_True/Py_False`, call `Py_INCREF`
   and return the result.

Obviously `not` has the shortest code which needs to be executed.

We can also invoke the `dis` module, aka disassembler of Python byte code into mnemonics
like so (it needs a function to dissasemble):

    :::python
    import dis
    
    def f(result):
        if False:
            pass
    print(dis.dis(f))

From the results below you can see that all expression variants are very similar:

    --------------- if False -------------------------
    
                  0 LOAD_GLOBAL              0 (False)
                  3 POP_JUMP_IF_FALSE        9
    
                  6 JUMP_FORWARD             0 (to 9)
            >>    9 LOAD_CONST               0 (None)
                 12 RETURN_VALUE            None
    --------------- if not result --------------------
                  0 LOAD_FAST                0 (result)
                  3 POP_JUMP_IF_TRUE         9
    
                  6 JUMP_FORWARD             0 (to 9)
            >>    9 LOAD_CONST               0 (None)
                 12 RETURN_VALUE            None
    --------------- if result is False ---------------
                  0 LOAD_FAST                0 (result)
                  3 LOAD_GLOBAL              0 (False)
                  6 COMPARE_OP               8 (is)
                  9 POP_JUMP_IF_FALSE       15
    
                 12 JUMP_FORWARD             0 (to 15)
            >>   15 LOAD_CONST               0 (None)
                 18 RETURN_VALUE            None
    --------------- if result is not True ------------
                  0 LOAD_FAST                0 (result)
                  3 LOAD_GLOBAL              0 (True)
                  6 COMPARE_OP               9 (is not)
                  9 POP_JUMP_IF_FALSE       15
    
                 12 JUMP_FORWARD             0 (to 15)
            >>   15 LOAD_CONST               0 (None)
                 18 RETURN_VALUE            None
    --------------- if result != True ----------------
                  0 LOAD_FAST                0 (result)
                  3 LOAD_GLOBAL              0 (True)
                  6 COMPARE_OP               3 (!=)
                  9 POP_JUMP_IF_FALSE       15
    
                 12 JUMP_FORWARD             0 (to 15)
            >>   15 LOAD_CONST               0 (None)
                 18 RETURN_VALUE            None
    --------------- if result == False ---------------
                  0 LOAD_FAST                0 (result)
                  3 LOAD_GLOBAL              0 (False)
                  6 COMPARE_OP               2 (==)
                  9 POP_JUMP_IF_FALSE       15
    
                 12 JUMP_FORWARD             0 (to 15)
            >>   15 LOAD_CONST               0 (None)
                 18 RETURN_VALUE            None
    --------------------------------------------------

The last 3 instructions are the same (that is the implicit `return None` of the function).
`LOAD_GLOBAL` is to "read" the `True` or `False` boolean constants and
`LOAD_FAST` is to "read" the function parameter in this example.
All of them `_JUMP_` outside the if statement and the only difference is
which comparison operator is executed (if any in the case of `not`).

**UPDATE:**
as I was publishing this blog post I read the following comments from
Ammar Askar who also gave me a few pointers on IRC:
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Note that this code path also has a direct inlined check for booleans, which should help too: <a href="https://t.co/YJ0az3q3qu">https://t.co/YJ0az3q3qu</a></p>&mdash; Ammar Askar (@__ammar2__) <a href="https://twitter.com/__ammar2__/status/1203012870386139137?ref_src=twsrc%5Etfw">December 6, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

So go ahead and take a look at
[`case TARGET(POP_JUMP_IF_TRUE)`](https://github.com/python/cpython/blob/e76ee1a72b9e3f5da287663ea3daec4bb3f67612/Python/ceval.c#L2989-L3001).

P.S.
----

When I teach Python I try to explain what is going on under the hood. Sometimes
I draw squares on the whiteboard to represent various cells in memory and visualize
things. One of my students asked me how do I know all of this? The essentials
(for any programming language) are always documented in its official documentation.
The rest is hacking around in its source code and learning how it works. This is
also what I expect people working with/for me to be doing!


See you soon and Happy learning!
