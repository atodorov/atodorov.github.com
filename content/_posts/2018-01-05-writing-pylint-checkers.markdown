Title: How to write pylint checker plugins
date: 2018-01-05 13:00
comments: true
Tags: fedora.planet, QA, Python, Django
og_image: images/validation.jpg
twitter_image: images/validation.jpg

In this post I will walk you through the process of learning how to write
additional checkers for pylint!

Prerequisites
-------------

1. Read
   [Contributing to pylint](https://pylint.readthedocs.io/en/latest/development_guide/contribute.html)
   to get basic knowledge of how to execute the test suite and how it is structured.
   Basically call `tox -e py36`. Verify that all tests **PASS** locally!

2. Read pylint's
   [How To Guides](https://pylint.readthedocs.io/en/latest/how_tos/index.html),
   in particular the section about writing a new checker. A plugin is usually
   a Python module that registers a new checker.

3. Most of pylint checkers are AST based, meaning they operate on the
   abstract syntax tree of the source code. You will have to familiarize
   yourself with the AST node reference for the `astroid` and `ast` modules.
   Pylint uses Astroid for parsing and augmenting the AST.

       **NOTE:** there is compact and excellent documentation provided by the
       *Green Tree Snakes* project. I would recommend the
       [Meet the Nodes](http://greentreesnakes.readthedocs.io/en/latest/nodes.html)
       chapter.

       Astroid also provides exhaustive documentation and
       [node API reference](http://astroid.readthedocs.io/en/latest/api/astroid.nodes.html).  

       **WARNING:** sometimes Astroid node class names don't match the ones from ast!

4. Your interactive shell weapons are `ast.dump()`, `ast.parse()`, `astroid.parse()` and
   `astroid.extract_node()`. I use them inside an interactive Python shell to
   figure out how a piece of source code is parsed and converted back to AST nodes!
   You can also try this
   [ast node pretty printer](https://bitbucket.org/takluyver/greentreesnakes/src/default/astpp.py?fileviewer=file-view-default)!
   I personally haven't used it.

How pylint processes the AST tree
---------------------------------

Every checker class may include special methods with names
`visit_xxx(self, node)` and `leave_xxx(self, node)` where xxx is the lowercase
name of the node class (as defined by astroid). These methods are executed
automatically when the parser iterates over nodes of the respective type.

All of the magic happens inside such methods. They are responsible for collecting
information about the context of specific statements or patterns that you wish to
detect. The hard part is figuring out how to collect all the information you need
because sometimes it can be spread across nodes of several different types (e.g.
more complex code patterns).

There is a special decorator called `@utils.check_messages`. You have to list
all message ids that your `visit_` or `leave_` method will generate!


How to select message codes and IDs
-----------------------------------

One of the most unclear things for me is message codes. pylint
[docs](https://pylint.readthedocs.io/en/latest/how_tos/custom_checkers.html) say

>> The message-id should be a 5-digit number, prefixed with a message category.
>> There are multiple message categories, these being `C`, `W`, `E`, `F`, `R`,
>> standing for `Convention`, `Warning`, `Error`, `Fatal` and `Refactoring`.
>> The rest of the 5 digits should not conflict with existing checkers and they
>> should be consistent across the checker. For instance, the first two digits should
>> not be different across the checker.

I'm usually having troubles with the numbering part so you will have to get creative
or look at existing checker codes.

Practical example
-----------------

In [Kiwi TCMS](http://kiwitcms.org) there's legacy code that looks like this:

    :::python
    def add_cases(run_ids, case_ids):
        trs = TestRun.objects.filter(run_id__in=pre_process_ids(run_ids))
        tcs = TestCase.objects.filter(case_id__in=pre_process_ids(case_ids))
    
        for tr in trs.iterator():
            for tc in tcs.iterator():
                tr.add_case_run(case=tc)
    
        return

Notice the dangling `return` statement at the end! It is useless because when missing
the default return value of this function will still be `None`. So I've decided to
create a plugin for that.

Armed with the knowledge above I first try the ast parser in the console:

    :::python
    Python 3.6.3 (default, Oct  5 2017, 20:27:50) 
    [GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import ast
    >>> import astroid
    >>> ast.dump(ast.parse('def func():\n    return'))
    "Module(body=[FunctionDef(name='func', args=arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Return(value=None)], decorator_list=[], returns=None)])"
    >>> 
    >>> 
    >>> node = astroid.parse('def func():\n    return')
    >>> node
    <Module l.0 at 0x7f5b04621b38>
    >>> node.body
    [<FunctionDef.func l.1 at 0x7f5b046219e8>]
    >>> node.body[0]
    <FunctionDef.func l.1 at 0x7f5b046219e8>
    >>> node.body[0].body
    [<Return l.2 at 0x7f5b04621c18>]

As you can see there is a `FunctionDef` node representing the function and it has
a `body` attribute which is a list of all statements inside the function. The last
element is `.body[-1]` and it is of type `Return`! The `Return` node also has an
attribute called `.value` which is the return value! The complete code will look
like this:

    :::python uselessreturn.py
    import astroid
    
    from pylint import checkers
    from pylint import interfaces
    from pylint.checkers import utils
    
    
    class UselessReturnChecker(checkers.BaseChecker):
        __implements__ = interfaces.IAstroidChecker
    
        name = 'useless-return'
    
        msgs = {
            'R2119': ("Useless return at end of function or method",
                      'useless-return',
                      'Emitted when a bare return statement is found at the end of '
                      'function or method definition'
                      ),
            }
    
    
        @utils.check_messages('useless-return')
        def visit_functiondef(self, node):
            """
                Checks for presence of return statement at the end of a function
                "return" or "return None" are useless because None is the default
                return type if they are missing
            """
            # if the function has empty body then return
            if not node.body:
                return
    
            last = node.body[-1]
            if isinstance(last, astroid.Return):
                # e.g. "return"
                if last.value is None:
                    self.add_message('useless-return', node=node)
                # e.g. "return None"
                elif isinstance(last.value, astroid.Const) and (last.value.value is None):
                    self.add_message('useless-return', node=node)
    
    
    def register(linter):
        """required method to auto register this checker"""
        linter.register_checker(UselessReturnChecker(linter))

Here's how to execute the new plugin:

    $ PYTHONPATH=./myplugins pylint --load-plugins=uselessreturn tcms/xmlrpc/api/testrun.py | grep useless-return
    W: 40, 0: Useless return at end of function or method (useless-return)
    W:117, 0: Useless return at end of function or method (useless-return)
    W:242, 0: Useless return at end of function or method (useless-return)
    W:495, 0: Useless return at end of function or method (useless-return)

**NOTES:**

- If you contribute this code upstream and pylint releases it you will get a traceback:

        pylint.exceptions.InvalidMessageError: Message symbol 'useless-return' is already defined

    this means your checker has been released in the latest version and you can drop the custom
    plugin!

- This is example is fairly simple because the AST tree provides the information we
  need in a very handy way. Take a look at some of
  [my other checkers](https://github.com/PyCQA/pylint/pulls/atodorov) to get a feeling
  of what a more complex checker looks like!

- Write and run tests for your new checkers, especially if contributing upstream.
  Have in mind that the new checker will be executed against existing code and in
  combination with other checkers which could lead to some interesting results.
  I will leave the testing to yourself, all is written in the documentation.


This particular example I've contributed as
[PR #1821](https://github.com/PyCQA/pylint/pull/1821) which happened to contradict
an existing checker. The update, raising warnings only when there's a single return
statement in the function body, is [PR #1823](https://github.com/PyCQA/pylint/pull/1823).


Workshop around the corner
--------------------------

I will be working together with [HackSoft](http://hacksoft.io) on an in-house
workshop/training for writing pylint plugins. I'm also looking at reviving
[pylint-django](https://github.com/landscapeio/pylint-django/) so we can
write more plugins specifically for Django based projects.

If you are interested in workshop and training on the topic let me know!


Thanks for reading and happy testing!
