---
layout: post
Title: Spoiler: How to Open Source Existing Proprietary Code in 10 Steps
date: 2014-04-23 22:47
comments: true
Tags: 'Fedora', 'Django'
---

We've heard about companies opening up their proprietary software products,
this is hardly news nowadays. But have you wondered what it is like to migrate
production software from closed to open source? I would like to share my own
experience about going open source as seen from behind the keyboard.

[Difio](http://www.dif.io) was recently open sourced and the steps to go through
were:

* Simplify - remove everything that can be deleted
* Create self contained modules aka re-organize the file structure
* Separate internal from external modules
* Refactor the existing code
* Select license and update copyright
* Update 3rd party dependencies to latest versions and add requirements.txt
* Add README and verbose settings example
* Split difio/ into its own git repository
* Test stand alone deployments on fresh environment
* Announce


Do you want to know more? Use the comments and tell me what exactly!
I'm writing a longer version of this article so stay tuned!

