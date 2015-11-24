---
layout: post
Title: Fixing Display Brightness on MacBook Air with RHEL 7
date: 2015-04-29 12:14
comments: true
categories: ['fedora.planet', 'Mac', 'RHEL']
---

One issue with RHEL/CentOS/Fedora on MacBook Air laptops is brightness control
and backlight behavior after suspend/resume. I've found the solution 
[here](http://mattoncloud.org/2014/02/05/fedora-20-on-a-macbook-air/)
and only tweaked it slightly for my use case.

mba6x_bl doesn't load automatically
-----------------------------------

The reason being the driver matches older hardware:

    $ modinfo mba6x_bl
    filename:       /lib/modules/3.10.0-229.1.2.el7.x86_64/extra/mba6x_bl/mba6x_bl.ko
    alias:          dmi:*:pnMacBookAir6*
    license:        GPL
    description:    MacBook Air 6,1 and 6,2 backlight driver
    author:         Patrik Jakobsson <patrik.r.jakobsson@gmail.com>
    rhelversion:    7.1
    srcversion:     4D069C8EB0E470AF27E7F8D
    depends:        video
    vermagic:       3.10.0-229.1.2.el7.x86_64 SMP mod_unload modversions 

My system is **MacBookAir7,2** and doesn't match the module alias. So a 
[quick fix](https://github.com/patjak/mba6x_bl/pull/25) was needed.
For more info about `MODULE_ALIAS` see
[ArchWiki](https://wiki.archlinux.org/index.php/Modalias).
Alternatively on Red Hat based systems you can place a config file
under `/etc/sysconfig/modules`, see 
[the docs](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/sec-Persistent_Module_Loading.html)
for more details.


intel_backlight driver is in the way
------------------------------------

On older systems mba6x_bl doesn't get used automatically. The problem is the offending
intel_backlight driver which gets used instead. To workaround it add this xorg.conf snippet:

    $ cat /etc/X11/xorg.conf.d/98-mba_bl.conf
    Section "Device"
        Identifier      "Intel Graphics"
        Driver          "intel"
        Option          "Backlight"     "mba6x_backlight"
    EndSection


For more info see [RHBZ 989555](https://bugzilla.redhat.com/show_bug.cgi?id=989555#c19).


Everything in one go
--------------------

If you are using RHEL 7 or CentOS 7 (version 7.1 required) instead of Fedora you can take
a look at my [Macbook Air RHEL 7 repository](/blog/2015/04/29/rhel-7-repository-for-macbook-air/).
