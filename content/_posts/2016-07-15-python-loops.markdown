Title: On Python Infinite Loops
Headline: testing a mutation testing tool
date: 2016-07-15 09:30
comments: true
Tags: QA, Python

How do you write an endless loop without using `True`, `False`, number constants
and comparison operators in Python ?

I've been working on the mutation test tool
[Cosmic Ray](https://github.com/sixty-north/cosmic-ray) and discovered that it
was missing a boolean replacement operator, that is an operator which will switch
`True` to `False` and vice versa, so I wrote one. I've also added some tests to
Cosmic Ray's test suite and then I hit the infinite loop problem.
CR's test suite contains the following code inside a module called `adam.py`

    :::python
    while True:
        break


The test suite executes mutations on `adam.py` and then runs some tests which
it expects to fail. During execution one of the mutations is
`replace break with continue` which makes the above loop infinite. The test suite
times out after a while and kills the mutation. Everything fails as expected and
we're good.

Adding my boolean replacement operator broke this function. All of the other mutations
work as expected but then the loop becomes

    :::python
    while False:
        break

When we test this particular mutation there is no infinite loop so Cosmic Ray's
test suite doesn't time out like it should and an error is reported.

    :::diff
    job ID 25:Outcome.SURVIVED:adam
    command: cosmic-ray worker adam boolean_replacer 2 unittest -- tests
    --- mutation diff ---
    --- a/home/travis/build/MrSenko/cosmic-ray/test_project/adam.py
    +++ b/home/travis/build/MrSenko/cosmic-ray/test_project/adam.py
    @@ -32,6 +32,6 @@
         return x
     
     def trigger_infinite_loop():
    -    while True:
    +    while False:
             break

So the question becomes how to write the loop condition in such a way that nothing
will mutate it but it will still remain true so that when `break` becomes `continue`
this piece of code will become an infinite loop ? Using `True` or `False` constants
obviously is a no go. Same goes for numeric constants, e.g. `1` or comparison
operators like `>`, `<`, `is`, `not`, etc. - all of them will be mutated and will
break the loop condition.

So I took a look at the docs for
[truth value testing](https://docs.python.org/2.4/lib/truth.html) and discovered
[my solution](https://github.com/sixty-north/cosmic-ray/pull/155):

    :::python
    while object():
        break


I'm creating an object instance here which will not be mutated by any of the
existing mutation operators.

Thanks for reading and happy testing!
