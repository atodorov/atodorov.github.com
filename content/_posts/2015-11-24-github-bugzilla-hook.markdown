---
layout: post
Title: GitHub Bugzilla Hook
date: 2015-11-24 13:32
comments: true
Tags: 'QA', 'fedora.planet'
---

Last month I've created a tool which adds comments to Bugzilla when a commit
message references a bug number. It was done as a proof of concept and didn't
receive much attention at the time. Today I'm happy to announce the existence
of [GitHub Bugzilla Hook](https://github.com/atodorov/github-bugzilla-hook).

I've used David Shea's
[GitHub Email Hook](https://github.com/rhinstaller/github-email-hook/) as my
starting template and only modified it where needed. GitHub Bugzilla Hook will
examine push data and post comments for every unique bug+branch combination.
Once a comment for that particular bug+branch combination is made, new ones
will not be posted, even if later commits reference the same bug.
My main assumption is commits which are related to a bug will be pushed together
most of the times so there shouldn't be lots of noise in Bugzilla.

See [rhbz#1274703](https://bugzilla.redhat.com/show_bug.cgi?id=1274703) for
example of how the comments look. The parser behavior is taken from anaconda
and conforms to the style the Red Hat Installer Engineering Team uses.
Hopefully you find it useful as well.

My next step is to find a hosting place for this script and hook it up
with the rhinstaller GitHub repos!

