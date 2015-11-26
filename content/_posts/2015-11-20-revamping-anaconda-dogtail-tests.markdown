---
layout: post
Title: Revamping Anaconda's Dogtail Tests
date: 2015-11-20 15:34
comments: true
Tags: QA, fedora.planet
Slug: revamping-anaconda-dogtail-tests
---

In my [previous post](/blog/2015/11/13/running-anaconda-from-git/) I briefly talked
about running anaconda from a git checkout. My goal was to rewrite `tests/gui/` so
that they don't use a LiveCD and virtual machines anymore. I'm pleased to announce
that this is already done (still not merged), see 
[PR#457](https://github.com/rhinstaller/anaconda/pull/457).

The majority of the changes are just shuffling bits around and deleting
unused code. The existing UI tests were mostly working and only needed minor
changes. There are two things which didn't work and are temporarily disabled:

* Clicking the Help button results in [rhbz#1282432],
which in turn may be hiding another bug behind it;
* Looping over the available languages resulted in AT-SPI NonImplementedError
which I'm going to debug next.

To play around with this make sure you have accessibility enabled and:

    # cd anaconda/
    # export top_srcdir=`pwd`
    # setenforce 0
    # cd tests/gui/
    # ./run_gui_tests.sh


**Note:** you also need Dogtail for Python3 which isn't officially available
yet. I'm building from
<https://vhumpa.fedorapeople.org/dogtail/beta/dogtail3-0.9.1-0.3.beta3.src.rpm>

My future plans are to figure out how to re-enable what is temporarily
disabled, update `run_gui_tests.sh` to properly start gnome-session and
enable accessibility, do a better job cleaning up after a failure,
enable coverage and hook everything into `make ci`.

Happy testing!
