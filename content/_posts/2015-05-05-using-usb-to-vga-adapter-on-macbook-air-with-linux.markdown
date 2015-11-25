---
layout: post
Title: Using USB to VGA Adapter on MacBook Air with Linux
date: 2015-05-05 14:02
comments: true
Tags: 'RHEL', 'Mac', 'fedora.planet'
---

A quick solution for MacBook Air users running Linux who want to
use external projector is to use a USB to VGA adapter. Mine is
<a href="http://www.amazon.com/gp/product/B004AIJE9G/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B004AIJE9G&linkCode=as2&tag=atodorovorg-20&linkId=74W7KWXBGC7SZ5QH">Plugable UGA-165</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B004AIJE9G" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
and it works great with Red Hat Enterprise Linux 7.1.

After the device is plugged in the *udl* kernel module is loaded
and a new framebuffer device is created (/dev/fb1 in my case). Using
*mate-display-properties* I'm able to configure the 2nd monitor attached
to the USB video card. I was able to succeffully display an OpenOffice
presentation on the 2nd monitor and play YouTube video.

All USB 2.0 devices from Plugable should be well supported on Linux.
For USB 3.0 David Airlie from Red Hat is doing some reverse engineering
but I have no idea what the status is. For more info see:

* <http://plugable.com/2012/06/21/displaylink-usb-devices-on-linux-kernel-3-4-0>
* <http://airlied.livejournal.com/80307.html>
* <http://airlied.livejournal.com/80516.html>
* <http://airlied.livejournal.com/80797.html>
