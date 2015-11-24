---
layout: post
title: "Upstream Test Suite Status of Fedora 20"
date: 2013-12-24 08:01
comments: true
categories: ['Fedora', 'QA']
---

Last week I've expressed my thoughts about the state of
[upstream test suites in Fedora](https://lists.fedoraproject.org/pipermail/test/2013-December/119637.html)
along with some other ideas. Following the response on this thread I'm starting
to analyze all SRPM packages in Fedora 20 in order to establish a baseline. Here are my initial findings.

What's Inside
-------------

I've found two source distributions for Fedora 20:

* The `Fedora-20-source-DVD.iso` file which to my knowledge contains the sources
of all packages that comprise the installation media;
* The `Everything/source/SRPMS/` directory which appears to contain the sources
of everything else available in the Fedora 20 repositories.


There are **2574** SRPM packages in Fedora-20 source DVD and **14364** SRPMs
in the Everything/ directory. 9,2G vs. 41G.



Test Suite Execution In %check
------------------------------

[Fedora Packaging Guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines#Test_Suites)
state

{% blockquote %}
If the source code of the package provides a test suite,
it should be executed in the {% raw %}%check{% endraw %} section,
whenever it is practical to do so.
{% endblockquote %}


In my research I found **738** SRPMs on the DVD which have a {% raw %}%check{% endraw %}
section and **4838** such packages under `Everything/`. This is **28,6%** and **33,6%**
respectively.

Test Suite Existence
---------------------

A quick grep for either `test/` or `tests/` directories in the package sources revealed
**870** SRPM packages in the source DVD which are very likely to have a test suite.
This is **33,8%**. <strike>I wasn't able to inspect the `Everything/` directory with this script
because it takes too long to execute and my system crashed out of memory.
I will update this post later with that info.</strike>

*UPDATE 2014-01-02*: 
In the `Everything/` directory only **4481** (**31,2%**) SRPM packages appear to have
test suites.

The scripts and raw output are available at <https://github.com/atodorov/fedora-scripts>.

So it looks like on average **30%** of the packages execute their test suites at build
time in the {% raw %}%check{% endraw %} section and less than **35%** have test suites at all!
There's definitely room for improvement and I plan to focus on this during 2014!


