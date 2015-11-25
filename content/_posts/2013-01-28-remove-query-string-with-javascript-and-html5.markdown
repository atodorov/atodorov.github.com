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

{% codeblock lang:html %}
<script type="text/javascript">
var uri = window.location.toString();
if (uri.indexOf("?") > 0) {
    var clean_uri = uri.substring(0, uri.indexOf("?"));
    window.history.replaceState({}, document.title, clean_uri);
}
</script>
{% endcodeblock %}

This code will clean the URL in the browser address bar without reloading the page.
It works for HTML5 enabled browsers.

This works for me with 
Firefox 10.0.12, Opera 12.02.1578 and Chrome 24.0.1312.56 under Linux. In fact I'm
using this snippet on this very own blog as well.


**Updated on 2013-01-30**

Here is another approach proposed by reader Kamen Mazdrashki: 

{% codeblock lang:html %}
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
{% endcodeblock %}

If you'd like to keep the hash tag aka named anchor aka fragment identifier at the end of the URL
then uncomment the commented section.

I've tested removing the hashtag from the URL. Firefox doesn't seem to scroll the page
to where I wanted but your experience may vary. I didn't try hard enough to
verify the results.

One question still remains though: Why would someone point the users to an URL which contains
named anchors and then remove them? I don't see a valid use case for this scenario. Do you?



