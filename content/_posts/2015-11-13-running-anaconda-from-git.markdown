---
layout: post
Title: Running Anaconda from git
date: 2015-11-13 10:48
comments: true
Tags: QA, fedora.planet
---

It is now possible to execute anaconda directly from a git checkout.

**Disclaimer:** this is only for testing purposes, you are not supposed to
execute anaconda from git and install a running system! My intention is
to use this feature and rewrite the Dogtail tests inside `tests/gui/` which
rely on having a LiveCD.iso and running VMs to execute. For me this has proven
very slow and difficult to debug problems in the past hence the change.

*Note:* you will need to have an active DISPLAY in your environment and
also set SELinux to permissive, see [rhbz#1276376].

Please see [PR 438](https://github.com/rhinstaller/anaconda/pull/438) for
more details.
