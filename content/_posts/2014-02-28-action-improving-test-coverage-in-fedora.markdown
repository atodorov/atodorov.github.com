---
layout: post
Title: Call to Action: Improving Overall Test Coverage in Fedora
date: 2014-02-28 14:46
comments: true
categories: ["Fedora", "QA"]
---

Around Christmas 2013
[I said](/blog/2013/12/24/upstream-test-suite-status-of-fedora-20/)
{% blockquote %}
... it looks like on average 30% of the packages execute their test suites at
build time in the %check section and less than 35% have test suites at all!
There’s definitely room for improvement and I plan to focus on this during 2014!
{% endblockquote %}

I've recently started working on this goal by first identifying potential offending
packages and discussing the idea on Fedora's
[devel](https://lists.fedoraproject.org/pipermail/devel/2014-February/thread.html),
[packaging](https://lists.fedoraproject.org/pipermail/packaging/2014-February/thread.html)
and [test](https://lists.fedoraproject.org/pipermail/test/2014-February/thread.html)
mailing lists.

May I present you nearly **2000 packages** which need your love:

* [wiki/QA/Testing_in_check](https://fedoraproject.org/wiki/QA/Testing_in_check)
* [wiki/QA/Missing_upstream_test_suites](https://fedoraproject.org/wiki/QA/Missing_upstream_test_suites)

The intent for these pages is to serve as a source of working material for Fedora 
volunteers.


How Can I Help
----------------

* Join upstream and create a test suite for a package you find interesting;
* Provide patches - [first patch](https://lists.fedoraproject.org/pipermail/devel/2014-February/196035.html)
came in less than 30 minutes of initial announcement :);
* Review packages in the wiki and help identify false negatives;
* Forward to people who may be interested to work on these items;
* Share and promote in your local open source and developer communities;

Important
----------

If you would like to gain some open source practice and QA experience I will
happily provide mentorship and general help so you can start working on Fedora.
Just ping me!
