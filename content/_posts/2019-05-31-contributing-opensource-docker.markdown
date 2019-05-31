Title: Contributing to Open Source with Docker, Inc
Headline: BoF session in Sofia
date: 2019-05-31 12:50
comments: true
Tags: fedora.planet
og_image: images/docker_oss.jpg
twitter_image: images/docker_oss.jpg

![Contributing to OSS](/images/docker_oss.jpg "Contributing to OSS")

The rumors have finally been confirmed. Docker, Inc. is opening their new
R&D center in Sofia. At an event last night, they stated their intentions to do a fair amount
of product development in Sofia as well as contribute to the local society/community
too (if I got this correctly). This is very good news for the local eco-system so
congrats for that from my side!

This blog post outlines my impressions from the event and a few related more general
thoughts.


How did Docker came to Sofia?
-----------------------------

I don't know the details but their top team in Bulgaria seems to be coming
directly from VMware. So were other engineers present at the event who are
based elsewhere. When you think about it this is not surprising at all.
(FTR VMware is also directly responsible for having Uber engineering in Sofia).

VMware is one of the few companies in Bulgaria that does real product development
and R&D (credit where credit is due).
There's even a smaller number of companies developing infrastructure
products, e.g. the same things I test on behalf of Red Hat. The majority of the
other companies are either outsourcing or focused on products in upper layers
of the stack!


Contributing to Open Source according to Docker (and myself)
------------------------------------------------------------

This BoF session was lead by Andrew Hsu and Sebastiaan van Stijn.
The group was predominantly inexperienced in terms of OSS contribution but
motivated to try/find a project where they can contribute. From what I could
tell they were relatively experienced software engineers.

On my question "what are they planning for the local community in Sofia?" the
immediate answer was meet-ups and presentations which is expected. This is how
you start and try to establish the level of experience of the local groups
and their level of interest in what you are doing.

I prompted a bit further about workshops or hackathons and they told me
they've had a hacking even in Paris but didn't elaborate much further. Maybe
it is too early for them to be able to give more detailed answers.
Let's hope we'll see more practical events.

Andrew did outline the general principles of their community (aka don't be a jerk),
pointed out the various communication channels they have (rip IRC), the fact that
internally the company uses GitHub and encourages cross-team participation via
the [pull request workflow](https://gist.github.com/Chaser324/ce0505fbed06b947d962).
This is what my friends at [Bitergia](https://bitergia.com/) call "inner source"
and is a good thing!

A few of the participants asked how and where to start and all I kept hearing was
"follow pull requests on GitHub", "do you want to see some source code"! This is
something I take issue with so let me explain.

While that has been the historical model for doing open source, aka dig straight
into the problem, and also how I started and still do open source I think it doesn't
work in the modern world. What I've seen from my students and folks which I've trained
is that they have far too many opportunities to be bothered to dig deep into something
which seemingly puts roadblocks on every step of the way. Especially when you are
a new comer. I myself experience this regularly and often get frustrated by
communities who make it damn nearly impossible to land a code change. My only motivation
here is that I depend on that component being fixed and there is no work-around.


To be fair to Docker our Fedora or Red Hat communities aren't much better in this regard.
In most of the projects I've contributed they kind of expect you to be motivated
enough and be able to figure out both process and technical details mostly on your own!
Maybe it is the nature of working on platform and infrastructure. You do need a fair bit
of general knowledge and specific system knowledge to work on such projects.


My personal experience leading [Kiwi TCMS](http://kiwitcms.org) has been that most
contributors need a long time to settle in and feel comfortable in the project and
that they do need a fair amount of hand holding.

First and fore-most many contributors don't know the underlying technology well enough.
For complex software there's also the whole issue of computer science 101, operating systems,
how the kernel or virtualization engine works, etc. Then you need to know the architecture
of the software you want to fix, the libraries and frameworks it uses - this helps you
quickly navigate to the place which needs a patch. Honestly this takes years to master
and to develop a gut feeling about it. On the outside it may look easy because active
contributors have had many years of experience acquiring this knowledge.

Then we have the "process" part. How do I open or rebase a pull request. How to amend
commits, etc. This is something I learned the hard way but I've shown it to other
people and they were able to advance much more quickly. Also things like how do you communicate
with others in the community, how do you "push" for some types of changes, etc.
Dedicated mentors will help a lots here, but that also means dedicated contributors.


We do provide a detailed technical training
and on-boarding program and mentoring for Kiwi TCMS and still there are more people who give it a try
and drop out compared to those who stay with the team.
We still expect commitment and finishing the tasks one set out to complete though.


My initial impression (from Docker) for the moment is very guarded and mostly critical.
I feel like they are interested in finding folks to contribute to their own repositories
and then hire them (that is expected) but I don't feel like they care much about what
happens outside their own projects. I hope I am wrong and we do see engineers (regardless
of who employs them) contributing all over the place on a regular basis.


What is the problem ?
---------------------

The problem for the local eco-system (and it is a world wide problem)
is that there are many companies coming in but there is a very limited pool of talent.
Especially in less popular fields like research, operating systems and low level infrastructure.
That takes many years to develop in house and to reach critical mass for a thriving
community. I don't feel we are there yet!

In a later blog post I will describe the history of ScyllaDB which
is the measure of success I would like to see in Bulgaria.


The problem I see for the open source community (in the country) is that nobody is really
working on developing that. There are small efforts by individuals or a few companies but
the mechanics of open source and the culture of free sharing of knowledge is something
I don't see yet. I fail to see a program, like Google Summer of Code perhaps, where
developers are encouraged and supported to contribute just for the sake of contributing.

Also I fail to see a structure which will help new contributors and
young developers set out on a path of meaningful contributions early in their career
and by doing this improve their skills and personal brand which ties in with the first
paragraph.


These are some things I have observed and some gut feelings from someone who's been doing
open source for 15+ years. I can't pin point exact reason why this is happening.
I don't have a recipe how to fix it!

I do however keep in touch with like minded folks from several other companies and we've
discussed these topics occasionally. We do have some ideas but lack critical mass,
shared goal and self-organization.
