Title: Quality Assurance According 2 Einstein
Headline: links and references
date: 2017-04-20 18:00
comments: true
Tags: QA, fedora.planet
og_image: images/qa_einstein.png
twitter_image: images/qa_einstein.png

![logo](/images/qa_einstein.png "logo")


[Quality Assurance According 2 Einstein](https://www.facebook.com/events/1887550261534408/)
is a talk which introduces several different ideas about how we need to think
and approach software testing. It touches on subjects like mutation testing,
pairwise testing, automatic test execution, smart test non-execution, using tests
as monitoring tools and team/process organization.

Because testing is more thinking than writing I have chosen a different format
for this presentation. It contains only slides with famous quotes from one
of the greatest thinkers of our time - Albert Einstein!

This blog post includes the accompanying links and references only! It is my first
iteration on the topic so expect it to be unclear and incomplete, use your imagination!
I will continue 
working and presenting on the same topic in the next few months
so you can expect updates from time to time. In the mean time I am happy to discuss
with you down in the comments.


> IMAGINATION
> IS MORE
> IMPORTANT
> THAN KNOWLEDGE.


* [Hello World bug challenge]({filename}2016-03-25-hello-world-bug-challenge.markdown)
* [Testing a Sudoku]({filename}2016-04-16-hiring-qa-sudoku.markdown#disqus_thread)
* <https://github.com/weldr/welder-web/pull/56>
* <https://github.com/weldr/welder-web/pull/59>


> THE FASTER YOU GO,
> THE SHORTER
> YOU ARE.

* [Using Statistics to Predict Which Tests to Run](http://bit.ly/GTAC2016Unity3D)
* [The framework that knows its bugs](http://bit.ly/ISTA2016ExMachina)
* [Testing Red Hat Enterprise Linux the Microsoft way]({filename}2017-04-14-testing-rhel-microsoft.markdown)
* [Automatic dependency testing with Strazar](http://mrsenko.com/blog/mr-senko/2016/05/18/triggering-automatic-dependency-testing/)
* [Automatic cargo update, test and pull request]({filename}2017-04-12-automatic-cargo-update-pull-request.markdown)


> IF THE FACTS
> DON'T FIT
> THE THEORY,
> CHANGE THE FACTS.

* [Coverage is Not Strongly Correlated with Test Suite Effectiveness](https://www.youtube.com/watch?v=sAfROROGujU&list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db&index=47)
* [Code Coverage is a Strong Predictor of Test Suite Effectiveness](https://www.youtube.com/watch?v=NKEptA3KP08&list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db&index=1)
* [Mutation testing vs. coverage, Pt. 1]({filename}2016-12-27-mutation-vs-coverage.markdown)
* [Mutation testing vs. coverage, Pt. 2]({filename}2017-04-05-mutation-vs-coverage-pt2.markdown)
* There are 101 coverage metrics according to [Cem Kaner](http://www.badsoftware.com/coverage.htm).
  Which ones are you measuring and what conclusions are you making out of these metrics?


> THE WHOLE OF
> SCIENCE
> IS NOTHING MORE
> THAN A REFINEMENT
> OF EVERYDAY
> THINKING.

* [How to find 1000 bugs in 30 minutes](https://github.com/HackBulgaria/QA-and-Automation-101/tree/master/lesson12)
* [How we found a million style and grammar errors in the English Wikipedia](https://www.youtube.com/watch?v=m5NfgXP76Vw&index=1&list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db&t=103s)
* [Simple Testing Can Prevent Most Critical Failures](https://www.youtube.com/watch?v=56oNQf5oITw&list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db&t=1300s&index=47)
* [Need it robust, make it fragile](https://www.youtube.com/watch?v=nCGBgI1MNwE&list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db&index=60)
    * btw its me who asks the first question at the end :)

> INSANITY -
> DOING THE SAME THING
> OVER AND OVER
> AND EXPECTING
> DIFFERENT RESULTS.

* [4 Quick Wins to Manage the Cost of Software Testing]({filename}2016-12-28-4-quick-wins-sw-testing.markdown)

This principle can be applied to any team/process within the organization.
The above link is reference to a nice book which was recommended to me but the
gist of it is that we always need to analyze, ask questions and change is we want
to achieve great results. A practicle example of what is possible if you follow
this principle is this talk
[Accelerate Automation Tests From 3 Hours to 3 Minutes](https://www.youtube.com/watch?v=khSsjjg2eSQ&index=1&list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db).

> THE ONLY
> REASON FOR TIME
> IS SO THAT
> EVERYTHING DOESN'T
> HAPPEN AT ONCE.

The topic here is "using tests as a monitoring tool".
This is something I started a while back ago, helping a prominent startup with their
production testing but my involvement ended very soon after the framework was
deployed live so I don't have lots of insight.

As the first few days this technique identified some unexpected behaviors,
for example a 3rd party service was updating very often. Once even they were
broken for a few hours - something nobody had information about.

Since then I've heard about 2 more companies using similar techniques to continuously
validate that production software continues to work without having a physical
person to verify it. In the event of failures there are alerts which are
delath with accordingly.


> NO PROBLEM
> CAN BE SOLVED FROM
> THE SAME LEVEL
> OF CONSIOUSNESS
> THAT CREATED IT.

That much must be obvious to us quality engineers. What about the future however?

* [How do I implement AI in test automation](https://www.quora.com/How-do-I-implement-AI-in-test-automation)
* [source{d} - Building the first AI that understands code](http://sourced.tech/)

I don't have anything more concrete here. Just looking towards what is coming next!


> DO NOT WORRY ABOUT
> YOUR DIFFICULTIES
> IN MATHEMATICS.
> I CAN ASSURE
> YOU MINE ARE STILL
> GREATER.

Thanks for reading and happy testing!
