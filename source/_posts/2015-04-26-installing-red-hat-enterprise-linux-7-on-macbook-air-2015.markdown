---
layout: post
title: "Installing Red Hat Enterprise Linux 7 on MacBook Air 2015"
date: 2015-04-26 20:33
comments: true
categories: ['fedora.planet', 'RHEL', 'Mac']
---

Recently I've upgraded to a new 
<a href="http://www.amazon.com/gp/product/B00UGECEUY/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00UGECEUY&linkCode=as2&tag=atodorovorg-20&linkId=3YENGI5TIYKEC5GM">MacBook Air</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B00UGECEUY" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
(13 inch, early 2015) laptop and luckily enough I'm running
Red Hat Enterprise Linux 7.1 on it. Here is how to install it.

Prepare boot media
-------------------

The easiest method is to boot from a USB stick which holds
either the entire DVD or just boot.iso. Since I happened to find a 1GB only USB stick I
went for the boot.iso. `dd if=boot.iso of=/dev/sdb` is the only thing you need to prepare
the boot media.

Initial boot
-------------

![Mac boot menu](/images/mac/boot_menu.jpg "Mac boot menu")

While computer is booting hold the (left) Alt (Option) key to enter *Startup Manager*.
Wait a second or two before it displays your local hard drive and the USB boot media.
Select the option *EFI boot* to boot the anaconda installer.

Installation
------------

Booting from a boot.iso means I need to use the network to grab the rest of the installation.
Because the wireless card needs proprietary drivers
I've tried both USB to Ethernet adapter and USB tethering with my phone.

**Note:** initially I have forgotten to plug in my USB networking card which resulted in 
[bug #1191286](https://bugzilla.redhat.com/show_bug.cgi?id=1191286). After cold-plugging and
rebooting the system everything was fine. Subsequently I don't see any problems with the
USB networking card. The bug should be fixed in RHEL 7.2 btw.

**Note:** I've been using a
<a href="http://www.amazon.com/gp/product/B002PONXAI/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B002PONXAI&linkCode=as2&tag=atodorovorg-20&linkId=N4KGQKYSBSDWMMM6">USB docking station from Plugable</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B002PONXAI" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
for years because their products are Linux friendly. In particular the networking chip is ASIX and
there is no problems with drivers for Linux.

In my case I've wiped out the entire SSD disk b/c I don't care about dual boot.
Previously I've heard about anaconda crashing while it tries to detect the Mac OS file system.
I've played around with Rawhide before going for RHEL 7.1 and didn't see any problems related to
foreign filesystems.

I've gone with the default partitioning scheme while slightly modifing the partition sizes, etc.


Post install
------------

There are several issues which still need attention. I didn't have enough time in the last few
days to check these out:

**Things which work**

* GNOME 3 sucks big time. Fortunately I was able to install MATE Desktop from EPEL;
* Wireless card needs drivers; I've managed to compile them myself, 
[see here](/blog/2015/04/27/compiling-broadcom-wl-kmod-wifi-driver-for-rhel-7/);
* Display brightness doesn't seem to work at all. On top of that the display goes full black
after suspend-resume. I could barely see anything on it. 
[Fixed here](http://localhost:4000/blog/2015/04/29/fixing-display-brightness-on-macbook-air-with-rhel-7/)!
* There is a very annoying boot chime <strike>which I have no idea how to disable</strike>
[Fixed here](/blog/2015/04/27/disabling-macbook-startup-sound-in-linux/);
* The onboard keyboard is quite annoying for previous ThinkPad user like myself. Most
importantly I need to press Fn to activate the F1, F2, etc keys which I use a lot in mcedit.
[Fixed here](/blog/2015/04/30/fixing-tilde-and-function-keys-mapping-for-macbook-air-on-linux/);
* Output sound works - both speakers and headphones;
* Microphone works (tested with a hands free device);
* Power manager was reporting my battery life totally wrong but after a full discharge/recharge
it seems to have calibrated itself;
* ATrpms and EPEL are still missing some codecs for RHEL 7 which means no movies;
*UPDATE 2015-04-30:* codecs seem to work now with the [NUX Desktop](http://li.nux.ro/repos.html)
repos. Not sure what I was missing when testing it initially;

**Things that don't work yet**

* *UPDATE 2015-04-30:* I'd like to remap the Cmd key to the Menu key found in PC keyboards;
* I do have a Thunderbolt to Ethernet adapter and hot-plug seems to work (at least partially)
despite claims that this is not supported in Linux. Needs more testing;
* Camera doesn't work, reverse engineering a [driver](https://github.com/patjak/bcwc_pcie)
 is in progress;
* I need a CPU temperature monitor and maybe CPU fan speed needs adjustments;
* I have not yet tested presenting via projector but already have a few ideas how to make it work;

**UPDATE 2015-04-28:**
Check the list above for links to wifi and backlight drivers and how to disable the boot chime.

**UPDATE 2015-04-29:**
You can find precompiled RPMS in my
[Macbook Air RHEL 7 repository](/blog/2015/04/29/rhel-7-repository-for-macbook-air/).

**UPDATE 2015-04-30:**
Added more links and split the list into stuff which already works and stuff that doesn't.




Fedora 22 on MacBook Air
-------------------------

I did try Fedora 22 Beta and experienced 
[bug #1215458](https://bugzilla.redhat.com/show_bug.cgi?id=1215458).
Also for some reason the installation hit an error downloading a package and didn't let me retry
but forced me to exit the process.


I'll continue posting my updates until the system runs smoothly like it is supposed to.
