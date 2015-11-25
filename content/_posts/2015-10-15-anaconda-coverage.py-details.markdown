---
layout: post
Title: Anaconda &amp; coverage.py - Pt.2 - Details
date: 2015-10-15 14:15
comments: true
Tags: 'QA', 'fedora.planet'
---

My [previous post](/blog/2015/10/14/anaconda-coverage.py-introduction/)
was an introduction to testing installation related components. Now I'm going to
talk more about anaconda and how it is tested.

There are two primary ways to test anaconda. You can execute `make check` in the
source directory which will trigger the package test suite. The other possibility
is to perform an actual installation, on bare meta or virtual machine, using the
[latest Rawhide snapshots](https://kojipkgs.fedoraproject.org/mash/) which also
include the latest anaconda. For both of these methods we can collect code
coverage information. In live installation mode coverage is enabled via the
`inst.debug` boot argument. Fedora 23 and earlier use `debug=1` but that
can lead to [problems](https://github.com/rhinstaller/anaconda/pull/291)
sometimes.


Kickstart Testing
-----------------

[Kickstart](https://github.com/rhinstaller/pykickstart/blob/master/docs/kickstart-docs.rst)
is a method of automating the installation of Fedora by supplying the necessary
configuration into a text file and pointing the installer at this file. There is
the directory `tests/kickstart_tests`, inside the anaconda source, where each
test is a kickstart file and a shell script. The test runner provisions a virtual
machine using boot.iso and the kickstart file. A shell script then verifies
installation was as expected and copies files of interest to the host system.
Kickstart files are also the basis for testing Fedora installations in
[Beaker](https://beaker.fedoraproject.org/bkr/jobs/).

Naturally some of these in-package kickstart tests are the same as
[out-of-band kickstart tests](https://bitbucket.org/fedoraqa/fedora-beaker-tests/).
Hint: there are more available but not yet public.

The question which I don't have an answer for right now is
"Can we remove some of the duplicates and how this affects devel and QE teams" ?
The pros of in-package testing are that it is faster compared to Beaker. The cons
are that you're not testing the real distro (every snapshot is a possible final
release to the users).


Dogtail
--------

[Dogtail](https://fedorahosted.org/dogtail/) uses accessibility technologies to
communicate with desktop applications. It is written in Python and can be used
as GUI test automation framework. Long time ago I've proposed support for Dogtail
in anaconda which was rejected, then couple of years later it was accepted and
later removed from the code again.

Anaconda has in-package Dogtail tests (`tests/gui/`). They work by attaching
a second disk image with the test suite to a VM running a LiveCD. Anaconda is
started on the LiveCD and an attempt to install Fedora on disk 1 is made.
Everything is driven by the Dogtail scripts. There are only a few of these
tests available and they are currently disabled.
Red Hat QE has also created another method for running Dogtail tests in anaconda
using an updates.img with the previous functionality.


Even if there are some duplicate tests I'm not convinced we have to drop the
`tests/gui/` directory from the code because
the framework used to drive the graphical interface of anaconda appears to be very
well written. The code is clean and easy to follow.
Also I don't have metrics of how much these two methods differ or how much they cover
in their testing. IMO they are pretty close and before we can find a way to
reliably execute them on a regular basis there isn't much to be done here.
One idea is to use the `--dirinstall` or `--image` options and skip the
LiveCD part entirely.


How Much is Tested
------------------

`make ci` covers 10% of the entire code base for anaconda. Mind you that
`tests/storage` and `tests/gui` are currently disabled.
See [PR #346](https://github.com/rhinstaller/anaconda/pull/346),
[PR #327](https://github.com/rhinstaller/anaconda/pull/327) and
[PR #319](https://github.com/rhinstaller/anaconda/pull/319)!
There is definitely room for improvement.

On the other hand live installation testing is much
better. Text mode covers around 25% while graphical installations around 40%.
Text and graphical combined cover 50% though. These numbers will drop quite a bit
once anaconda learns to
[include all possible files](https://github.com/rhinstaller/anaconda/pull/397)
in its report but it is a good estimate.


The important questions to ask here are:

* How much can PyUnit tests cover in anaconda?
* How much can kickstart tests cover ?
* Have we reached a threshold in any of the two primary methods for testing ?
* Does UI automation (with Dogtail) improve anything ?
* When testing a particular feature (say user creation) how different is the
code execution path between manual (GUI) testing, kickstart and unit testing ?
If not so different can we invest in unit tests instead of higher level tests then ?
* How different is the code execution path between different tests (manual or kickstart) ?
In other words how much value are we getting from testing for the resources we're putting in ?


In my next post I will talk more about these questions and some rudimentary
analysis against coverage data from the various test methods and test cases!
