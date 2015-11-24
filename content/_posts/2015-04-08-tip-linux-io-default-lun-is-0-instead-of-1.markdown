---
layout: post
title: "Tip: Linux-IO default LUN is 0 instead of 1"
date: 2015-04-08 15:09
comments: true
categories: ['RHEL', 'Fedora', 'tips']
---

I've been testing iBFT in KVM which worked quite well with a RHEL 6 iSCSI target
and failed miserably when I switched to RHEL 7 iSCSI target.

{% codeblock %}
iPXE> dhcp net0
DHCP (net0 52:54:00:12:34:56)... ok
iPXE> set keep-san 1
iPXE> sanboot iscsi:10.0.0.1:::1:iqn.2015-05.com.example:target1
Could not open SAN device: Input/output error (http://ipxe.org/1d704539)
iPXE>
{% endcodeblock %}

The [error page](http://ipxe.org/err/1d7045) says
{% blockquote %}
Note that the default configuration when Linux is the target is for the disk to be LUN 1.
{% endblockquote %}

Well this is not true for Linux-IO (targetcli). **The default LUN is 0!**

{% codeblock %}
iPXE> sanboot iscsi:10.0.0.1:::0:iqn.2015-05.com.example:target1
Registered SAN device 0x80
Booting from SAN device 0x80
{% endcodeblock %}

Kudos to Bruno Goncalves from Red Hat in helping me debug this issue!
