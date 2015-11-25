---
layout: post
Title: Quick Script for Khan Academy - Looking for Contributors
date: 2013-04-16 22:20
comments: true
Slug: quick-script-for-khan-academy
---

The Bulgarian translators team behind
[Khan Academy](https://www.khanacademy.org/) asked for help some time ago 
on a local mailing list. I promised to help but had nearly forgotten about that.
The guys are no developers, they simply wanted a script which will give them information
if a particular video has Bulgarian subtitles and the completion percentage.

They gave me a spread sheet file with a list of video URLs (3000 + of them).
Using Python's *BeautifulSoup* module I hacked a small script to produce the
desired output. 
Everything can be found at <https://github.com/atodorov/Khan-Academy-Find-Subtitles>.

The script is very fresh, just run it today against the given input and produced
some results. Lots of the URLs were skipped, around 500 entries produced results,
100 more failed. I have no idea what happened to the rest.

This is an ideal side project for students (I'm looking at you #HackFMI participants)
which will teach you something about screen scraping and extracting data from
the web. It will also boost your karma by helping a project which
lacks developers but is open source in nature.

If you have some Python skills and would like to help please ping me as I
may not have the time to maintain this project in the long term.
