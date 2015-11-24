---
layout: post
Title: Why VMware Multi-Hypervisor Manager Architecture Is Wrong
date: 2013-05-30 23:36
comments: true
categories: 
---

Today I've visited the annual 
[VMware Open House Event](http://www.openhouse.vmware-bulgaria.com/) in Sofia.
One of the sessions discussed their product 
[vCenter Multi-Hypervisor Manager](http://www.vmware.com/support/mhm/doc/vcenter-multi-hypervisor-manager-10-release-notes.html)
and the developers explained their architecture and technology behind it. 
I think they are wrong.

<img src="/images/vmware_mhm_architecture.png" alt="MHM Architecture" style="clear:both;display:block;"/>
Image taken from product release notes.

As shown above the purple-orange components are the MHM ones. They are designed as
plug-ins to the vCenter product and can not function as stand alone products.
vCenter MHM Server is responsible for communicating with 3rd party hypervisors
and then talks back to the MHM Extension in vCenter which feeds the MHM Plug-In (the UI).
I see three bad design decisions here: 

1) The plugin architecture makes both the management layer and the UI a separate module.
As was shown in a demo session the user can not manage/visualize ESX and Hyper-V hosts/VMs
at the same time. They are managed and visualized in separate views. 
This leads to non uniform user experience. Not to mention both UIs are different because the
supported hypervisor capabilities are different. -1 for user experience. 

2) From what I understand both vCenter and MHM Extension provide API access. MHM one is not public yet.
Customers are using this API to build their own scripts around the infrastructure. For a customer
this means duplicating effort and maintaining scripts that talk to two separate APIs, although they
will be very similar to one another. -1 for making it easy on the customer.

3) From development point of view the top two components are not necessary. They introduce
extra development and management costs to the product. -1 for product maintainability.

The Alternative
----------------

One could design the same product in the fashion that [libvirt](http://libvirt.org) does - 
abstract all hypervisor details and provide a common API to build applications against.
In this case vCenter Server will be the application on top.
This interface will also report hypervisor capabilities so that the UI will be disabled
where appropriate. 

<img src="/images/libvirt-driver-arch.png" alt="Libvirt Driver Architecture" style="clear:both;display:block;"/>
Image taken from <http://libvirt.org/api.html>

I think libvirt's approach is much cleaner and easier to maintain in the long term.

Indeed I've asked the question why not use libvirt - 
it already supports ESX and Hyper-V as well as bunch of other hypervisors. I didn't get a clear
answer on that, just that the team was looking at it, evaluated libvirt but opted to go
another way. 

I still feel VMware has not learned how to do the open source dance as well as others do.
What do you think? 
