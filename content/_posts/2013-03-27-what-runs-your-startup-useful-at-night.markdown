---
layout: post
Title: What Runs Your Start-up - Useful at Night
date: 2013-03-27 12:00
comments: true
Tags: start-up, what runs, Node.js, HTML5, CouchDB, Redis, MongoDB, Amazon, S3, Heroku, iOS, Android
Slug: what-runs-your-startup-useful-at-night
---

<img style="float: left; margin-right: 10px;" src="/images/startup/usefulatnight.png" alt="Useful at Night logo" />

[Useful at Night](http://usefulatnight.com/) is a mobile guide for nightlife
empowering real time discovery of cool locations, allowing nightlife players
to identify opinion leaders. Through geo-location and data aggregation
capabilities, the application allows useful exploration of cities, places and
parties.

[Evelin Velev](http://about.me/velev) was kind enough to share what technologies
his team uses to run their star-up.

<br/>

Main Technologies
----------------

Main technologies used are Node.js, HTML 5 and NoSQL.


Back-end application servers are written in Node.js and hosted at Heroku,
coupled with [RedisToGo](http://www.redistogo.com/) for caching and
CouchDB served by [Cloudant](https://cloudant.com/) for storage.

Their mobile front-end supports both iOS and Android platforms and is built using
HTML5 and a homemade UI framework called RAPID. There are some native parts developed
in Objective-C and Java respectively.

In addition *Useful at Night* uses MongoDB for metrics data with a custom metrics solution
written in Node.js; Amazon S3 for storing different assets; and a custom storage solution
called Divan (simple CouchDB like).

Why Not Something Else?
-----------------------

> We chose Node.js for our application servers, because it enables us to build efficient
> distributed systems while sharing significant amounts of code between client and server.
> Things get really interesting when you couple Node.js with Redis for data structure
> sharing and message passing, as the two technologies play very well together.
> 
> We chose CouchDB as our main back-end because it is the most schema-less data-store that
> supports secondary indexing. Once you get fluent with its map-reduce views, you can
> compute an index out of practically anything. For comparison, even MongoDB requires
> that you design your documents as to enable certain indexing patterns. Put otherwise,
> we'd say CouchDB is a data-store that enables truly lean engineering - we have never had
> to re-bake or migrate our data since day one, while we're constantly experimenting with
> new ways to index, aggregate and query it.
> 
> We chose HTML5 as our front-end technology, because it's cross-platform and because we
> believe it's ... almost ready. Things are still really problematic on Android, but iOS
> boasts a gorgeous web presentation platform, and Windows 8 is also joining the game with
> a very good web engine. Obviously we're constantly running into issues and limitations,
> mostly related to the unfortunate fact that in spite of some recent developments,
> a web app is still mostly single threaded. However, we're getting there, and we're proud
> to say we're running a pretty graphically complex hybrid app with near-native GUI performance
> on the iPhone 4S and above.


Want More Info?
---------------

If you'd like to hear more from *Useful at Night* please comment below. I will ask them
to follow this thread and reply to your questions.

