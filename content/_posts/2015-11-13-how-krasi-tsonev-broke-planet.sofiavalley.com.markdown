---
layout: post
Title: How Krasi Tsonev Broke Planet.SofiaValley.com
date: 2015-11-13 10:09
comments: true
Tags: QA, fedora.planet
---

Yesterday I've added [Krasimir Tsonev's blog](http://krasimirtsonev.com/blog/) to
<http://planet.sofiavalley.com> and the planet broke. Suddenly it started showing
only Krasi's articles and all of them with the same date. The problem was the RSS
feed didn't have any timestamps. The fix is trivial:

{% codeblock lang:diff %}
--- rss.xml.orig	2015-11-13 10:12:35.348625718 +0200
+++ rss.xml	2015-11-13 10:12:45.157932304 +0200
@@ -9,120 +9,160 @@
                             <title><![CDATA[A modern React starter pack based on webpack]]></title>
                             <link>http://krasimirtsonev.com/blog/article/a-modern-react-starter-pack-based-on-webpack</link>
                             <description><![CDATA[<p><i>Checkout React webpack starter in <a href=\"https://github.com/krasimir/react-web<br /><p>You know how crazy is the JavaScript world nowadays. There are new frameworks, libraries and tools coming every day. Frequently I’m exploring some of these goodies. I got a week long holiday. I promised to myself that I’ll not code, read or watch about code. Well, it’s stronger than me. <a href=\"https://github.com/krasimir/react-webpack-starter\">React werbpack starter</a> is the result of my no-programming week.</p>]]></description>
+                            <pubDate>Thu, 01 Oct 2015 00:00:00 +0300</pubDate>
+                            <guid>http://krasimirtsonev.com/blog/article/a-modern-react-starter-pack-based-on-webpack</guid>
                         </item>
{% endcodeblock %}

Thanks to Krasi for fixing this quickly and happy reading!
