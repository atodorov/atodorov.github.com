---
layout: post
title: "HackFMI Post-mortem"
date: 2013-04-15 10:27
comments: true
categories: ['hackaton', 'hackfmi']
---

<img src="/images/hackfmi/hackfmi_beer.jpg" alt="HackFMI" style="float:left;margin-right:10px;" />

The first [HackFMI](http://hackfmi.com) event is now over :(. It was HUGE!
Kudos to the organizers, sponsors, mentors and all teams who took part and worked hard during
the weekend.

More than 100 people participated. There were 22 different teams presenting at the
finale yesterday evening. That in my opinion counts as a BIG success. I was surprised
to see so many people, lots of them first and second year at the university. There were
a good number of female hackers too, which I also didn't expect.
*DISCLAIMER: I've graduated a different university where the culture and male/female ratio
was different so my expectations were biased.*

People had interesting ideas and were passionate about them. They set off hacking
on a big scale. At times they wanted to create too big of an application and had to
cut off some features due to time constraints.

Congrats to all of them and hopefully they continue hacking!

What Happened
--------------

I wasn't able to talk to all the teams nor stay at the event full time but here is
how I saw things. 

Organization was perfect. The best organized non-commercial local event I've seen in years.
There was food, beverages, T-shirts, even beer :). There were six big IT companies
[sponsoring](http://hackfmi.com/sponsors-and-partners/) the
event. All of these are successful Bulgarian born companies.
Let that serve as an example!

The faculty was supporting the event too.
There were API and SQL dump for the teams to use. The entire building was open
during the weekend and during the night. Teams were able to make use of many rooms. 
From what I know some of the successful ideas will be implemented into the faculty
administration as well. All of this is a first time and quite unexpected for a 
Bulgarian university. I smell the wind of change already. 

Technology
----------

My technology view of the event is limited to the teams I've mentored explicitly and the ones
I happened to walk by and interfere with. Naturally I gravitated around 4 teams using
Django and found two teams using PHP.

Django guys were doing well despite one of the teams not having any experience with it. 
Most of the applications were such that didn't require extensive knowledge of Django internals
but require mere programming of all features they wanted to implement. 

What stroked me is that folks were making their database models too complicated. 
I stumbled across two use cases in different teams where they wanted to have 
one to many or many to many relationships. I strongly advised against this.
Hopefully they will remember.

Django makes schema design a child's play and probably this is why lots of people
abuse and misuse that. My advise is keep the database as simple as possible
and move everything up the application layer. It's easier to change and to maintain
that way. Not to mention experienced DBAs are hard to find. 

**Keep the DB simple and know your tools well! **

With PHP the case was pretty much the same. Guys had some extra fields in their DB schema
which were unnecessary. They also wanted to abuse the data types of the DB and not use native types.

All of these technological misunderstandings are coming from inexperience, I know.
To get a closer look at why it is important to have a simple schema look at:
[Disqus: Scaling the World’s Largest Django Application](http://ontwik.com/python/disqus-scaling-the-world%E2%80%99s-largest-django-application/)


The Hackers
------------

During one of the breaks I was outside and one of the mentors complained that
ideas were pretty much standard. No screen scraping for additional information, 
no mashing up, no revolutionary ideas. Everybody was using the provided API and
SQL dumps. Well almost.

One of my favorite [teams](https://github.com/vcrazy/project-6) set off to
write a PHP robot which will automatically login and extract information from
SUSI (the faculty information system). Unfortunately that didn't work so they
had to abandon it. They didn't known [Selenium](http://docs.seleniumhq.org/)
and there was not enough time to
try and hack some browser side extension which will do the trick but they promised
to try it.


Because of their unorthodox approach from the start they became my personal favorites
and received Red Hat swag from me.

![Team Six](/images/hackfmi/hackfmi2013_team_six_rh_swag.jpg "Team Six")
Adrian and Vihren are Team Six!

What I didn't like
------------------

I didn't like the fact that there was lots of duplicate work and ideas. Only one team
built a mobile application based on API and services provided by another team.

I suggest there's a #hackfmi IRC channel next time so that people can communicate
with each other and focus on building great apps not reinventing the wheel. 
**Use IRC, you are hackers!**


What I was missing is that nobody proposed a pure cloud or big data application.
I don't know if there was enough data provided by the faculty for such kind of
ideas, probably there wasn't. Maybe next time there will be.


Ohloh Stats
-----------

While not participating actively except for a few hours of mentoring I found a
way to contribute. Many of the projects repositories are listed under
<https://www.ohloh.net/p/hackfmi2013> which provides some interesting insight
and stats.

The list is incomplete. Lots of teams didn't have any GitHub repos
or didn't push the code recently. I will be contacting all of them in the next few days
and hopefully we will have a more accurate statistics by the end of the week.
Expect a separate blog post about it.



If you missed this event you should be sorry. [You were warned](/blog/2013/03/24/upcoming-hackatons-in-sofia/)!
If you attended please share your experience with me. What you liked, what you didn't. 


