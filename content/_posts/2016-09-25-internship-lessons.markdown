Title: What Ivan Learned from Organizing Internships
Headline: for junior developers in Ruby
date: 2016-09-25 11:30
comments: true
Tags: events

This is a summary of [Ivan Nemytchenko](http://inem.at/)'s talk at
EuRuKo yesterday
(slides [here](http://www.slideshare.net/creatop/my-experiense-of-remote-internship-for-junior-ruby-developers)).
I'm writing this because that was the best talk both
in terms of content and visual presentation I saw at the conference and because
it is closely related to my work with [HackBulgaria](http://hackbulgaria.com).


The short story is that at some point Ivan was mentoring several junior developers
and saw the need to scale this effort so he did a call for interns and got back 60 replies.

What an Intern Gets
-------------------

1. Projects in their portfolio
2. Working experience, including team work
3. Developing an entire product from idea to production

Ivan wanted to find suitable interns who have basic Ruby on Rails knowledge
and who could invest a minimum of 20 hours per week of their time so he devised
an aptitude test of 3 parts. 

<blockquote class="twitter-tweet" data-lang="en">
<p lang="en" dir="ltr">The three part test <a href="https://twitter.com/inem">@inem</a> used to challenge 60 candidates for a Ruby internship. Pretty cool. <a href="https://twitter.com/hashtag/euruko?src=hash">#euruko</a> <a href="https://t.co/OsnN03pXkf">pic.twitter.com/OsnN03pXkf</a></p>&mdash; Tatiana Stantonian (@binaryberry) <a href="https://twitter.com/binaryberry/status/779664766394564608">September 24, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Part 1 is developing basic functionality of the product.
Part 2 was adding different user types which require different validation logic, etc.
Part 3 was adding "purchasing" logic via external APIs. In Part 3 intentionally
there was no code review!

The final result was shit! That was the purpose of the test. The reasoning being that
there is no right or wrong way to solve the problems he presented to the interns. Instead
he wanted to make them think and decide on a solution. Then feel the pain of their decision.
Ivan argues that what made us senior developers are these pains we have experienced at some
point in our careers, those fuck-ups that we did in some old project. All of them made us
better in our job because we could learn from the mistakes we've made and more importantly
understand the consequence of our decisions.

The common mistakes Ivan saw were:

* Ignoring levels of abstraction;
* Using too many gems without knowing or understanding their limitations;
* Gems were treated as the only way to solve a problem. More importantly changing
this way was out of the question;
* Interns didn't know about [service objects](http://stevelorek.com/service-objects.html),
well even some experienced developers seem to not know that;
* Business logic was all around the place;
* Bad naming all around

The next thing Ivan did was a group hangout code review followed by a short lecture about
design patterns, a refactoring session and finally cross code review. At the end the
product was delivered as expected.

Following these initial efforts Ivan continued (with even more interns, or the next group of them I think)
by asking interns to develop internship automatization, that is a means for the system to
distribute tasks based on git commits, tags, etc so it can scale. They've added an admin
dashboard and started working on an open source alternative to NewRelic (if I got that correctly).
He was also able to enlist 2 more mentors to help him.

Problems Ivan found:

* Not enough mentors and external projects to work on for all of the interns;
* Treating a project as not real (e.g. not a real world product) is a mistake;
* A training project has the same management issues that a real product will have
and they need to be resolved in pretty much the same way;
* There was collective irresponsibility from the group of interns. They didn't do
what they said they will do;
* There were communication issues between the interns and the lack of enough mentors
was an obvious problem.
* There was also lack of motivation.

I'd say these are the typical problems one also sees in almost any teams. It doesn't
matter if these are teams of students or teams of developers inside some company.

What a Junior Needs
-------------------

* A real project to work on;
* **A business context, a reason why something should be done and why it needs to be
done in a particular way**;
* Some visible achievement for their portfolio;
* Team work experience;
* Whole cycle development experience.

Ivan thinks that **the aptitude test worked great** because his interns were able to find
good jobs afterwards but he will change a few things. There will be even more tests
and he will reject unfit/bad interns. He will also do call for mentors not only for interns.
And he wants to turn mentors' experience into tests as well.

I particularly like the "business context" item. IMO even seasoned developers need to have this
if they are expected to create a great product for their company. We're not just coders but
sometimes companies forget that!

I am also wondering how can I apply a similar aptitude test in my work (both mentoring at
HackBulgaria and otherwise).

How about Senior Developers
---------------------------

* They all have routine tasks;
* and research tasks;
* Nice to have features and
* Low priority features;
* Side project ideas
* Missing features in their favorite open source projects

Senior developers' tasks and desires will have to align with what a junior needs in order
for the mentorship to work. As senior devs we often make a mistake and expect everyone else
to think the same way we do and act as fast as we do. **Ideally senior developers want to have multiple clones
of ourselves to work with!** I myself have been guilty of that and trying to change.

In the context of a for-profit company the above findings should be taken into deep consideration
if you are about to have interns.


After the talk I was lucky to talk to Ivan and tell him more about the training sessions
at HackBulgaria. I also proposed to him the sponsorship model which he hasn't considered.
He then made a counter offer: ask interns for high payment upfront and let them recoup that
based on their progress towards the end.

I am really happy to have heard this presentation and being able to talk to Ivan in person. I also have
my notes about my "QA and Automation 101" training at HackBulgaria and I now
have a better idea how to go about organizing and summarizing them (will try to publish that soon).

Last but not least, Ivan works at GitLab and promised to look at an issue I personally have
so here it is [GitLab #7953](https://gitlab.com/gitlab-org/gitlab-ce/issues/7953) :).


Related reading
---------------

* My *How to hire Software Testers* series: parts
[One](http://atodorov.org/blog/2016/04/12/how-to-hire-software-testers-pt-1/),
[Two](http://atodorov.org/blog/2016/04/16/how-to-hire-software-testers-pt-2/) and
[Three](http://atodorov.org/blog/2016/06/03/how-to-hire-software-testers-pt-3/);
* RadoRado's [How I Became a Better Developer](http://radorado.me/kak_stanah_po_dobar_programist/)
in Bulgarian but please use Google translate;
* [Damir Zekic](https://twitter.com/sidonath)'s The Importance of Teaching and Mentoring (from the
pov of the mentor) lightning talk at EuRuKo (will link video soon), similar to what Rado says;
* Alex Moldovan's [How Outsourcing is Killing Cluj](https://medium.com/@alexnm/how-outsourcing-is-killing-cluj-345a4cbbcb6c#.nutpdfftu).
