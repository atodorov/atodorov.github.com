---
layout: post
Title: Compiling Twinkle SIP Phone on RHEL 7
date: 2015-05-01 15:04
comments: true
Tags: RHEL, fedora.planet
---

One of the best SIP clients for Linux is [Twinkle](http://twinklephone.com/).
However upstream is not active (or even maybe dead) and the package is missing from
latest Fedora releases and fails to build on RHEL 7.

First you need to build and install a few dependencies in the following order:
[ucommon](http://koji.fedoraproject.org/koji/packageinfo?packageID=8437),
[ccrtp](http://koji.fedoraproject.org/koji/packageinfo?packageID=1443),
[libzrtpcpp](http://koji.fedoraproject.org/koji/packageinfo?packageID=6408).
You will also need [EPEL 7](https://fedoraproject.org/wiki/EPEL) enabled
to satisfy build dependencies.

Then apply the following patch to the original 
[twinkle.spec](http://koji.fedoraproject.org/koji/buildinfo?buildID=397914)

    --- twinkle.spec.orig	2015-05-01 14:07:01.870710147 +0300
    +++ twinkle.spec	2015-05-01 15:07:28.734734573 +0300
    @@ -47,6 +47,8 @@
     
     %build
     export LDFLAGS=-lkio 
    +export CPPFLAGS="$CPPFLAGS -I/usr/include/libzrtpcpp/" 
    +%__autoconf
     %configure
     make %{?_smp_mflags}
 

The package now builds, installs and runs successfully on RHEL 7.
The compiled packages and dependencies are available in my
[Macbook Air RHEL 7 repository](/blog/2015/04/29/rhel-7-repository-for-macbook-air/).
