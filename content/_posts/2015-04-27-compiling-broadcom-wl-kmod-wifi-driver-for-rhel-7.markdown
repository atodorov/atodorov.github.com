---
layout: post
Title: Compiling Broadcom wl-kmod WiFi Driver for RHEL 7
date: 2015-04-27 12:17
comments: true
Tags: fedora.planet, RHEL, Mac
---

After I got my 
[[MacBook Air]] [installed with RHEL 7.1](/blog/2015/04/26/installing-red-hat-enterprise-linux-7-on-macbook-air-2015/)
the first priority was getting wireless working. 
First check if your device isn't already supported
[upstream](http://linuxwireless.org/en/users/Drivers/b43/#Supported_devices). Mine isn't

    14e4:43a0: Broadcom Corporation BCM4360 802.11ac Wireless Network Adapter (rev 03)

Next grab the src.rpm files necessary to build the *wl* driver from RPM Fusion.
For `akmods-0.5.2-1.fc21.src.rpm`, `broadcom-wl-6.30.223.248-2.fc21.src.rpm`,
`kmodtool-1-23.fc20.src.rpm` just execute *rpmbuild --rebuild* against each file
and install `kmodtool` and `akmods`.

Then you need two more files `buildsys-build-rpmfusion` and `wl-kmod`.
The first one is a helper tool containing list of recent kernels to build against,
the later one is the driver source itself. Both needed minor modifications before
building on RHEL 7.

I've created my own 
[buildsys-build-rpmfusion](https://github.com/atodorov/buildsys-build-rpmfusion-for-rhel7) package listing the current kernels
for RHEL 7.1. For [wl-kmod](https://github.com/atodorov/wl-kmod-for-rhel7) I've introduced a 
[patch](https://github.com/atodorov/wl-kmod-for-rhel7/blob/master/wl-kmod-100_redhat.patch)
which modifies the other patches in the package so it builds correctly on 7.1.

**Note:** I don't know if there's a define which can be used to detect if we're building
on RHEL (maybe I can define my own) but direct kernel version number comparison doesn't
work here because Red Hat backports chosen functionality from more recent kernels without
changing the version number. This approach may not be the best one but I've tried to keep it clean
for easier maintenance in the future and it got me started very quickly.

Build the modified buildsys-build-rpmfusion and:

    yum install buildsys-build-rpmfusion-7-1.x86_64.rpm buildsys-build-rpmfusion-kerneldevpkgs-current-7-1.x86_64.rpm


Build the wl-kmod package and:

    yum install akmod-wl-6.30.223.248-5.el7.x86_64.rpm broadcom-wl-6.30.223.248-2.el7.noarch.rpm kmod-wl-3.10.0-229.el7.x86_64-6.30.223.248-5.el7.x86_64.rpm kmod-wl-6.30.223.248-5.el7.x86_64.rpm

If necessary re-create your initramfs image to include *wl.ko*.
