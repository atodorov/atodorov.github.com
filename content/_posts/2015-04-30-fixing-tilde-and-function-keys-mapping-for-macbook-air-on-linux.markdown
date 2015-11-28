---
layout: post
Title: Fixing Tilde and Function Keys Mapping for MacBook Air on Linux
date: 2015-04-30 11:33
comments: true
Tags: RHEL, Mac, fedora.planet
---

Thera are two problems with the [[MacBook Air]] keyboard on Linux:

Function keys and media keys are switched and by default you have to
press Fn+F5 in order to refresh a browser page. The 
[solution](https://chaidarun.com/fedora-mbp) is

    echo 2 > /sys/module/hid_apple/parameters/fnmode

The tilde key is mapped improperly, see 
[RHBZ #1025041](https://bugzilla.redhat.com/show_bug.cgi?id=1025041#c2).
To fix it

    echo 0 > /sys/module/hid_apple/parameters/iso_layout

Permanent fix
-------------

Either you have to add the above commands in a boot script or you can
`yum install mba-kbd-fix` from my
[Macbook Air RHEL 7 repository](/blog/2015/04/29/rhel-7-repository-for-macbook-air/).
The RPM source can be found [here](https://github.com/atodorov/mba-kbd-fix).
