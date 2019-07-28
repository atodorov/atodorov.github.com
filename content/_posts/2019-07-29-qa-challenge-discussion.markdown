Title: How to start solving problems in the QA profession
Headline: summary and action items from recent discussion
date: 2019-07-29 10:50
comments: true
Tags: fedora.planet, QA
og_image: images/discussion.jpg
twitter_image: images/discussion.jpg

3 months ago [Adriana](/blog/categories/adriana/) and I hosted a discussion panel at
[QA: Challenge Accepted](http://qachallengeaccepted.com/) conference together with
Aleksandar Karamfilov (Pragmatic), Gjore Zaharchev (Seavus, Macedonia) and
Svetoslav Tsenov (Progress Telerik). The recording is available below in mixed
Bulgarian and English languages:

<iframe width="560" height="315" src="https://www.youtube.com/embed/2LWRF8moV2A" frameborder="0" allowfullscreen></iframe>

The idea for this was born at the end of the previous year mainly because I was
disappointed by what I was seeing in the local (and a bit of European) QA communities.
In
[this interview](https://dev.bg/%D1%80%D0%B0%D0%B7%D0%B3%D0%BE%D0%B2%D0%BE%D1%80-%D1%81-%D0%B5%D0%B2%D0%B3%D0%B5%D0%BD%D0%B8-%D0%BA%D0%BE%D1%81%D1%82%D0%B0%D0%B4%D0%B8%D0%BD%D0%BE%D0%B2-%D0%B7%D0%B0-%D1%80%D0%B0%D0%B1%D0%BE%D1%82/)
Evgeni Kostadinov (Athlon) says:

> I would advise everyone who is now starting into Quality Assurance to display
> mastership at work.

This is something that we value very strongly in the open source world. For example
in [Kiwi TCMS](http://kiwitcms.org) we've built a team of people who contribute on
a regular basis, without much material rewards, constantly improve their skills,
show progress and I (as the project leader) am generally happy with their work. OTOH
I do lots of in-house training at companies, mostly teaching programming to testers
(Python & Ruby). Over the last 2 years I've had 30% of people who do fine, 30% of people
who drop out somewhere in the middle and 30% of people who fail very early in the process.
That is 60% failure rate on entry level material and exercises!


All of this goes to show that there is big disparity between professional testing and the
open source world I live in. And I want to start tackling the problems because I want the
testers in our communities to really become professional in their field so that we can work
on lots more interesting things in the future. Some of the problems that I see are:

* Lack of personal motivation - many people seem comfortable at entry level positions
  and when faced with the challenge to learn or do something new they fail big time
* Using the wrong titles/job positions in the wrong context - calling QA somebody
  who's clearly a tester or calling Senior somebody who barely started their career.
  All of that leads to confusion across the board
* Lack of technical skills, particularly when it comes to programming - how would you
  expect to do software testing if you have no idea how that software is built ?!?
  How are you going to get advantage of new tools and techniques when most of them
  are based around automation and source code ?!?


Motivation
----------

I am strong believer that personal motivation is key to everything. However this is also
one of my weakest points. I don't know how to motivate others because I never felt the
need for someone else to motivate me. I don't understand why there could be people who
are seemingly satisfied with a very low hanging fruit when there are so many opportunities
waiting for them. Maybe part of my reasoning is because of my open source background
where DIY is king, where "Talk is cheap. Show me the code." is all that matters.

Discussion starts with Svetoslav who doesn't
have a technical education/background. He's changed profession later in life and in
recent years has been speaking at some events about testing they do in the
NativeScript team.

**Svetoslav:** He realized that he needs to make a change in his life,
invested lots in studying (not just 3 months) all the while traveling between his home town
and Sofia by car and train and still keeping his old job to be able to pay the bills.
He sees the profession not as a lesser field compared to development but as equal.
That is he views himself as an engineer specializing in testing.

**Aleksandar:** There are no objective reasons for some people to be doing very good
in our field while others fail spectacularly. This coming from the owner of one of the
biggest QA academies in the country. A trend he outlines is the folks who come for
knowledge and put their effort into it and the ones who are motivated by the relatively
high salary rates in the industry. In his opinion current practitioners should not
be giving false impression that the profession is easy because there are equally hard
items as in any other engineering field. Wrong impression about how hard/easy it is
to achieve the desired monetary reward is something that often leads to failure.

**Gjore:** Coming from his teaching background at the University of Niš he says people
generally have the false impression they will learn everything by just attending
lectures/training courses and not putting effort at home. I can back this up 100%
judging by performance levels of my corporate students. Junior level folks often
don't understand how much they need to invest into improving their skills especially
in the beginning. OTOH job holders often don't want to listen to others because they
think they know it all already. Another field he's been experimenting with is a
mentoring program.


Tester, QA, QE, etc - which is what and why that matters
--------------------------------------------------------

IMO part of the problem is that we use different words to often describe the same thing.
Companies, HR, employees and even I are guilty of this. We use various terms
interchangeably while they have subtle but important differences.

As a friend of mine told me

> even if you write automation all the time if you do it after the fact
> (e.g. after a bug was reported) then you are not QA/QE - you are a simple tester
> (with a slightly negative connotation)


**Aleksandar:** terminology has been defined long time ago but the problem comes from
job offers which use the wrong titles (to make the position sound sexier). Another
problem is the fact that Bulgaria (also Macedonia, Serbia and I dare say Romania) are
predominantly outsourcing destinations: your employer really needs testers but fierce
competition, lack of skilled people (and distorted markets), etc leads to distortion
in job definitions. He's blaming companies that they don't listen enough to their
employees. 

Note: there's nothing bad in being "just a tester" executing test scenarios and reporting
bugs. That was one of the happiest moments in my career. However you need to be aware of
where you stand, what is required from you and how you would like to develop in the future.


**Svetoslav:** Doesn't really know all the meaning of all abbreviations and honestly
doesn't really care. His team is essentially a DevOps team with lots of mixed responsibility
which necessitates mixed technical and product domain skills. Note that Progress is by
contrast a product company, which is also the field I've always been working in. That is
to be successful in a product company you do need to be a little bit of everything
at different times so the definition of quality engineer gets stretched and skewed
a lot.


**Gjore:** He's mostly blaming middle level management b/c they do not posses
all the necessary technical skills and don't understand very well the nature of
technical work. In outsourcing environment often people get hired just to
provide head count for the customer, not because they are needed. Software testing
is relatively new on the Balkans and lots of people still have no idea
what to do and how to do it. We as engineers are often silent and contribute to
these issues by not raising them when needed. We're also guilty of not
following some established processes, for example not
attending some required meetings (like feature planning) and by doing so
not helping to improve the overall working process. IOW we're not always
professional enough.


Testers and programming
-----------------------

<blockquote class="twitter-tweet">
    <p lang="en" dir="ltr">Testers should be code literate. Reading code is a crucial skill for any tester and writing code has so many uses beyond just boilerplate automation.
        <a href="https://t.co/Tts0rzHI4Y">https://t.co/Tts0rzHI4Y
    </a></p>&mdash; Amber Race (@ambertests)
    <a href="https://twitter.com/ambertests/status/1109862132554694656?ref_src=twsrc%5Etfw">March 24, 2019</a>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


On one of my latest projects we've burned through
the following technologies in the span of 1 year: Rust, Haskell, Python, React, all sorts
of cloud vendors (pretty much all of them) and Ansible of course. Testing was adjusted
as necessary and while hiring we only ask for the person to have adequate coding
skills in Python, Bash or any other language. The rest they have to learn accordingly.

So what to do about it? My view is that anyone can learn programming but not many
people do it successfully.

**Svetoslav:** To become an irreplaceable test engineer you need skills. Broad technical
skills are a must and valued very highly. This is a fact, not a myth. Information is
easily accessible so there's really no excuse not to learn. Mix in product and business
domain knowledge and you are golden.

**Aleksandar:** Everyone looks like they wish to postpone learning something new, especially
programming. Maybe because it looks hard (and it is), maybe because people don't feel
comfortable in the subject, maybe because they haven't had somebody to help them
and explain to them critical concepts. OTOH having all of that technical understanding
actually makes it easier to test software b/c you know how it is built and how it works.
Sometimes the easiest way to explain something is by showing its source code (I do this a lot).

Advice to senior folks: don't troll people who have no idea about something they've
never learned before. Instead try to explain it to them, even if they don't want to hear it.
This is the only way to help them learn and build skills. In other words: be a good
team player and help your less fortunate coworkers.

**Gjore:** A must have is to know the basic principles of
[object oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
and I would add also [SOLID](https://en.wikipedia.org/wiki/SOLID). With the ever changing
landscape of requirements towards our profession we're either into the process of change
or out of this process.


Summary and action items
------------------------

The software testing industry is changing. All kind of requirements are pushing our
profession outside its comfort zone, often outside of what we signed up for initially.
This is a fact necessitated by evolving business needs and competition. This is equally
true for product and outsourcing companies (which work for product companies after all).
This is equally true for start-ups, SME and big enterprises.

![QA shifting left and right](/images/qa_shift_left_right.png "QA shifting left and right")
Image from [No Country for Old QA, Emanuil Slavov (Komfo)](https://www.youtube.com/watch?v=jFZd6MaKKZg)

What can we do about it ?

**Svetoslav:** Invest in building an awesome (technical) team. Make it a challenge to
learn and help your team mates to learn with you. However be frank with yourself and with
them. Ask for help if you don't know something. Don't be afraid to help other people
level-up because this will ultimately lead to you leveling-up.


**Aleksandar:** Industry should start investing in improving workers qualification level
because Bulgaria is becoming an expensive destination. We're on-par with some companies
in western Europe and USA (coming from a person who also sells the testing service).
Without raising skills level we're not going to have anything competitive to offer.
Also pay attention to building an inclusive culture especially towards people on the
lowest level in terms of skills, job position, responsibilities, etc.

**Gjore:** Be the change, drive the change, otherwise it is not going to happen!


So here are my tips and tricks the way I understand them:

* Find your motivation and make sure it is the "correct" one - there's nothing
  wrong in wanting a higher salary but make sure you are clear that you are
  trading in your time and knowledge for that. Knowing what's in it for you will
  help you self motivate and pull yourself through hard times
* Find a mentor if possible - I've never had one so I can't offer much advise here
* Software testing is hard, no kidding. Some researchers claim it is even harder
  than software development because the field of testing encompasses the entire field
  of development
* Once you understand the concepts and how things work it becomes easy. We do have
  very fast rate of technology change but most of the things are not fundamental
  paradigm change. Building on this basic knowledge makes things easier (or to put it
  mildly: everything has been invented by IBM in the 1970s)
* You will not learn everything (not even close) in a short course. I've spent 5 years
  in engineering university learning how software and hardware works. I've been
  programming for the past 20 years every single day. This makes it easier but
  there are lots of things I have not idea about. 30-60 minutes of targeted learning
  and applying what you learn goes a long way over the course of many years
* Invest in yourself, nobody is going to do it for you. If you look at
  [github.com/atodorov](https://github.com/atodorov) you will notice that everything
  is green. If you drill down by year you will find this is the case for the past
  3-4 years only. The 10 years before that I've spent building up to this moment.
  It is only now that I get to reap some of the benefits of doing so (like a random
  Silicon Valley startup telling me they are fans of my work or being invited as
  a speaker at events)
* Programming is hard, when you don't know the basic concepts and when you lack
  the framework to think about abstractions (loops, conditionals, etc). When you
  learn all of this it becomes harder because you need to learn different languages
  and frameworks. However it is not impossible. There are lots of free materials
  available online, now more than ever
* Think about your "position" in the team/company. What do you do, what is required
  of you, how can you do it better ? Call things with their real names and
  explain to your coworkers which is what. This will bring more consistency in the
  entire community


Lots of these items sound cliche but they are true. There's nothing stopping you from
becoming the best QA engineer in the world but you.


To be continued
---------------

This first discussion was born out of necessity and is barely scratching the surface.
The format is not ideal. We didn't present multiple points of view.
We didn't have time to prepare for it to be honest!

Gjore and I made a promise to continue the discussion bringing it to Macedonia and Serbia.
I am hoping we can also bring other neighboring countries like Romania and Greece on board
and learn from mutual experience.


See you soon and Happy testing!
