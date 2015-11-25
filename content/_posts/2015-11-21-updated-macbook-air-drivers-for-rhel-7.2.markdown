---
layout: post
Title: Updated MacBook Air Drivers for RHEL 7.2
date: 2015-11-21 11:27
comments: true
Tags: Mac, RHEL, fedora.planet
---

Yesterday I've upgraded to
[Red Hat Enterprise Linux 7.2](https://access.redhat.com/announcements/2058583)
on my MacBook Air and I decided to rebuild the wifi and backlight drivers.
Wifi broke immediately but I was able to fix the build with a
[simple patch](https://github.com/atodorov/wl-kmod-for-rhel7/commit/88d678a25eb702ce36f7c39471edefb65de57ad5).
I'm now using the newly built *kmod-wl-3.10.0-327.el7.x86_64-6.30.223.248-7.el7.x86_64*
and it appears to work as expected.

The *mba6x_bl* driver built without problems however I'm having problems when
closing the laptop lid. The screen stays on and (I think) the computer doesn't
suspend. My battery was drained as I left the computer as-is overnight. Suspending
from the Desktop menu however appears to work. See
[Issue #41](https://github.com/patjak/mba6x_bl/issues/41). I'd love to get some
help in debugging what's going wrong and trying to fix it. At this point I have
no idea where to look and if it's the driver to blame or something else on the system.
