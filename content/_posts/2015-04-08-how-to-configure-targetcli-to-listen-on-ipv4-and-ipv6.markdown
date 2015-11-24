---
layout: post
title: "How to Configure targetcli to Listen on IPv4 and IPv6"
date: 2015-04-08 11:46
comments: true
categories: ['RHEL', 'Fedora']
---

In order to configure *targetcli* to listen on both IPv4 and IPv6 one has to
delete the default IPv4 portal configuration and replace it with IPv6 instead.

{% codeblock %}
# targetcli 
/>
/> cd iscsi/iqn.2015-04.com.example:target1/tpg1/portals
/iscsi/iqn.20.../tpg1/portals> ls
o- portals ............................................................................................................ [Portals: 1]
  o- 0.0.0.0:3260 ............................................................................................................. [OK]
/iscsi/iqn.20.../tpg1/portals> delete 0.0.0.0 3260
Deleted network portal 0.0.0.0:3260
/iscsi/iqn.20.../tpg1/portals> create ::0
Using default IP port 3260
Created network portal ::0:3260.
/iscsi/iqn.20.../tpg1/portals> ls
o- portals ............................................................................................................ [Portals: 1]
  o- [::0]:3260 ............................................................................................................... [OK]
/iscsi/iqn.20.../tpg1/portals> exit

# netstat -antp | grep 3260
tcp6       0      0 :::3260                 :::*                    LISTEN 
{% endcodeblock %}

It appears the target is listening only on IPv6 but in fact it will
also accept connections over IPv4. I've tried it. 

This is a bit counter intuitive, however if you try adding the IPv6 address
without removing the default IPv4 one *targetcli* will throw an error:

{% codeblock %}
/iscsi/iqn.20.../tpg1/portals> create ::0
Using default IP port 3260
Could not create NetworkPortal in configFS.
/>
{% endcodeblock %}

For more information about *targetcli* usage see my previous post
[How to Configure iSCSI Target on Red Hat Enterprise Linux 7](/blog/2015/04/07/how-to-configure-iscsi-target-on-red-hat-enterprise-linux-7/).
