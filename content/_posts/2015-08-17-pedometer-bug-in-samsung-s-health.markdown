---
layout: post
Title: Pedometer Bug in Samsung S Health
date: 2015-08-17 16:43
comments: true
categories: ['QA', 'Samsung']
---

Do you remember the 
[pedometer bug in Samsung Gear Fit](/blog/2015/01/09/pedometer-bug-in-samsung-gear-fit-smartwatch/)
I've discovered earlier ? It turns out that Samsung is a fan of this one
and has the exact same bug in their *S Health* application.

The application doesn't block pedometer(e.g. steps counting) while
performing other activities such as cycling for example. So in reallity it
reports incorrect value for burned callories. At this time I call it
bad software development practice/architecture on Samsung's part which leads
to this bug being present.

Btw for more interesting bugs see
[Samsung Gear Fit Bug-of-the-Day](http://gearfitbugs.tumblr.com/).
