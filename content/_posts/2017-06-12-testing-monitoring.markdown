Title: Monitoring behavior via automated tests
Headline: and why is it important
date: 2017-06-12 11:30
comments: true
Tags: QA, fedora.planet
og_image: images/qa_shutterfly.jpg
twitter_image: images/qa_shutterfly.jpg

In my last several presentations I briefly talked about
using your tests as a monitoring tool. I've not been eating my own
dog food and stuff failed in production!

What is monitoring via testing
------------------------------

This is a technique I coined 6 months ago while working with Tradeo's team.
I'm not the first one to figure this out so if you know the proper
name for it please let me know in the comments.
So why not take a subset of your automated tests and run them regularly against
production? Let's say every hour?

In my particular case we
started with integration tests which interact with the product (a web app)
in a way that a living person would do. E.g. login, update their settings,
follow another user, chat with another user, try to deposit money, etc.
The results from these tests are logged into a database and then charted
(using Grafana). This way we can bring lots of data points together and easily
analyze them.

This technique has the added bonus that we can cover the most critical
test paths in a couple of minutes and do so regularly without human intervention.
Perusing the existing monitoring infrastructure of the devops team we can configure
alerts if need be. This makes it sort of early detection/warning system plus
it gives a degree of possibility to spot correlations between data points or
patterns.

As simple as it sounds I've heard about a handfull of companies doing this
sort of continuous testing against production. Maybe you can implement something
similar in your organization and we can talk more about the results?

Why does it matter
------------------

Anyway, everyone knows
[how to write Selenium tests]({filename}2017-05-27-qa-python-selenium-101-retro.markdown)
so I'm not going to bother you with the details. Why does this kind of
testing matter?

Do you remember a recent announcement by GitHub about Travis CI leaking some
authentication tokens into their public log files? I did receive an email about
this but didn't pay attention to it because I don't use GitHub tokens for
anything I do in Travis. However as a safety measure GitHub had went ahead and
wiped out my security tokens.

The result from this is that my
[automated upstream testing infrastructure](http://mrsenko.com/blog/mr-senko/2016/05/18/triggering-automatic-dependency-testing/)
had stopped working! In particular my requests to the GitHub API stopped
working. And I didn't even know about it!

This means that since May 24th there have been at least 4 new
versions of libraries and frameworks on which some of my software depends
and I failed to test them! One of them was *Django 1.11.2*.

I have supplied a new GitHub token for my infra but if I had monitoring
I would have known about this problem well in advance. Next I'm off to write
some monitoring tests and also implement better failure detection in
[Strazar](https://github.com/MrSenko/strazar) itself!


Thanks for reading and happy testing (in production)!
