---
layout: post
title: "Keeping Backwards Compatibility for pykickstart"
date: 2013-11-13 23:59
comments: true
categories: ['QA', 'Fedora']
---

Consider the following scenario:

* I'm using [SNAKE](https://fedorahosted.org/snake/) templates as part of my
installation testing work;
* SNAKE has a dependency on pykickstart;
* To test the latest and greatest kickstart features in Fedora we need the
latest version of pykickstart;
* Latest pykickstart needs Python 2.7
* Python 2.7 is not available on RHEL 6 which is used to host the test
infrastructure.


Just yesterday I hit an issue with the above setup and figured Fedora QA is
in a kind of strange situation - we always need the latest but need it
conservative enough to run on RHEL 6. See the original thread at
[kickstart-list](https://www.redhat.com/archives/kickstart-list/2013-November/msg00001.html).


In this particular case the solution will be to remove the offending code
and implement the same functionality in backward-compatible manner. Also add
more tests. I will be working on this tomorrow (there's an older patch already).


The BIG question remains though - how do you manage software evolution and still
keep it compatible with older execution stacks? Please share your experience in
the comments section.

---

PP: Spoiler - this is part of an ongoing effort to bring open source installation
testing expertise (my domain) into Fedora world, plus establish a community supported
test infrastructure. More info TBA soon.
