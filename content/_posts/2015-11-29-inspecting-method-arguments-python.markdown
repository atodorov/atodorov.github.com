Title: Inspecting Method Arguments in Python
Headline: and creating them dynamically
date: 2015-11-29 16:04
comments: true
Tags: fedora.planet, Python

How do you execute methods from 3rd party classes in a backward compatible
manner when these methods change their arguments ?

s3cmd's [PR #668](https://github.com/s3tools/s3cmd/pull/668) is an example
of this behavior, where python-libs's `httplib.py` added a new parameter
to disable hostname checks. As a result of this
[s3cmd broke](/blog/2015/11/24/python-libs-in-rhel-7.2-broke-ssl-verification-in-s3cmd/).

One solution is to use try-except and nest as much blocks as you need to cover
all of the argument variations. In s3cmd's case we needed two nested try-except
blocks.

Another possibility is to use the
[inspect](https://docs.python.org/3/library/inspect.html) module and create the argument
list passed to the method dynamically, based on what parameters are supported.
Depending on the number of parameters this may or may not be more elegant than
using try-except blocks although it looks to me a bit more human readable.

The argument list is a member named *co_varnames* of the code object. If you
want to get the members for a function then

    inspect.getmembers(my_function.__code__)


if you want to get the members for a class method then

    inspect.getmembers(MyClass.my_method.__func__.__code__)


Consider the following example

    :::python test.py
    import inspect
    
    def hello_world(greeting, who):
        print greeting, who
    
    class V1(object):
        def __init__(self):
            self.message = "Hello World"
    
        def do_print(self):
            print self.message
    
    class V2(V1):
        def __init__(self, greeting="Hello"):
            V1.__init__(self)
            self.message = self.message.replace('Hello', greeting)
    
    class V3(V2):
        def __init__(self, greeting="Hello", who="World"):
            V2.__init__(self, greeting)
            self.message = self.message.replace('World', who)
    
    if __name__ == "__main__":
        print "=== Example: call the class directly ==="
        v1 = V1()
        v1.do_print()
    
        v2 = V2(greeting="Good day")
        v2.do_print()
    
        v3 = V3(greeting="Good evening", who="everyone")
        v3.do_print()
    
        # uncomment to see the error raised
        #v4 = V1(greeting="Good evening", who="everyone")
        #v4.do_print()
    
        print "=== Example: use try-except ==="
        for C in [V1, V2, V3]:
            try:
                c = C(greeting="Good evening", who="everyone")
            except TypeError:
                try:
                    print "    error: nested-try-except-1"
                    c = C(greeting="Good evening")
                except TypeError:
                    print "    error: nested-try-except-2"
                    c = C()
    
            c.do_print()
    
    
        print "=== Example: using inspect ==="
        for C in [V1, V2, V3]:
            members = dict(inspect.getmembers(C.__init__.__func__.__code__))
            var_names = members['co_varnames']
            args = {}
    
            if 'greeting' in var_names:
                args['greeting'] = 'Good morning'
    
            if 'who' in var_names:
                args['who'] = 'children'
    
            c = C(**args)
            c.do_print()

The output of the example above is as follows

    === Example: call the class directly ===
    Hello World
    Good day World
    Good evening everyone
    === Example: use try-except ===
        error: nested-try-except-1
        error: nested-try-except-2
    Hello World
        error: nested-try-except-1
    Good evening World
    Good evening everyone
    === Example: using inspect ===
    Hello World
    Good morning World
    Good morning children
