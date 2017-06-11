Title: Can a nested function assign to variables from the parent function
Headline: examples and workarounds in Python
date: 2017-06-11 23:00
comments: true
Tags: Python, fedora.planet


While working on a
[new feature for Pelican](https://github.com/getpelican/pelican/pull/1909)
I've put myself in a situation where I have two functions, one nested inside
the other and I want the nested function to assign to variable from the
parent function. Turns out this isn't so easy in Python!

    :::python hello.py
    def hello(who):
        greeting = 'Hello'
        i = 0
    
        def do_print():
            if i >= 5:
                return
    
            print i, greeting, who
            i += 1
            do_print()
    
        do_print()
    
    if __name__ == "__main__":
        hello('World')

The example above is a recursive *Hello World*. Notice the `i += 1` line!
This line causes `i` to be considered local to `do_print()` and the result
is that we get the following failure on Python 2.7:

    :::python
    Traceback (most recent call last):
      File "./test.py", line 16, in <module>
        hello('World')
      File "./test.py", line 13, in hello
        do_print()
      File "./test.py", line 6, in do_print
        if i >= 5:
    UnboundLocalError: local variable 'i' referenced before assignment

We can workaround by using a global variable like so:

    :::python hello.py using global variable
    i = 0
    def hello(who):
        greeting = 'Hello'
    
        def do_print():
            global i
    
            if i >= 5:
                return
    
            print i, greeting, who
            i += 1
            do_print()
    
        do_print()

However I prefer not to expose internal state outside the `hello()`
function. Only if there was a keyword similar to **global**. In Python 3
there is **nonlocal**!

    :::python hello.py using nonlocal, Python 3
    def hello(who):
        greeting = 'Hello'
        i = 0
    
        def do_print():
            nonlocal i
    
            if i >= 5:
                return
    
            print(i, greeting, who)
            i += 1
            do_print()
    
        do_print()


**nonlocal** is nice but it doesn't exist in Python 2! The workaround is to
not assign state to the variable itself, but instead use a mutable container.
That is instead of a scalar use a list or a dictionary like so:

    :::python hello.py where i is a list, Python 2
    def hello(who):
        greeting = 'Hello'
        i = [0]
    
        def do_print():
            if i[0] >= 5:
                return
    
            print i[0], greeting, who
            i[0] += 1
            do_print()
    
        do_print()


Thanks for reading and happy coding!
