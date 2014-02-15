---
layout: post
title: "7 Years and 1400 Bugs Later as Red Hat QA"
date: 2014-02-15 10:43
comments: true
categories: ['RHEL', 'Fedora', 'QA']
---

![Platform QE](/images/redhat_platform_qe.jpg "Platform QE")

Today I celebrate my 7th year working in Red Hat's Quality Engineering department.
Here's my story!

On a cold winter Friday in 2007 I left my job as a software developer in Sofia,
packed my stuff together, purchased my [first laptop](http://amzn.to/1hlPuyr) and
on Sunday jumped the train to Brno to join the Release Test Team at Red Hat.
Little did I know what it was all about. When I was offered the position
I was on a very noisy bus and had to pick between two positions. I didn't quite understood
what were the options and just picked the second one.
Luckily everything turned out great and continues to this day.


What do I do exactly
--------------------

From all QE teams RTT is the first one and last one to test a release. The team has
both technical function and a more managerial one. Our focus
is on the core Red Hat Enterprise Linux product and sometimes additional
layered products as required. 

We are the first to test a new nightly build or a
snapshot of the upcoming RHEL release. If all goes well other QA teams take over
and do their magic. At the end when bits are published live we're the last to
verify that content is published where it is expected to be. In short this is
covering the work of the release engineering team which is to build a product and
publish the contents for consumption.

The same principles apply to Fedora although the engagement here is less demanding.

Personally I have been and continue to be responsible for Red Hat Enterprise Linux 5
family of releases. It's up to me to give the go ahead for further testing. This position
also has the power to block and delay the GA release if not happy with testing or
there is a considerable risk of failure until things are sorted out - which I've done
once and it's a hard decision to make.


Like in other QA teams I have to create test plan documents, write test case scenarios,
implement test automation scripts (and sometimes tools), regularly execute said test
plans and test cases, find and report any new bugs and verify old ones are fixed. 
Most importantly make sure RHEL installs and is usable for further testing :).

Sometimes I have to deal with capacity planning and as RHEL 5 tech lead I have to organize
and manage (for a lack of better word) the entire testing campaign for RTT for that product.

Stats and Numbers
-----------------

It is hard (if not impossible) to [measure QA work](https://github.com/atodorov/qe-metrics)
with numbers alone but here are some interesting facts about my experience so far.

* Nearly 1400 bugs filed (1390 at the time of writing);
* Reported bugs across 32 different products. Top 3 being RHEL 6, RHEL 5 and Fedora (1000+ bugs);
* Top 3 components for reporting bugs: anaconda, releng, kernel;
* Nearly 100 bugs filed in my first year 2007;
* The 3 most productive years being 2010, 2009, 2011 (800 + bugs); 
* Filed 200 bugs/year which is about 1 bug/day considering holidays;
* 35th top bug reporter (excluding robot accounts). I was in top 10 a few years back;

Many of the bugs I report are private so if you'd like to know more stats just ask me
and I'll see what I can do.


2007
----




2008
----

2009
----

2010
----

2011
----

2012
----

2013
----

2014
----








What do I do now
----------------

During the last year I have gradually changed my responsibilities to work more on Fedora
as a volunteer in the Fedora QA team. As part of Fedora QA I'm regularly testing installation
of Rawhide trees and [work with community](/blog/2013/09/23/fedora-test-days-are-coming-to-sofia/).
I also like to work on [process](//blog/2013/12/24/upstream-test-suite-status-of-fedora-20/) and
[infrastructure improvement](/blog/2013/11/19/open-source-quality-assurance-infrastructure-for-fedora-qa/)
both externally with Fedora and internally for RHEL.






