---
layout: post
title: "Lenovo Rants: Battery and Dock Flaws"
date: 2013-09-15 10:23
comments: true
categories: ['bugs', 'QA']
---

To all my readers - sorry for not being able to blog more frequently lately.
Here's an easy read about my favourite laptop brand Lenovo and some of their
design flaws I've found.

X220 and T60 Batterries are ALMOST Identical
---------------------------------------------

!["X220 and T60 batteries"](/images/lenovo_x220_t60_battery.jpg "X220 and T60 batteries")

As you can see the [X220](http://amzn.to/12y5hwp) and 
[T60](http://amzn.to/183SgiR) batteries are nearly identical with the notable
exception of the connector placement. The end result - I have to purchase yet another
battery as a backup for long travel/work on the go. Not what I want.

I wish all Lenovo models had the same batteries so people can swap them around
as they wish. Is this too much to ask for? Have you seen another brand which
got this right? 

ThinkPad Mini Dock Design Flaw
------------------------------

Note: this section has previously been published
[here](http://otb.bg/blog/2012/06/14/thinkpad-mini-dock-design-flaw/).

I'm using a [ThinkPad Mini Dock Series 3](http://amzn.to/15tjUYi) docking station
with my X220 laptop. Being a QA engineer for so long I immediately
noticed something that wasn't quite right. The buttons on the left and the mechanism
next to them are blocking the hot air exhaust from the CPU fan. This model of docking
station is made to fit several models of laptops and those which dock in position 2 are
less affected from those which dock in possition 1. Mine was not a lucky one.

![docking station in position 2](/images/dock/alone.jpg "docking station in position 2")

On the pictures below it is clearly visible that most of the hot air coming out of the CPU
fan is blocked.

![top view](/images/dock/top.jpg "top view")
![back view](/images/dock/back.jpg "back view")
![side view](/images/dock/side.jpg "side view")


In order to reduce laptop heating and provide better cooling I decided to remove the
1/2 position switch mechanism. To do that you have to unscrew all screws from the docking
station and carefully split the top and bottom halves. The offending piece of plastic is
screwed with two tiny screws at the bottom. Once they are removed everything comes off.

![blocking part removed](/images/dock/removed.jpg "blocking part removed")

Even with this piece removed my laptop still hets up too much! I guess 80 C is just
normal for the Core i7 processors :(.


Have you found something not quite right in your hardware design? Please share in the
comments.
