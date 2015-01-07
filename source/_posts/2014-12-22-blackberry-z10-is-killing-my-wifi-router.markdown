---
layout: post
title: "BlackBerry Z10 is Killing My WiFi Router"
date: 2014-12-22 15:46
comments: true
categories: ['BlackBerry', 'QA', 'bugs']
---

Few days ago I've resurrected my BlackBerry Z10 only to find out that it kills
my WiFi router shortly after connecting to the network.
It looks like many people are having the same problem with BlackBerry but most forum
threads don't offer a meaningful solution so I did some tests. 

Everything works fine when WiFi mode is set to either 11bgn mixed or 11n only and
WiFi security is disabled.

When using WPA2/Personal security mode and AES encryption the problem occurs
regardless of which WiFi mode is used. There is another type of encryption called TKIP
but the device itself warns that this is not supported by the 802.11n specification
(all my devices use it anyway).

So to recap:
**BlackBerry Z10 causes my TP-Link router to die if using WPA2/Personal security with
AES Encryption. Switching to open network with MAC address filtering works fine!**

I haven't had the time to upgrade the firmware of this router and see if the problem persists.
Most likely I'll just go ahead and flash it with OpenWRT.
