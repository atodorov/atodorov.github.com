---
layout: post
Title: HackFMI Code Stats
date: 2013-04-19 10:00
comments: true
Tags: hackfmi
---

It's Friday - five days after the first [HackFMI](http://hackfmi.com)
event was held. I have some interesting statistics derived from the
source code of all projects. Read on!

!["HackFMI stats"](/images/hackfmi/hackfmi2013_cocomo.png "HackFMI stats")

How The Stats Were Calculated
-----------------------------

I've used [Ohloh](http://ohloh.net) to analyze the source code of all projects.
A simple Ohloh project called [HackFMI 2013](https://www.ohloh.net/p/hackfmi2013)
enlists and tracks [18](https://www.ohloh.net/p/hackfmi2013/enlistments)
different repositories as if they were one big project.
Not all teams had repositories and some didn't sent information back to me although
I asked them. Two projects sent me tarballs with their code, which I've pushed to GitHub
for the purpose of tracking stats.


Be aware however that Ohloh is known to produce inaccurate statistics for projects
with lots of code and short development history. Furthermore its
[COCOMO](https://www.ohloh.net/p/hackfmi2013/estimated_cost) calculations
are wrong as well due to duplicate code,
not written during the hackathon such as jQuery or PHP libraries.


The Stats
---------

During the weekend sprint **759,453 lines of code** were written by
**56 contributors** spread across **768 commits**.

!["HackFMI top contributors"](/images/hackfmi/hackfmi2013_top_contributors.png "HackFMI top contributors")

From the top 10 contributors 5 had Python as their primary language.
Which is to say Python developers have good development practices with Git.

None of the contributors (excluding myself) were recognized by Ohloh,
meaning either they have not contributed to any other open source project
or their contributors were not under their name or
they've used a different name/email combination. Whatever the case go
claim your contributions and track your kudos rank across the open source community. 


**19 different** programming languages 
[were used](https://www.ohloh.net/p/hackfmi2013/analyses/latest/languages_summary#dingus-row).

!["HackFMI top languages"](/images/hackfmi/hackfmi2013_languages.png "HackFMI top languages")

The most popular ones are XML, JavaScript, HTML, PHP, CSS and ActionScript. This is nearly 97%
of the source code. All the rest languages have been used under 1% per language.
The languages used are pretty standard and expected.

Estimated Cost
--------------

The [estimated development cost](https://www.ohloh.net/p/hackfmi2013/estimated_cost)
is 205 person-years valued at $ 11,251,680. This is too high because of all duplicated
libraries and extra files tracked.

Ohloh allows files and directories to be excluded on per-repository basis.
I'd appreciate your help if you preview the projects and create the exclusion rules. Thanks!

The stats and repositories are public. If you manage to extract other interesting details
don't hesitate to share them in the comments.
