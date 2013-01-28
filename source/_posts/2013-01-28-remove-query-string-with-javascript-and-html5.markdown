---
layout: post
title: "Remove Query String with JavaScript and HTML5"
date: 2013-01-28 15:52
comments: true
categories: ['JavaScript', 'HTML5']
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

    <script type="text/javascript">
    // (c) 2013 - Alexander Todorov, http://atodorov.org
    // Published under GNU GPLv3
    var uri = window.location.toString();
    var clean_uri = uri.substring(0, uri.indexOf("?"));
    window.history.replaceState({}, document.title, clean_uri);
    </script>


This code will clean the URL in the browser address bar without reloading the page.
It works for HTML5 enabled browsers. This totally works for me with 
Firefox 10.0.12, Opera 12.02.1578 and Chrome 24.0.1312.56 under Linux.

