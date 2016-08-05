Title: Python 2 vs. Python 3 List Sort Causes Bugs
Headline: and crashes django-chartit
date: 2016-08-05 10:30
comments: true
Tags: QA, Python

Can sorting a list of values crash your software? Apparently it can and is
another example of my
[Hello World Bugs]({filename}2016-03-25-hello-world-bug-challenge.markdown).
Python 3 has simplified the
[rules for ordering comparisons](https://docs.python.org/3/whatsnew/3.0.html#ordering-comparisons)
which changes the behavior of sorting lists when their contents are dictionaries.
For example:

    :::python
    Python 2.7.5 (default, Oct 11 2015, 17:47:16) 
    [GCC 4.8.3 20140911 (Red Hat 4.8.3-9)] on linux2
    >>> 
    >>> [{'a':1}, {'b':2}] < [{'a':1}, {'b':2, 'c':3}]
    True
    >>>

    :::python
    Python 3.5.1 (default, Apr 27 2016, 04:21:56) 
    [GCC 4.8.3 20140911 (Red Hat 4.8.3-9)] on linux
    >>> [{'a':1}, {'b':2}] < [{'a':1}, {'b':2, 'c':3}]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unorderable types: dict() < dict()
    >>>


The problem is that the second elements in both lists have different keys
and Python doesn't know how to compare them. In earlier Python versions
this has been special cased as
[described here](http://stackoverflow.com/questions/3484293/is-there-a-description-of-how-cmp-works-for-dict-objects-in-python-2/3484456#3484456)
by Ned Batchelder (the author of Python's coverage tool) but in Python 3
dictionaries have no natural sort order.

In the case of *django-chartit* (of which I'm now the official maintainer) this
bug triggers when you want to plot data from multiple sources (models) on the same
chart. In this case the fields coming from each data series are different and the
above error is triggered.

I have worked around this in
[commit 9d9033e](https://github.com/chartit/django-chartit/commit/9d9033ecd5a8592a12872293cdf6d710cebf894f)
by simply disabling an iterator sort but this is sub-optimal and I'm not quite certain
what the side effect might be. I suspect you may end up with a chart where the order
of values on the X axis isn't the same for the different models, e.g. one graph plotting
the data in ascending order the other one in descending.

The trouble also comes from the fact that we're sorting an iterator (a list of fields) by
telling Python to use a list of dicts to determine the sort order. In this arrangement
there is no way to tell Python how we want to compare our dicts. The only solution I
can think about is creating a custom class and implementing a custom `__cmp__()` method
for this data structure!
