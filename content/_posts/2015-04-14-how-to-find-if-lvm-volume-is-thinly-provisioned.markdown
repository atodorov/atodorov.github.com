---
layout: post
Title: How to Find if LVM Volume is Thinly Provisioned
date: 2015-04-14 15:40
comments: true
Tags: RHEL, Fedora
---

The latest versions of Red Hat Enterprise Linux, CentOS and Fedora all
support LVM thin provisioning. Here's how to tell if a logical volume
has been thinly provisioned or not.

Using `lvs` to display volume information look under the *Attr* column.
Attribute values have the following meaning:

{% blockquote %}
The lv_attr bits are:

1  Volume type: (C)ache, (m)irrored, (M)irrored without initial sync, (o)rigin,
(O)rigin  with  merging  snapshot, (r)aid,  (R)aid  without  initial  sync,
(s)napshot,  merging  (S)napshot, (p)vmove, (v)irtual, mirror or raid (i)mage,
mirror or raid (I)mage out-of-sync, mirror (l)og device, under  (c)onversion,
thin  (V)olume,  (t)hin pool, (T)hin pool data, raid or pool m(e)tadata or
pool metadata spare.
{% endblockquote %}

This is how `lvs` looks like when you have a regular LVM setup:

{% codeblock %}
# lvs
  LV   VG              Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  root rhel_dhcp70-183 -wi-ao---- 17,47g                                                    
  swap rhel_dhcp70-183 -wi-ao----  2,00g    
{% endcodeblock %}

When using LVM thin provisioning you're looking for the left-most attribute bit
to be V, t or T. Here's an example:

{% codeblock %}
# lvs
  LV     VG              Attr       LSize  Pool   Origin Data%  Meta%  Move Log Cpy%Sync Convert
  pool00 rhel_dhcp71-101 twi-aotz-- 14,55g               7,52   3,86                            
  root   rhel_dhcp71-101 Vwi-aotz-- 14,54g pool00        7,53                                   
  swap   rhel_dhcp71-101 -wi-ao----  2,00g   
{% endcodeblock %}
