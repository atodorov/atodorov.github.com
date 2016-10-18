---
layout: post
Title: Updated MacBook Air Drivers for RHEL 7.3
date: 2016-10-18 13:27
comments: true
Tags: Mac, RHEL, fedora.planet
Slug: updated-macbook-air-drivers-for-rhel-7.3
---

Today I have re-build the wifi and backlight drivers for MacBook Air
against the upcoming Red Hat Enterprise Linux 7.3 kernel.
*wl-kmod* again needed a
[small patch](https://github.com/atodorov/wl-kmod-for-rhel7/commit/c6b3d0fde66dd29671df5f52c40f7395f1e1e59e)
before it can be compiled. *mba6x_bl* has been updated to the latest
upstream and compiled without errors. The current RPM versions are

    akmod-wl-6.30.223.248-9.el7.x86_64.rpm
    kmod-wl-3.10.0-513.el7.x86_64-6.30.223.248-9.el7.x86_64.rpm
    kmod-wl-6.30.223.248-9.el7.x86_64.rpm
    wl-kmod-debuginfo-6.30.223.248-9.el7.x86_64.rpm

    kmod-mba6x_bl-20161018.d05c125-1.el7.x86_64.rpm
    kmod-mba6x_bl-3.10.0-513.el7.x86_64-20161018.d05c125-1.el7.x86_64.rpm
    mba6x_bl-common-20161018.d05c125-1.el7.x86_64.rpm

and they seem to work fine for me. Let me know if you have any issues
after RHEL 7.3 comes out officially.

PS: The [bcwc_pcie](https://github.com/patjak/bcwc_pcie) driver for the video camera
appears to be ready for general use, regardless of some issues. No promises here
but I'll try to compile that one as well and provide it in my
[Macbook Air RHEL 7 repository]({filename}2015-04-29-rhel-7-repository-for-macbook-air.markdown).
