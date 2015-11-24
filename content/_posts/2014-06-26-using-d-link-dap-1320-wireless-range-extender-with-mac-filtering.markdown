---
layout: post
title: "Using D-Link DAP-1320 Wireless Range Extender with MAC Filtering"
date: 2014-06-26 10:10
comments: true
categories: 
---

<iframe style="width:120px;height:240px;float:left;display:inline-block;margin-right:10px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-na.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=US&source=ss&ref=ss_til&ad_type=product_link&tracking_id=atodorovorg-20&marketplace=amazon&region=US&placement=B00B0RQSD0&asins=B00B0RQSD0&linkId=R2B5GSDVQ7GHLAXK&show_border=true&link_opens_in_new_window=true">
</iframe>

Recently I've purchased a
<a href="http://www.amazon.com/gp/product/B00B0RQSD0/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00B0RQSD0&linkCode=as2&tag=atodorovorg-20&linkId=ELZCDTH62GGNKJTL">wireless range extender</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B00B0RQSD0" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
as the one shown here. It had troubles connecting to the upstream Wi-Fi router
because it used MAC filtering instead of password security. Luckily there was
a [forum thread](http://forums.dlink.com/index.php?topic=56386.0) which helped
me figure it out.

DAP 1320 uses two MAC addresses
-------------------------------

Everything was working just fine with MAC filtering disabled on the upstream
router but failed miserably when enabled. I thought the MAC address provided
on the DAP 1320 packaging was wrong. 

It turned out the device had 2 addresses.
The one on the packaging is *70:62:B8:07:0B:76* and it didn't matter if that
is enabled or disabled in the router settings. The second MAC is used when
trying to forward connections through the router. Both addresses differ by the
second symbol with a difference of 2. So I've enabled *72:62:B8:07:0B:76*
in the router settings and everything worked like a charm.

Other findings
--------------

Unfortunately if a device is connected to the wifi extender's network it will
bypass the MAC filtering employed on the upstream wifi router. As much as I dislike
using passwords for Wi-Fi I had to configure one for the extended network.

I've also found that when you save the configuration file from the device on your
hard drive it comes in a base64-encoded-line-by-line format. Pretty awkward.

Another pleasant (but not entirely surprising) finding was that D-Link included
a written acknowledgment of using open source components and an offer to provide
source code upon request.

