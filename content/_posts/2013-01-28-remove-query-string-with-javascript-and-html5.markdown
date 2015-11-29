---
layout: post
Title: Remove Query String with JavaScript and HTML5
date: 2013-01-28 15:52
comments: true
Tags: JavaScript, HTML5
---

A [query string](http://en.wikipedia.org/wiki/Query_string) is the stuff after
the question mark in URLs.

!["URL with query string"](/images/url_w_qs.png)

Why remove query strings?
-------------------------

Two reasons: clean URLs and social media.

Clean URLs not only look better but they prevent users to see if you are tracking
where they came from. The picture above shows what the address bar
looks like after the user clicks a link in Feedburner. The high-lightened part is
what Google Analytics uses to distinguish Feedburner traffic from other types of
traffic. I don't want my users to see this.


As you know, social media sites give URLs a score, whether it is based on number of
bookmarks, reviews, comments, likes or whatever. Higher scores usually result in
increased traffic to your site. Query strings mess things up because <http://www.dif.io>
and <http://www.dif.io/?query> are usually considered two different URLs. So instead
of having a high number of likes for your page you get several scores and never
make it to the headlines.


JavaScript and HTML5 to the rescue
----------------------------------

Place this JavaScript code in the `<head>` section of your pages. Preferably near the top.

    :::html
    <script type="text/javascript">
    var uri = window.location.toString();
    if (uri.indexOf("?") > 0) {
        var clean_uri = uri.substring(0, uri.indexOf("?"));
        window.history.replaceState({}, document.title, clean_uri);
    }
    </script>

This code will clean the URL in the browser address bar without reloading the page.
It works for HTML5 enabled browsers.

This works for me with 
Firefox 10.0.12, Opera 12.02.1578 and Chrome 24.0.1312.56 under Linux.
<strike>In fact I'm using this snippet on this very own blog as well.</strike>
**UPDATE:** I've
[migrated to Pelican](/blog/2015/11/25/blog-migration-from-octopress-to-pelican/)
and haven't enabled this script on the blog!


**Updated on 2013-01-30**

Here is another approach proposed by reader Kamen Mazdrashki: 

    :::html
    <script type="text/javascript">
    var clean_uri = location.protocol + "//" + location.host + location.pathname;
    /*
    var hash_pos = location.href.indexOf("#");
    if (hash_pos > 0) {
        var hash = location.href.substring(hash_pos, location.href.length);
        clean_uri += hash;
    }
    */
    window.history.replaceState({}, document.title, clean_uri);
    </script>

If you'd like to keep the hash tag aka named anchor aka fragment identifier at the end of the URL
then uncomment the commented section.

I've tested removing the hashtag from the URL. Firefox doesn't seem to scroll the page
to where I wanted but your experience may vary. I didn't try hard enough to
verify the results.

One question still remains though: Why would someone point the users to an URL which contains
named anchors and then remove them? I don't see a valid use case for this scenario.

You may want to take a look at the many
<a target="_blank" href="http://www.amazon.com/s/ref=as_li_ss_tl?_encoding=UTF8&camp=1789&creative=390957&field-keywords=HTML5%20and%20JavaScript&linkCode=ur2&rh=i%3Aaps%2Ck%3AHTML5%20and%20JavaScript&tag=atodorovorg-20&url=search-alias%3Daps&linkId=5JHZNZC3Q5R3RB3L">HTML5 and JavaScript books</a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=ur2&o=1" width="1" height="1" border="0" style="border:none !important; margin:0px !important;" />
if you don't have enough experience with the subject. For those of you who
are looking into Node.js I can recommend two book by my friend Krasi Tsonev:
<a rel="nofollow" href="http://www.amazon.com/gp/product/1783287330/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1783287330&linkCode=as2&tag=atodorovorg-20&linkId=ZBA3EYC4PZGKASAF">Node.js Blueprints - Practical Projects to Help You Unlock the Full Potential of Node.js</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=1783287330" width="1" height="1" border="0" style="border:none !important; margin:0px !important;" />
and
<a rel="nofollow" href="http://www.amazon.com/gp/product/B00XJRN9S6/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00XJRN9S6&linkCode=as2&tag=atodorovorg-20&linkId=OLBCPLXOAILZTJR5">Node.js By Example</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B00XJRN9S6" width="1" height="1" border="0" style="border:none !important; margin:0px !important;" />
.