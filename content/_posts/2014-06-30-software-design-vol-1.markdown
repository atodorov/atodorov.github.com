---
layout: post
Title: Software Design Vol. 1
date: 2014-06-30 23:22
comments: true
categories: 
---

I'm starting a new series where I will share my thoughts about software design,
usability and other related topics with examples of items I like or dislike.
I've
[written before](/blog/2013/05/30/why-vmware-multi-hypervisor-manager-architecture-is-wrong/)
about the topic so consider this post as a sequel. I'm starting with couple of
examples from the mobile world. Plese use the comments to tell if there is something
that you particulary like or dislike in software or hardware design
(and apologies to my readers for not being able to post more frequently lately).


BlackBerry Camera Burst Feature vs. Android
--------------------------------------------

BlackBerry 10 Camera's burst mode is well made in my opinion. It is capable of
taking thousands of pictures and saving the to disk without interruption. Thus
I am capable of taking pictures of fast moving objects like flash lights.

![Flash light](/images/flashlight.jpg "Flash light")

On the other hand I have access to an 
<a target="_blank" href="http://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-keywords=htc%20one&linkCode=ur2&tag=atodorovorg-20&url=search-alias%3Daps&linkId=CZ33VB6BARW7FWZS">HTC One smartphone</a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
with Android. The burst
mode feature there is particularly crappy. It shoots between 20 to 50 photos
(haven't counted how much exactly), then takes a second to flash everything to disk,
then pops a question asking the user to select the best one and possibly delete
the rest. If you don't want all of this just tap the back button to return to
shooting mode.


BlackBerry Hub
---------------

Hub is another well designed application which integrates all of your accounts and
messaging into the core of the OS although other mobile OSes have a similar feature
as well if I'm not mistaken. I just mention it because it is easy and comfortable to use.


BlackBerry Memory Management
----------------------------

BlackBerry 10 OS memory management is particularly crappy with respect to
the end user. I'm not sure whether this is due to QNX being real-time OS
or just the Java stack keeping stuff in memory.

After some usage my development Z10 will begin experiencing out of memory issues
(it has 1 GB of RAM vs. 2 GB in production hardware). This will lead to apps
crashing, web pages that were able to open, not being able to load and the most
annoying of all - camera starts taking pictures with random color spots.

![Blackberry camera fail](/images/bbz10camerafail.jpg "BlackBerry Z10 camera fail")

After restarting the device everything is back to normal :(.

BlackBerry Date and Time Synchronization
----------------------------------------

This one I also hate a lot. It appears that the software is designed to
automatically synchronize over the Internet and without a reliable connection fails miserably.
After reboot (or even worse battery removal) the device will start with a fixed date and time
somewhere in the past. If it fails to synchronize or takes too long several things happen:

* The Blackberry Hub application loads first (email and other accounts) which causes all sorts
of warnings of invalid SSL certificates. Which in their own right are annoying because Cancel
means dismiss the warning until the next connection retry; which blocks access to the main menu
for manual configuration;
* All images taken by the Camera app will be saved on disk with the wrong date which makes you think
they are gone; I've found this by accident while scrolling way back in my history looking for something
unrelated.


Multiple File Selection
-------------------------

I haven't tested this explicitly on Android or other mobile devices but on BlackBerry
the user needs to tap each individual object to select it. My guess is this is similar
on all devices utilizing a touch screen.  However such interface makes it damn hard to
select a thousand files for deletion (the unusable results from the camera burst mode feature).
Luckily Z10 (and possibly others) has a shell application with `cp`, `mv` and `rm -f` commands.

