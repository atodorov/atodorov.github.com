---
layout: post
title: "Bug Analysis Of RHBZ #1337"
date: 2013-09-02 16:38
comments: true
categories: ['QA']
---

In my [previous post](/blog/2013/08/23/red-hats-ebugzilla-hits-one-million-bugs/)
I asked the readers of this blog to pick a bug number from Red Hat's Bugzilla
so I can analyze it later.

[Radoslav Georgiev](http://radorado.me) decided to step up and
selected the [Leet](https://en.wikipedia.org/wiki/Leet) bug
<https://bugzilla.redhat.com/show_bug.cgi?id=1337>

This is a rather old bug against kernel, in particular
against the token ring driver. There isn't much info on the bug but it seems
the issue is hardware dependent and doesn't reproduce reliably.

Looking at the bug status and history it looks like it was closed without
fixing it. Most likely the reason for this was there was no hardware
to test, bug was not reproduced and no customers were seeing the issue or
were willing to test and work with devel!


If you'd like to see my comments on other interesting bugs just post a link
to them in the comments section.

