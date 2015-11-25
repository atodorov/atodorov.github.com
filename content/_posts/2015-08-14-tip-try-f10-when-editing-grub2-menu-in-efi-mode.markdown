---
layout: post
Title: Tip: Try F10 When Editing grub2 Menu in EFI Mode
date: 2015-08-14 14:06
comments: true
Tags: 'Fedora', 'RHEL', 'Mac', 'fedora.planet', 'tips'
---

When editing the grub2 menu (especially in EFI mode) it tells you to
press Ctrl-x to save your changes and continue the boot process.
However this doesn't work on Apple hardware
([rhbz#1253637](https://bugzilla.redhat.com/show_bug.cgi?id=1253637))
and maybe some other platforms. If this is the case try pressing **F10** 
instead. It works for me!


