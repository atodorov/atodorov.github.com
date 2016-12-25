Title: 4 Quick Wins to Manage the Cost of Software Testing
Headline: a guide by QASymphony
date: 2016-12-28 11:48
comments: true
Tags: QA, fedora.planet
og_image: images/software-testing.jpg
twitter_image: images/software-testing.jpg

    Every activity in software development has a cost and a value. Getting cost to
    trend down while increasing value, is the ultimate goal.

This is the introduction of an e-book called
[4 Quick Wins to Manage the Cost of Software Testing](http://pi.qasymphony.com/four-quick-wins-thank-you).
It was sent to me by Ivan Fingarov couple of months ago. Just now I've managed to
read it and here's a quick summary. I urge everyone to download the original copy
and give it a read.

The paper focuses on several practices which organizations can apply immediately
in order to become more efficient and transparent in their software testing. While
larger organizations (e.g. enterprises) have most of these practices already in place
smaller companies (up to 50-100 engineering staff) may not be familiar with them
and will reap the most benefits of implementing said practices. Even though I work
for a large enterprise I find this guide useful when considered at the individual
team level!

The first chapter focuses on *Tactics* to minimize cost: Process, Tools, Bug System Mining
and Eliminating Handoffs.

In *Process* the goal is to minimize the burden of documenting the test process
(aka testing artifacts), allow for better transparency and visibility outside the QA group
and streamline the decision making process of what to test and when to stop testing,
how much has been tested, what the risk is, ect. The authors propose testing core functionality
paired with emerging risk areas based on new features development. They propose making
a list of these and sorting that list by perceived risk/priority and testing as much
as possible. Indeed this is very similar to the method I've used at Red Hat when designing
testing for new features and new major releases of Red Hat Enterprise Linux. A similar
method I've seen in place at several start-ups as well, although in the small organization
the primary driver for this method is lack of sufficient test resources.

*Tools* proposes the use of test case management systems to ease the documentation burden.
I've used [TestLink](http://testlink.org/) and [Nitrate](https://github.com/Nitrate/Nitrate).
From them Nitrate has more features but is currently unmaintained with me being the
largest contributor on GitHub. From the paid variants I've used
[Polarion](https://www.polarion.com/products/qa/test-automation) which I generally dislike.
Polarion is most suitable for large organizations because it gives lots of opportunities
for tracking and reporting. For small organizations it is an overkill.

*Bug System Mining* is a technique which involves regularly scanning the bug tracker
and searching for patterns. This is useful for finding bug types which appear
frequently and generally point to a flaw in the software development process. The fix for these
flaws usually is a change in policy/workflow which eliminates the source of the errors.
I'm a fan of this technique when joining an existing project and need to assess
what the current state is. I've done this when consulting for a few start-ups, including
[Jitsi Meet](http://meet.jit.si) (acquired by Atlassian), however I'm not doing bug mining
on a regular basis which I consider a drawback and I really should start doing!

For example at one project I found lots of bugs reported against translations, e.g.
missing translations, text overflowing the visible screen area or not playing well with
existing design, chosen language/style not fitting well with the product domain, etc.

The root cause of the problem was how the software in question has been localized.
The translators were given a file of English strings, which they would translate and
return back in an spread sheet. Developers would copy&paste the translated strings
into localization files and integrate with the software. Then QA would usually
inspect all the pages and report the above issues. The solution was to remove devel
and QA from the translation process, implement a translation management system together
with live preview (web based) so that translators can keep track of what is left to
translate and can visually inspect their work immediately after a string was translated.
Thus translators are given more context for their work but also given the responsibility
to produce good quality translations.

Another example I've seen are many bugs which seem like a follow up/nice to have features
of partially implemented functionality. The root cause of this problem turned out to be
that devel was jumping straight to implementation without taking the time to brainstorm
and consult with QE and product owners, not taking into account corner cases and minor
issues which would have easily been raised by skillful testers. This process lead to
several iterations until the said functionality was considered initially implemented.


*Eliminating Handoffs* proposes the use of cross-functional teams to reduce idle time
and reduce the back-and-forth communication which happens when a bug is found, reported,
evaluated and considered for a fix, fixed by devel and finally deployed for testing.
This method argues that including testers early in the process and pairing them with
the devel team will produce faster bug fixes and reduce communication burden.

While I generally agree with that statement it's worth noting that cross-functional
teams perform really well when all team members have relatively equal skill level
on the horizontal scale and strong experience on the vertical scale (think T-shaped specialist).
Cross-functional teams
don't work well when you have developers who aren't well versed in the testing domain
and/or testers who are not well versed in programming or the broader OS/computer science
fundamentals domain. In my opinion you need well experienced engineers for a good cross-functional
team.


In the chapter *Collaboration* the paper focuses on pairing, building the right thing
and faster feedback loops for developers. This overlaps with earlier proposals for
cross-functional teams and QA bringing value by asking the "what if" questions.
The chapter specifically talks about the Three Amigos meeting between PM, devel and QA
where they discuss a feature proposal from all angles and finally come to a conclusion
what the feature should look like. I'm a strong supporter of this technique and have
been working with it under one form or another during my entire career. This also
touches on the notion that testers need to move into the *Quality Assistance* business
and be proactive during the software development process, which is something I'm
hoping to talk about at the
[Romanian Testing Conference](http://www.romaniatesting.ro/) next year!


Finally the book talks about *Skills Development* and makes the distinction between
Centers of Excellence (CoE) and Communities of Practice (CoP). Both the book and I
are supporters of the CoP approach. This is a bottoms-up approach which is open for
everyone to join in and harnesses the team creative abilities. It also takes into
account that different teams use different methods and tools and that
"one size doesn't fit all"!

    Skilled teams find important bugs faster, discover innovative solutions to hard
    testing problems and know how to communicate their value. Sometimes, a few super
    testers can replace an army of average testers.

While I consider myself to be a "super tester" with thousands of bugs reported there
is a very important note to make here. Communities of Practice are successful when
their members are self-focused on skill development! In my view and to some
extent the communities I've worked with everyone should strive to constantly improve
their skills but also exercise peer pressure on their co-workers to not fall behind.
This has been confirmed by other folks in the QA industry and I've heard it many times
when talking to friends from other companies.



Thanks for reading and happy testing!
