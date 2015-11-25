---
layout: post
Title: Call for Ideas: Graphical Test Coverage Reports
date: 2015-07-27 13:04
comments: true
Tags: Fedora, QA, Django, fedora.planet
---

If you are working with Python and writing unit tests chances are you are
familiar with the [coverage](http://nedbatchelder.com/code/coverage/) reporting
tool. However there are testing scenarios in which we either don't use unit tests
or maybe execute different code paths(test cases) independent of each other.

For example, this is the case with installation testing in Fedora. Because anaconda
- the installer is very complex the easiest way is to test it live, not with unit tests.
Even though we can get a coverage report (anaconda is written in Python) it reflects
only the test case it was collected from.

`coverage combine` can be used to combine several data files and produce an aggregate
report. This can tell you how much test coverage you have across all your tests.

As far as I can tell Python's coverage doesn't tell you how many times a particular
line of code has been executed. It also doesn't tell you which test cases executed
a particular line
(see [PR #59](https://bitbucket.org/ned/coveragepy/pull-request/59)).
In the Fedora example, I have the feeling many of our tests are touching the same
code base and not contributing that much to the overall test coverage.
So I started working on these items.

I imagine a script which will read coverage data from several test executions
(preferably in JSON format, 
[PR #60](https://bitbucket.org/ned/coveragepy/pull-request/60)) and produce a 
graphical report similar to what GitHub does for your commit activity.

See an example [here](https://s3.amazonaws.com/atodorov/blog/pykickstart_report.html)!

The example uses darker colors to indicate more line executions, lighter for less
executions. Check the HTML for the actual numbers b/c there are no hints yet.
The input JSON files are
[here](https://s3.amazonaws.com/atodorov/blog/coverage_json_reports.tar.gz) and
the script to generate the above HTML is at 
[GitHub](https://github.com/atodorov/fedora-scripts/blob/master/coverage-tool).

Now I need your ideas and comments!

What kinds of coverage reports are you using in your job ? How do you generate them ?
How do they look like ?
