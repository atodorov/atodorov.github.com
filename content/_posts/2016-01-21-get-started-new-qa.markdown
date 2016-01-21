Title: How to Get Started on a New QA Project
date: 2016-01-21 14:00
comments: true
Tags: QA

Every time I have to look at a new software project and use my QA powers
to help them I follow a standard process of getting involved. Usually my
job is to reveal which areas are lacking adequate test coverage and propose
and implement improvements. Here's what it looks like.


Obtain Domain Knowledge
------------------------

Whatever the software does I don't start looking into the technical details
before I have domain knowledge about the subject. If the domain is purely
outside my expertise my first reading materials have
nothing to do with the product itself. My goal is to learn how the domain
works, what language it uses, any particular specifics that may exists, etc.

Then I start asking general questions about the software, how it works and
what it does. At this stage I'm not trying to go into details but rather
cover as much angles as possible. I want to know the big picture of how
things are supposed to work and what the team is trying to do. This also
starts to reveal the architecture behind the project.


Then I start using the software as if I'm the intended target audience while
taking notes about everything that seems odd or I simply don't understand.
Being with limited knowledge about the domain and the product helps a lot
because I haven't developed any bias yet. This initial hands-on introduction
is best done with a peer who is better familiar with the
product. It is not necessary for the peer to be a technical person, although
that helps when implementation related questions arise.

RTFM
-----

I make a point to read any available documents, wikis, READMEs, etc. They can
fill the gaps with often used terms, explain processes and workflows or
reveal that such are missing and document existing infrastructure.
Quite often I'm able to see some areas for
improvements directly from reading the documentation.

At this stage I'm just collecting notes and impressions which will be validated
later. I don't try to remember all of the docs because I can always go back
and read them again. Instead I try to remember the topics these documents
talk about and possibly collect links for future reference.


Get to Know the Devel Team
---------------------------

One thing I hate the most, except not knowing what a piece of code does is
not knowing who to ask. Quite often team structure follows the application
structure - front-end, back-end, mobile, etc. While getting to know who does
what I also use this as opportunity to gain deeper knowledge about the
product. I will talk to team leads and individual developers asking them to
explain the chosen architecture and also tell me what are the most annoying
problems according to them.

Later this knowledge makes it easier to see trends and suggest changes that
will improve the overall product quality. Having good working relationship
with developers also makes it easy for these changes to get through.


Get to Know the QA Team
------------------------

Similar to the previous step but with a deeper focus on details. This is my
personal domain so I'm trying to figure out who does what in terms of software
testing for the project in question. When I'm working with less experienced
QA teams I focus on what are the individual tasks at hand, how often are they
executed, what is the general workflow and how are we dealing with bugs.

Behind the scenes what this accomplishes is that I'm able to find what the
bug reporting, testing and verification process is. How are new bugs discovered
and what are the general test strategies without confronting people
directly. I also find what tools are used and get familiar with them in the
process and discover the level of technical abilities of individual team members.


Get to Know the App
--------------------

Armed with the previous knowledge I set off to explore the entire application.
Again this is best done with a peer. This time I look at every screen, widget
and button there is. I try using all the available features which also doubles
as an exploratory testing session.

For backend services which are usually harder to test I opt for a more
detailed explanation session with the developers. Here's the time when I'm
asking the question "How do you test .... ?" multiple times.

Deploy to Production
---------------------

If possible I like to keep an eye on how things are deployed to production.
It is not uncommon for software to experience problems due to problems with
the deployment procedure or the production environment itself.

Also with agile teams it is common to deploy more often. This in turn may
generate additional work for QA. Knowing how software is deployed to
production and what the workflow in the team is helps later with planning
test activities and resources.


Read All Bugs
-------------

Unless there are millions of them I try to go through all the bugs reported
in the bug tracker. If the project has some age to it earlier reports may not
be relevant anymore. In this case my marker is an important event like big
refactoring, important or big new features, changes in teams and organization
or similar. The thinking behind this is that every big change introduces lots
of risks from software quality stand point. Also large changes invalidate
previous conditions and may render existing problems obsolete, replacing them
with newer set of problems instead!


From reading bug reports I'm able to discover failure trends, which in turn
indicate areas for improvement. For example: lots of translation related bugs
indicate problems with the translation workflow, lots of broken existing
functionality means poor regression testing, probably also lack of unit tests,
lots of partially(poorly) implemented features shows chaotic planning and
unclear feature specifications, etc.

At this stage I try to classify problems both by technical component and
by type of issue. Later this will be my starting reference for creating
test strategies and test plans!

If possible and practical I talk to support and read all the support tickets
as well. This gives me an idea which problems are most visible to
customers which aren't necessary the biggest technical issues but may consume
man power dealing with them.


Summarize, Divide and Conquer
------------------------------

Depending on the project and team size these initial steps will take anywhere 
from a full week to a month or even more. After they are complete I'm
feeling comfortable talking about the software at hand and have a list of
possible problems and areas of improvements.

After talking to people in charge (e.g. PMs, Project Leads, etc) my initial
list is transformed into tasks. I strive to keep the tasks as independent
as possible. Then these tasks are prioritized and it's time to start executing
them one by one.






