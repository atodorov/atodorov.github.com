---
layout: post
title: "4000+ bugs in Fedora - checksec failures"
date: 2015-09-16 17:03
comments: true
categories: ['QA', 'bugs', 'fedora.planet']
---

In the last week I've been trying to figure out how many packages
conform to the new
[Harden All Packages](https://fedoraproject.org/wiki/Changes/Harden_All_Packages)
policy in Fedora!

From 46884 RPMs, 17385 are 'x86_64' meaning they may contain ELF objects.
From them 4489 are reported as failed `checksec`.

What you should see as the output from `checksec is`

    Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH
    Full RELRO      Canary found      NX enabled    DSO             No RPATH   No RUNPATH

The first line is for binaries, the second one for libraries b/c
DSOs on x86_64 are always position-independent. Some RPATHs are acceptable,
e.g. `{% raw %}%{_libdir}/foo/{% endraw %}` and I've tried to exclude them unless
other offenses are found. The script which does this is
[checksec-collect](https://github.com/atodorov/fedora-scripts/blob/master/checksec-collect).


Most often I'm seeing *Partial RELRO*, *No canary found* and *No PIE* errors.
Since all packages potentially process untrusted input, it makes sense for all of them
to be hardened and enhance the security of Fedora. That's why all of these errors
should be considered valid bugs.

Attn package maintainers
------------------------

Please see if your package is in the list and try to fix it or let me know
why it should be excluded, for example it's a boot loader and doesn't function
properly with hardening enabled. The full list is available at
[GitHub](https://github.com/atodorov/fedora-scripts/blob/master/checksec.log).

For more information about the different protection mechanisms see the following
links:

* [Partial vs Full RELRO](http://tk-blog.blogspot.bg/2009/02/relro-not-so-well-known-memory.html)
* [Stack canaries](https://en.wikipedia.org/wiki/Buffer_overflow_protection#Canaries)
* [NX memory protection](https://en.wikipedia.org/wiki/NX_bit#Linux)
* [Position Independent Executables](https://securityblog.redhat.com/2012/11/28/position-independent-executables-pie/)
* [RPATH](https://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath)
* [RUNPATH](http://blog.tremily.us/posts/rpath/)
