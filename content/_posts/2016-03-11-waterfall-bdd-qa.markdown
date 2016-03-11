Title: QA Switch from Waterfall to BDD
Headline: initial observations
date: 2016-03-11 11:08
comments: true
Tags: fedora.planet, QA

For the last two weeks I've been experimenting with Behavior-Driven Development
(BDD) in order to find out what it takes for the Quality Assurance department
to switch from using the Waterfall method to BDD. Here are my initial
observations and thoughts for further investigation.

Background
----------

Developing an entire Linux distribution (or any large product for that matter)
is a very complicated task. Traditionally QA has been involved in writing the
test plans for the proposed technology updates, then execute and maintain them
during the entire product life-cycle reporting and verifying tons of bugs
along the way. From the point of view of the entire product the process is
very close to the traditional waterfall development method. I will be using
the term waterfall to describe the old way of doing things and BDD the new one.
In particular I'm referring to the process of analyzing the proposed feature set
for the next major version of the product (e.g. Fedora) and designing the
necessary test plans documents and test cases.

To get an idea about where does QA join the process see the
[Fedora 24 Change set](https://fedoraproject.org/wiki/Releases/24/ChangeSet).
When the planning phase starts we are given these "feature pages" from which
QA needs to distill test plans and test cases. The challenges with the
waterfall model are that QA joins the planning process rather late and there
is not enough time to iron out all the necessary details. Add to this the fact
that feature pages are often incomplete and vaguely described and sometimes
looking for the right answers is the hardest part of the job.

QA and BDD
----------

Right now I'm focusing on using the
[Gherkin](https://github.com/cucumber/cucumber/wiki/Gherkin)
*Given-When-Then* language to
prepare feature descriptions and test scenarios from the above feature pages.
You can follow my work on [GitHub](https://github.com/atodorov/bdd/) and
I will be using them as examples below. Also see examples from my
co-workers [1](https://github.com/tlamer/bdd),
[2](https://github.com/hroncok/BDD).

With this experiment I want to verify how hard/easy it is for QA to write
test cases using BDD style documents and how is that different from the
traditional method. Since I don't have any experience (nor bias) towards BDD
I'm documenting my notes and items of interest.


Getting Started
---------------

It took me about 2 hours to get started. The essence of Gherkin is the
*Action & Response* mechanism. **Given** the system under test (SUT) is in a
known state and **when** an action is taken **then** we expect something
to happen in response to the action. This syntax made me think from the
point of view of the user. This way it was very easy to identify different
user roles and actions which will be attempted with the SUT. This also made
my test scenarios more explicit compared to what is described in the wiki pages.
IMO being explicit when designing tests is a good thing. I like it that way.

OTOH the same explicitness can be achieved with the waterfall method as well.
The trouble is that this is often overlooked because
we're not in the mindset to analyze the various user roles and scenarios.
When writing test cases with waterfall the mindset is more focused on the
technical features, e.g. how the SUT exactly works and we end up missing
important interactions between the user and the system. At least I can recall
a few times that I've made that mistake.

Tagging the scenarios is a good way of indicating
which scenario covers which roles. Depending on the tools you use it should
be possible to execute test scenarios for different roles (tags). In waterfall
we need to have a separate test plan for each user role, possibly duplicating
some of the test cases across test plans. A bit redundant
but more importantly easier to forget the bigger picture.


Big, Small & Undefined
-----------------------

BDD originates from TDD which in turn relies heavily on unit testing and
automation. This makes it very easy to use BDD 
test development (and even automate)
for self contained changes, especially ones which affect
only a single component (e.g. a single program). From the Fedora 24 changes
such are for example the systemd and system-python split.

I happen to work in a team where we deal with large changes, which affect
multiple components and infrastructure. Both the
[Pungi Refactor](https://fedoraproject.org/wiki/Releases/24/ChangeSet#Pungi_Refactor)
and
[Layered Docker Image Build Service](https://fedoraproject.org/wiki/Releases/24/ChangeSet#Layered_Docker_Image_Build_Service)
for which I've written BDD style test scenarios are of this nature. This leads
to the following issues:

* QA doesn't always have the entire infrastructure stack in a
staging environment for testing so we need to test on the live infra;
* QA doesn't always have the necessary access permissions to execute
the tests and in some cases never will. For example it is very unlikely
that QA will be able to build a test release and push that for syncing
to the mirrors infrastructure to verify that there are no files left behind;
* Not being able to test independently means QA has to wait for something to happen
then verify the results (e.g. rel-eng builds new Docker images and pushes
them live). When something breaks this testing is often too late.

Complex changes are often not described into detail. As they affect multiple
infrastructure layers and components sometimes it is not known what the required
changes need to be. That's why we implement them in stages and have contingency
plans. However this makes it harder for QA to write the tests. 
Btw this is the same regardless of which development method is used.
The good thing is that by forcing you to think from the POV of the user and
in terms of action & response BDD helps identify these missing bits faster.

For example, with Pungi (Fedora distro build tool),
the feature pages says that the produced directory
structure will be different from previous releases but it doesn't say what
is going to be different so we can't really test that. I know from
experience that this may break tools which rely on this structure like
virt-manager and anaconda and have added simple sanity tests for them.

In the Docker feature page we have functional requirement for automatic
image rebuilds if one of the underlying components (e.g. RPM package) changes.
This is not described in details and so is the test scenario. I can easily
write a separate BDD feature document for this functionality alone.


With the waterfall model when a feature isn't well defined QA often waits
for the devel team to implement the basic features and then writes test cases
based on the existing behavior. This is only good for regression testing
the next version but it can't show you something that is missing because
we're never going to look for it. BDD makes it easier to spot when we need
better definitions of scope and roles, even better functional requirements.


Automation and Integration
--------------------------

Having a small SUT is nice. For example we can easily write a
test script to install, upgrade and query RPM packages and verify the
systemd package split. We can easily prepare a test system and execute
the scripts to verify the expected results.

OTOH complex features are hard to integrate with BDD automation tools.
For the Docker Image Build Service the straight forward script would
be to start building a new image, then change an underlying component
and see if it gets rebuilt, then ensure all the content comes from
the existing RPM repos, then push the image to the Docker registry
and verify it can be used by the user, etc, etc. 
All of these steps take a non-trivial amount of time. Sometimes hours.
You can also execute them in parallel to save time but how do you sync
back the results ?

My preference for the moment is to kick-off individual
test suites for a particular BDD scenario and then aggregate the results back.
This also has a side benefit - for complex changes we can have layered
BDD feature documents, each one referencing another feature document.
Repeat this over and over until we get down to purely technical scenarios
which can be tested easily. Once the result are in go back the chain
and fill-in the rest. This way we can traverse all testing activities
from the unit testing level up to the infrastructure level.

I actually like the back & forth traversing idea very much. I've always
wanted to know how does each individual testing effort relate to the
general product development strategy and in which areas the product is
doing well or not. You can construct the same chain of events with waterfall
as well. IMO BDD just makes it a bit more easier to think about it.


Another problem I faced is how do I mark the scenarios as out of scope
for the current release ? I can tag them or split them into separate files
or maybe something else? I don't know which one is the best practice. In
waterfall I'll just disable the test cases or move them into a separate
test plan.

TODO
----

I will be writing more BDD test definitions in the upcoming 2 weeks to get
more experience with them. I still don't have a clear idea how to approach
BDD test writing when given a particular feature to work on. So far I've
used the functional requirements and items of concern (when present), in the
feature pages, as a starting point for my BDD test scenarios.

I also want to get more feedback from the development teams and product
management folks.


Summary
---------

BDD style test writing puts the tester into a mind set where it is easier
to see the big picture by visualizing different user roles and scenarios.
It makes it easier to define explicit test cases and highlights missing
details. It is easier for QA to join early in the planning process by
defining roles and thinking about all the possible interactions with the SUT.
This is the biggest benefit for me!

Self-contained changes are easier to describe and test automatically.

Bigger and complex features are harder to describe and even harder to
automate in one piece. Divide and conqueror is our best friend here!

