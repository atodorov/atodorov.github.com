---
layout: post
Title: Anaconda &amp; coverage.py - Pt.1 - Introduction
date: 2015-10-14 13:44
comments: true
categories: ['QA', 'fedora.planet']
---

Since early 2015 I've been working on testing installation related
components in Rawhide. I'm interested in the code produced by the
[Red Hat Installer Engineering Team](https://github.com/rhinstaller/) and in
particular in *anaconda*, *blivet*, *pyparted* and *pykickstart*. The goal of
this effort is to improve the overall testing of these components and also
have Red Hat QE contribute some of our knowledge back to the community. The benefit
of course will be better software for everyone. In the next
several posts I'll summarize what has been done so far and what's to be expected
in the future.

Test Documentation Matters
--------------------------

Do you want others to contribute tests? I certainly do! When I started looking
at the code it was obviously clear there was no documentation related to testing.
Everyone needs to know how to write and execute these tests! Currently we have
basic README files describing how to install necessary dependencies for development
and test execution, how to execute the tests (and what can be tested) and most
importantly what is the test architecture. There is description of how the file
structure is organized and which are the base classes to inherit from when adding
new tests. Most of the times each component goes through a *pylint* check and
a standard PyUnit test suite.

Test documentation is usually in a `tests/README` file. For example:

* [anaconda](https://github.com/rhinstaller/anaconda/blob/master/tests/README.rst)
* [blivet](https://github.com/rhinstaller/blivet/blob/master/tests/README.rst)
* [pykickstart](https://github.com/rhinstaller/pykickstart/blob/master/tests/README.rst)
* [pyparted](https://github.com/rhinstaller/pyparted/blob/master/tests/README.rst)

I've tried to explain as much as possible without bloating the files and going into
unnecessary details. If you spot something missing please send a pull request.


Continuous Integration
-----------------------

This has been largely an effort driven by Chris Lumens from the devel team.
All the components I'm interested in are tested regularly in a CI environment.
There is a `make ci` Makefile target for those of you interested in what exactly
gets executed.


Test Coverage
-------------

In order to **improve** something you need to know where you stand. We'll I didn't.
That's why the first step was to integrate the
[coverage.py](https://bitbucket.org/ned/coveragepy) tool with all of these components.

With the exception of blivet (written in C) all of the other
components integrate well with coverage.py and produce good statistics. pykickstart is
the champ here with 90% coverage, while anaconda is somewhere between 10% and 50%.
Full test coverage measurement for anaconda isn't straight forward and will be the
subject of my next post. For the C based code we have to hook up with
[Gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html) which shouldn't be too difficult.

At the moment there are several open pull requests to integrate the coverage test
targets with `make ci` and also report the results in human readable form. I will be
collecting these for historical references.


Tools
-----

I've created some basic text-mode
[coverage-tools](https://github.com/atodorov/coverage-tools) to help me combine and
compare data from different executions. These are only the start of it and I'm expanding
them as my needs for reporting and analytics evolve. I'm also looking into
[more detailed coverage reports](/blog/2015/07/27/call-for-ideas-graphical-test-coverage-reports/)
but I don't have enough data and use cases to work on this front at the moment.

Some ideas currently in mind:

* map code changes (git commits) to existing test coverage to get a feeling where to
invest in more testing;
* map bugs to code areas and to existing test coverage to see if we aren't
missing tests in areas where the bugs are happening;


Bugs
----

coverage.py is a very nice tool indeed but I guess most people use it in a very
limited way. Shortly after I started working with it I've found several places which
need improvements. These have to do with combining and reporting on multiple files.

Some of the interesting issues I've found and still open are:

* [PR #63 - New option --dont-remove when combining coverage data](https://bitbucket.org/ned/coveragepy/pull-requests/63/)
* [#425 - source parameter not including files which are explicitly specified](https://bitbucket.org/ned/coveragepy/issues/425)
* [#426 - Difference between coverage results with source specifies full dir instead of module name](https://bitbucket.org/ned/coveragepy/issues/426)


In my next post I will talk about anaconda code coverage and what I want to do with it.
In the mean time please use the comments to share your feedback.
