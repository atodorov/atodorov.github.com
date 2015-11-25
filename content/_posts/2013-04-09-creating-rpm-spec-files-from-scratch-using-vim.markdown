---
layout: post
Title: Creating RPM .spec Files From Scratch Using Vim
date: 2013-04-09 15:24
comments: true
Tags: 'tips', 'RPM'
---

On a Red Hat Enterprise Linux or Fedora (or compatible) system execute

    $ vim example.spec

This will create a new file with all the important sections and fields
already there. The template used is `/usr/share/vim/vimfiles/template.spec`
and is part of the *vim-common* RPM package.

This is very useful trick which I didn't know. Until now I always used the spec files
from previously built packages when creating new RPMs. This wasn't as fast as
creating a template and filling in the blanks.

For a detailed description about recommended RPM build practices see
the [Fedora Packaging Guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines).
