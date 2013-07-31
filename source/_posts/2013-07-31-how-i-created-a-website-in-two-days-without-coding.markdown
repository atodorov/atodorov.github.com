---
layout: post
title: "How I Created a Website In Two Days Without Coding"
date: 2013-07-31 21:55
comments: true
categories: ['Amazon', 'S3']
---

![header image](/images/logos/obuvki41plus_header.png "header image")

This is a simple story about a website I helped create without using any
programming at all. It took me two days because of the images and the logo
design which I've commissioned to a friend.

The website is [obuvki41plus.com](http://obuvki41plus.com/) which is a
re-seller business my spouse runs. It specializes in large size, elegant
ladies shoes - Europe size 41 plus (hard to find in Bulgaria),
hence the name.

Required Functionality
----------------------

* Display a catalog of items for sale with detailed information about
each item;
* Make it possible for people to comment and share the items;
* Very basic shopping cart which stores the selected items and then
redirects to a page with order instructions. Actual order is made via
phone for several reasons which I will explain in another post;
* Add a feedback/contact form;
* Look nice on mobile devices.


Technology
----------

* The website is static, all pages are simple HTML and is hosted in
Amazon S3;
* Comments are provided by Facebook's
[Comments Box](https://developers.facebook.com/docs/reference/plugins/comments/)
plug-in;
* Social media buttons and tracking are provided by
[AddThis](https://www.addthis.com/);
* Visitors analytics is standard and is from
[Google Analytics](http://www.google.com/analytics/);
* Template is from [GitHub Pages](http://pages.github.com/) with slight
modifications; Works on mobile too;
* Logo is custom designed by my friend
[Polina Valerieva](https://www.facebook.com/aluinpoli);
* Feedback/contact form is by [UserVoice](https://www.uservoice.com/);
* Shopping cart is by [simpleCart(js)](http://simplecartjs.org/).
I've created a simple animation effect when pressing the "ADD TO CART"
link to visually alert the user. This is done with jQuery.

I could have used some JavaScript templating engine like
[Handlebars](http://handlebarsjs.com/) but at the time I didn't know about
it and I prefer not to write JavaScript if possible :).


Colophon
---------

I did some coding after the initial release eventually. 
I've transformed the website to a Django
based site which is exported as static HTML. 

This helps me with faster deployment/management as everything is stored
in git, allows templates inheritance and also makes the site ready to
add more functionality if required.

