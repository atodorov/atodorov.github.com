Title: Introducing pylint-django 0.8.0
date: 2018-01-22 17:00
comments: true
Tags: fedora.planet, QA, Python, Django
og_image: images/validation.jpg
twitter_image: images/validation.jpg

Since my previous post was about
[writing pylint plugins]({filename}2018-01-05-writing-pylint-checkers.markdown)
I figured I'd let you know that I've released
[pylint-django](https://github.com/landscapeio/pylint-django) version 0.8.0
over the weekend. This release merges all pull requests which were
pending till now so make sure to read the change log.

Starting with this release Colin Howe and myself are the new
maintainers of this package. My immediate goal is to triage all of the
open issue and figure out if they still reproduce. If yes try to
come up with fixes for them or at least get the conversation going again.

My next goal is to integrate pylint-django with
[Kiwi TCMS](http://kiwitcms.org) and start resolving all the 4000+
errors and warnings that it produces.

You are welcome to contribute of course. I'm also interested in hosting a
workshop on the topic of pylint plugins.



Thanks for reading and happy testing!
