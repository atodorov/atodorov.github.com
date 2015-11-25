---
layout: post
Title: Tip: Generating Directory Listings with wget
date: 2013-02-21 12:12
comments: true
Tags: tips
---

Today I was looking to generate a list of all files under remote site directory,
including sub directories. I found no built-in options for this in
[wget](https://www.gnu.org/software/wget/). This is how I did it:

    wget http://example.com/dir/ --spider -r -np 2>&1 | grep http:// | tr -s ' ' | cut -f3 -d' '

I managed to retrieve 12212 entries from the URL I was exploring.
