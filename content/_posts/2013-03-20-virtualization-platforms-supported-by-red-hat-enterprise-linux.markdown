---
layout: post
title: "Virtualization Platforms Supported by Red Hat Enterprise Linux"
date: 2013-03-20 15:04
comments: true
categories: ['RHEL', 'virtualization', 'tips']
---

This is mostly for my own reference, to have a handy list
of supported virtualization platforms by Red Hat Enterprise Linux.

Software virtualization solutions
---------------------------------

A guest RHEL operating system is supported if it runs on the following
platforms:

* Xen shipped with RHEL Server
* KVM shipped with RHEL Server or RHEV for Servers
* [VMware](https://hardware.redhat.com/VMware) ESX/vSphere
* [Microsoft Hyper-V](https://hardware.redhat.com/Microsoft)

Red Hat does not support Citrix XenServer. However, customers can
[buy RHEL Server](http://otb.bg) and use it with Citrix XenServer
with the understanding that Red Hat will only support technical
issues that can be reproduced on bare metal.

The 
[official virtualization support matrix](http://www.redhat.com/resourcelibrary/articles/enterprise-linux-virtualization-support)
shows which host/guest operating systems combinations are supported.

Hardware partitioning
---------------------

Red Hat supports RHEL on hardware partitioning and virtualization solutions such as:

* [IBM System Z](https://hardware.redhat.com/list.cgi?product=Red+Hat+Hardware+Certification&quicksearch=IBM+System+Z)
* [IBM Power](https://hardware.redhat.com/list.cgi?product=Red+Hat+Hardware+Certification&quicksearch=IBM+POWER)
* [Fujitsu PRIMEQUEST](https://hardware.redhat.com/list.cgi?product=Red+Hat+Hardware+Certification&quicksearch=PRIMEQUEST)
* [Hitachi Virtage](https://hardware.redhat.com/list.cgi?product=Red+Hat+Hardware+Certification&quicksearch=Virtage)

Unfortunately the [recently updated](https://access.redhat.com/knowledge/articles/263573)
hardware catalog
[doesn't allow to filter by hardware partitioning vs. virtualization platform](https://bugzilla.redhat.com/show_bug.cgi?id=923802)
so you need to know what you are looking for to find it :(.


Red Hat Enterprise Linux as a guest on the Cloud
------------------------------------------------

Multiple public cloud providers are supported. Comprehensive list can be found here:
http://www.redhat.com/solutions/cloud-computing/public-cloud/find-partner/

You can also try [Red Hat Partner Locator's](http://redhat.force.com/finder/)
advanced search. However at the time of this writing there are no partners
listed in the Cloud / Virtualization category.

**Warning:** It is known that Amazon uses Xen with custom
modifications (not sure what version) and HP Cloud uses KVM but there
is not much public record about hypervisor technology used by most cloud providers.
Red Hat has partner agreements with these vendors and will commercially support 
only their platforms. This means that if you decide to use upstream Xen or anything
else not listed above, you are on your own. **You have been warned!**


Unsupported but works
---------------------

I'm not a big fan of running on top of unsupported environments
and I don't have the need to do so.
I've heard about people running CentOS (RHEL compatible) on VirtualBox
but I have no idea how well it works.

If you are using a different virtualization platform
(like LXC, OpenVZ, UML, 
<a target="_blank" href="http://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-brandtextbin=Parallels%20Software&linkCode=ur2&node=229534&tag=atodorovorg-20">Parallels</a><img src="https://www.assoc-amazon.com/e/ir?t=atodorovorg-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
or other) let me know if CentOS/Fedora works on it.
Alternatively I can give it a try if you can provide me with ssh/VNC access to the machine.
