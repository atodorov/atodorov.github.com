---
layout: post
title: "git History Stats and Project Cost Estimation"
date: 2013-07-18 23:40
comments: true
categories: 
---

How do you generate useful stats from a git repo? In particular how do you
calculate the monetary cost of development effort behind that git repo? 
I've found the [gitstats](https://github.com/hoxu/gitstats) project which
helped me answer the above question. 

Git clone the repo and make sure you
have Python and Gnuplot installed. `gitstat` will generate html files and
graphics from your git history. 

In my case I only needed to know how long it took for a project to be developed.
It turned out that around 56% of the days since day one were active and there were
an average of 8,5 commits per active day in the repo.

I took the number of active days and multiplied by an average daily
wage to come up with a real number. This is what I consider to be the cost to
develop the software from scratch. This is overly simplified, but serves my 
needs to establish some base line.

There's the [COCOMO](https://en.wikipedia.org/wiki/COCOMO) method which is probably
more accurate but I didn't find any usable online COCOMO calculator.
