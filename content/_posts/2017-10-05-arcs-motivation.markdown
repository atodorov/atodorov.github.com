Title: The ARCS model of motivational design
Headline: applied in practice
date: 2017-10-05 10:40
comments: true
Tags: fedora.planet, QA
og_image: images/motivation.jpg
twitter_image: images/motivation.jpg

![Motivation](/images/motivation.jpg "Motivation")

The ARCS model is an instructional design method developed by John Keller
that focuses on motivation. ARCS is based on a research into best practices
and successful teachers and gives you tactics on how to evaluate your
lessons in order to build motivation right into them.

I have conducted and oversaw quite a few trainings and I have not been impressed
with the success rate of those so this topic is very dear to me.
Success for me measures in the ability to complete the training and
learn the basis of a technical topic. And then gather the initial
momentum to continue developing your skills within the chosen field.
This is what I've been doing for myself and this is what I'd like to
see my students do.

In his paper (I have a year 2000 printed copy from Cuba)
Keller argues that motivation is a product of four factors:
**Attention, Relevance, Confidence and Satisfaction**. You need all of them
incorporated in your lessons and learning materials for them to be motivational.
I could argue that you need the same characteristics at work in order to
motivate people to do their job as you wish.

Once you start a lesson you need to grab the audience **Attention** so they
can listen to you. Then the topic needs to be **relevant** to the audience
so they will continue listening to the end. This makes for a good start
but is not enough. **Confidence** means for the audience to feel confident
they can perform all the necessary tasks on their own, that they have
what it takes to learn (and you have to build that). If they think they
can't make it from the start then it is a lost battle. And **Satisfaction**
means the person feels that achievements are due to their own abilities and
hard work not due to external factors (work not demanding enough, luck, etc).

If all of the above 4 factors are true then the audience should feel
personally motivated to learn because they can clearly understand the
benefit for themselves and they realize that everything depends on them.

ARCS gives you a model to evaluate your target audience and lesson properties
and figure out tactics by which to address any shortcomings in the above 4 areas.


Last Friday I hosted 2 training sessions: a Python and Selenium workshop
at HackConf and then a lecture about test case management and demo of
[Kiwi TCMS](http://kiwitcms.org) before students at Pragmatic IT academy.
For both of them I used the simplified ARCS evaluation matrix.

In this matrix the columns map to the ARCS areas while the rows map to
different parts of the lesson: audience, presentation media, exercise, etc.
Here's how I used them (I've mostly analyzed the audience).

Python & Selenium workshop
--------------------------

* Attention
    - (+) this is an elective workshop
    - (+) the topic is clear and the curricula is on GitHub
    - (+) the title is catchy (Learn Python & Selenium in 6 hours)
    - (+) I am well known in the industry
* Relevance
    - (+) Basic Python practical skills, being able to write small programs,
      knowing the basic building blocks
    - (+) Basic Selenium skills: finding and using elements
    - (+) Basic Python test automation skills: writing simple tests and asserts
* Confidence
    - (+) each task has tests which need to report PASS at the end
    - (-) need to use PyCharm IDE, unfamiliar with IDEs
    - (-) not enough experience with programming or Linux
    - (-) not enough experience with (automation) testing
    - (-) all materials and exercises are in English
* Satisfaction
    - (-) not being able to create a simple program


From the above it was clear that I didn't need to spend much time on building
attention or relevance. The topic itself and the fact that these are skill which
can be immediately applied at work gave the workshop a huge boost. During the
opening part of my workshop I've stated "this training takes around 2 months,
I've seen some of you forking my GitHub repo so I know you are prepared. Let's
see how much you can do in 6 hours" which sets the challenge and was my attention
building moment. Then I reiterated that all skills are directly applicable in
daily work confirming the relevance part.

I did need a confidence building strategy though. So having all the tests ready
meant evaluation was quick and easy. Anton (my assistant) and I promised to help
with the IDE and all other questions to counter the other items on the list.
During the course of the workshop I did quick code review of all participants
that managed to complete their tasks within the hour giving them quick tips on
how to perform or highlighting pieces of code/approaches that were different
from mine or that I found elegant or interesting. This was my confidence building
strategy. Code review and verbal praising also touches on the satisfaction
area, i.e. the participant gets the feeling they are doing well.

My Satisfaction building strategy was kind of mixed. Before I read about ARCS
I wanted to give penalty points to participants who didn't complete on time and then
send them home after 3 fails. At the end I only said I will do this but didn't
do it.

Instead I used the challenge statement from the attention phase and
turned that into a competition. The first 3 participants to complete their module tasks on time
were rewarded chocolates. With the agreement of the entire group the grand prize
was set to be a small box of the same chocolates and this would be awarded to
the person with the most chocolates (e.g. the one who's been in top 3 the most times).

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Bistra is our winner. 4/5 times in top 3 <a href="https://twitter.com/hashtag/Python?src=hash&amp;ref_src=twsrc%5Etfw">#Python</a> <a href="https://twitter.com/hashtag/Selenium?src=hash&amp;ref_src=twsrc%5Etfw">#Selenium</a> <a href="https://twitter.com/hashtag/testing?src=hash&amp;ref_src=twsrc%5Etfw">#testing</a> <a href="https://twitter.com/hashtag/HC17?src=hash&amp;ref_src=twsrc%5Etfw">#HC17</a> <a href="https://t.co/vXrPhElbbW">pic.twitter.com/vXrPhElbbW</a></p>&mdash; Alexander Todorov (@atodorov_) <a href="https://twitter.com/atodorov_/status/913787872032980993?ref_src=twsrc%5Etfw">September 29, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

I don't know if ARCS had anything to do with it but this workshop
was the most successful training I've ever done. 40% of the participants
managed to get at least one chocolate and at least 50% have completed all of
their tasks within the hour. Normally a passing rate on such training is
around 10 to 20 %.


During the workshop we had 5 different modules which consisted of 10-15 minutes
explanation of Python basics (e.g. loops or if conditions), quick Q&amp;A session
and around 30 minutes for working alone and code review. I don't think I was following
ARCS for each of the separate modules because I didn't have time to analyze them
individually. I gambled all my money on the introductory 10 minutes!


TCMS lecture
------------

My second lecture for the day was about test case management. The audience was
students who are aspiring to become software testers and attending the
Software Testing training at Pragmatic. In my lecture (around 1 hour) I wanted
to explain what test management is, why it is important and also demo the
tool I'm working on - [Kiwi TCMS](http://kiwitcms.org). The analysis looks like:

* Attention
    - (+) the entire training was elective but
    - (-) that particular lecture was mandatory. Students were not able to select
          what they are going to study
* Relevance
    - (-) it may not be clear what TCMS is and why we need it
    - (+) however students may sense that this is something work related since
          the entire training is
* Confidence
    - (-) unknown UI, generally unfamiliar workflow
    - (-) not enough knowledge how to write a Test Plan document or test cases
* Satisfaction
    - (-) how to make sure new skills can be applied in practice


So I was in a medium need of a strategy to build attention. My opening was by introducing
myself to establish my professional level and introducing [Kiwi TCMS](http://kiwitcms.org)
by saying it is the best open source test case management system to which I'm one of the
core maintainers.

Then I had a medium need of a relevance building strategy. I did this by explaining what
test management is and why it is important. I've talked briefly about QA managers trying to
indirectly inspire the audience to aim for this position. I finished this part by telling
the students how a TCMS system helps the ordinary guy in their daily work - namely by
giving you a dashboard where you can monitor all the work you need to do, check your
progress, etc.

I was in a strong need to build confidence. I did a 20-30 minutes demonstration where
I was writing a Test Plan and test cases and then pretending to execute them and marking bugs
and test results in the system. I told the students "you are my boss for today, tell me what
I need to test". So they instructed me to test the login functionality of the system
and we agreed on 5 different test cases. I described all of these into Kiwi TCMS and began
executing them. During execution I opened another browser window and did exactly what the
test case steps were asking for. There were some bugs so I promptly marked them as such and
I promised I will fix them.


To build satisfaction I was planning on having the students write one test plan and some
test cases but we didn't have time for this. Their instructor promised they will be doing
more exercises and using Kiwi TCMS in the next 2 months but this remains to be seen.
I've wrapped my lecture by giving advise to use Kiwi TCMS as a portfolio building tool.
Since these students are newcomers to the QA industry their next priority will be looking
for a job. I've advised them to document their test plans and test cases into Kiwi TCMS
and then present these artifacts to future employers.
I've also told them they are more than welcome to test and report bugs against Kiwi TCMS
on GitHub and add these bugs to their portfolio!


This is how I've applied ARCS for the first time. I like it and will continue to use it for
my trainings and workshops. I will try harder to make the application process more iterative
and apply the method not only to my opening speech but for all submodules as well!

One thing that bothers me is can I apply the ARCS principles when doing a technical
presentation and how do they play together or clash with storytelling, communication style and
rhetoric (all topics I'm exploring for my public speaking). If you do have more experience
with these please share it in the comments below.



Thanks for reading and happy testing!
