---
layout: post
Title: Thunderbolt to Ethernet Adapter on Linux
date: 2015-05-04 22:27
comments: true
Tags: 'RHEL', 'Mac', 'fedora.planet'
---

As it seems my
<a href="http://www.amazon.com/gp/product/B008ALA6DW/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B008ALA6DW&linkCode=as2&tag=atodorovorg-20&linkId=T2J6D7GIDMKNWLYV">Thunderbolt to gigabit Ethernet adapter</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B008ALA6DW" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
works with 
[RHEL 7 on a MacBook Air](/blog/2015/04/26/installing-red-hat-enterprise-linux-7-on-macbook-air-2015/)
despite some reports it may not.

After plugging the device is automatically recognized and the *tg3* driver is loaded.
Detailed *lspci* below:

    0a:00.0 Ethernet controller: Broadcom Corporation NetXtreme BCM57762 Gigabit Ethernet PCIe
        Subsystem: Apple Inc. Device 00f6
        Physical Slot: 9
        Flags: bus master, fast devsel, latency 0, IRQ 19
        Memory at cd800000 (64-bit, prefetchable) [size=64K]
        Memory at cd810000 (64-bit, prefetchable) [size=64K]
        [virtual] Expansion ROM at cd820000 [disabled] [size=64K]
        Capabilities: [48] Power Management version 3
        Capabilities: [50] Vital Product Data
        Capabilities: [58] MSI: Enable- Count=1/8 Maskable- 64bit+
        Capabilities: [a0] MSI-X: Enable+ Count=6 Masked-
        Capabilities: [ac] Express Endpoint, MSI 00
        Capabilities: [100] Advanced Error Reporting
        Capabilities: [13c] Device Serial Number 00-00-ac-87-a3-25-20-33
        Capabilities: [150] Power Budgeting <?>
        Capabilities: [160] Virtual Channel
        Capabilities: [1b0] Latency Tolerance Reporting
        Kernel driver in use: tg3

Unplugging and pluggin back in the network cable works as expected.
I did see my computer freeze 2 out of 10 times when I've unplugged the Thunderbolt
adapter but couldn't reproduce it repliably or grab more info. 

For the record this is with kernel 3.10.0-229.1.2.el7.x86_64 which is missing
this
[upstream commit](https://git.kernel.org/cgit/linux/kernel/git/gregkh/char-misc.git/commit/?h=char-misc-next&id=16603153666d22df544ae9f9b3764fd18da28eeb).
I'm not sure why it works though.

If I remember correctly *tg3* is available during installation so you should
be able to use the Thunderbolt adapter instead of WiFi as well.
