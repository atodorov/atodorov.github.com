---
layout: post
Title: Last Week in Fedora QA
date: 2014-03-03 10:23
comments: true
Tags: Fedora, QA
---

Here are some highlights from the past week discussions in Fedora which I found
interesting or participated in.

Call to Action: Improving Overall Test Coverage in Fedora
---------------------------------------------------------

I can not stress enough how important it is to further
[improve test coverage in Fedora](/blog/2014/02/28/action-improving-test-coverage-in-fedora/)!
You can help too. Here's how:

* Join upstream and create a test suite for a package you find interesting;
* Provide patches - [first patch](https://lists.fedoraproject.org/pipermail/devel/2014-February/196035.html)
came in less than 30 minutes of initial announcement :);
* Review packages in the wiki and help identify false negatives;
* Forward to people who may be interested to work on these items;
* Share and promote in your local open source and developer communities;


Auto BuildRequires
------------------

[Auto-BuildRequires](http://people.redhat.com/~rjones/auto-buildrequires/)
is a simple set of scripts which compliments `rpmbuild` by
automatically suggesting BuildRequires lines for the just built package.

It would be interesting to have this integrated into Koji and/or
continuous integration environment and compare the output between every two
consecutive builds (iow older and newer package versions). It sounds like a
good way to identify newly added or removed dependencies and update the package
specs accordingly.


How To Test Fonts Packages
-------------------------------

This is exactly what 
[Christopher Meng asked](https://lists.fedoraproject.org/pipermail/test/2014-February/120570.html)
and frankly I have no idea. 

I've come across a few fonts packages (*amiri-fonts*, *gnu-free-fonts* and *thai-scalable-fonts*)
which seem to have some sort of test suites but I don't know how they work or
what type of problems they test for. On top of that all three have a different
way of doing things (e.g. not using a standardized test framework or a variation of such).

I'll keep you posted on this once I manage to get more info from upstream developers.


Is URL Field in RPM Useless
---------------------------

So is it? Opinions here differ from totally useless to "don't remove it, I need it".
However I run a small test and from 2574 RPMs on the source DVD there is around 
40% of "something different than HTTP 200 OK". This means **40% potentially broken URLs**!

The majority are responses in the 3XX range and only less than 10% are 
actual errors (4XX, 5XX, missing URLs or connection errors).


It will be interesting to see if this can be removed from `rpm` altogether.
I don't think it will happen soon but if we don't use it why have it there? 

My script for the test is
[here](https://github.com/atodorov/fedora-scripts/blob/master/test-rpm-url-field.sh).


