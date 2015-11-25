---
layout: post
Title: Can I Use Android Phone as Smart Card Reader
date: 2013-12-18 23:09
comments: true
Tags: RHEL, Fedora, QA
---

Today I had troubles with my Omnikey CardMan 6121 smart card reader.
For some reason it will not detect the card inside and was unusable.
`/var/log/messages` was filled with  *Card Not Powered* messages:


    Dec 18 11:17:55 localhost pcscd: eventhandler.c:292:EHStatusHandlerThread() Error powering up card: -2146435050 0x80100016
    Dec 18 11:18:01 localhost pcscd: winscard.c:368:SCardConnect() Card Not Powered
    Dec 18 11:18:02 localhost pcscd: winscard.c:368:SCardConnect() Card Not Powered

<img src="/images/omnikey_cardman_6121.gif" style="float:right;margin-left:20px;" />

I've found the solution in 
[RHBZ #531998](https://bugzilla.redhat.com/show_bug.cgi?id=531998). 

{% blockquote Pierre Ossman https://bugzilla.redhat.com/show_bug.cgi?id=531998#c12 Comment #12 %}

I've found the problem, and it's purely mechanical.
Omnikey has simply screwed up when they designed this reader.
When the reader is inserted into the ExpressCard slot, it gets slightly
compressed. This is enough to trigger the mechanical switch that detects
insertions. If I jam something in there and force it apart, then pcscd
starts reporting that the slot is empty.
{% endblockquote %}

So I tried moving the smart card a millimeter back and forth inside the reader and
that fixed it for me.

This smart card is standard SIM size and I wonder if it is possible to use
[dual SIM](http://amzn.to/1dnl2gN) smart phones and [tablets](http://amzn.to/18XpWlp)
as a reader? I will be happy to work on the software side if there is an open source
project already (e.g. OpenSC + drivers for Android). If not, why not? 

If you happen to have information on the subject please share it in the comments.
Thanks!
