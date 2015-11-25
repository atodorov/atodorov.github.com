---
layout: post
Title: RHEL 7 Repository for MacBook Air
date: 2015-04-29 13:00
comments: true
Tags: 'RHEL', 'Mac', 'fedora.planet'
---

I've made a repository with binary (x86_64 only) and source RPM packages which
are missing from Red Hat Enterprise Linux 7 and necessary when using a 
MacBook Air. To install execute the commands below:

    cd /etc/yum.repos.d/
    wget https://s3.amazonaws.com/atodorov/rpms/macbook/el7/rhel7-macbook.repo


Wireless driver
---------------

    yum install kmod-wl


Display backlight driver
------------------------

    yum install kmod-mba6x_bl


And uncomment `/etc/X11/xorg.conf.d/98-mba_bl.conf`.

*Note:* the .spec file is available from 
[RP #26](https://github.com/patjak/mba6x_bl/pull/26).

Fixing keyboard mapping
-----------------------

    yum install mba-kbd-fix

