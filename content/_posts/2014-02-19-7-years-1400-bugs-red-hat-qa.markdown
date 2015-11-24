---
layout: post
Title: 7 Years and 1400 Bugs Later as Red Hat QA
date: 2014-02-19 10:43
comments: true
categories: ['RHEL', 'Fedora', 'QA']
---

Today I celebrate my 7th year working at Red Hat's Quality Engineering department.
Here's my story!

![Platform QE](/images/redhat_platform_qe.jpg "Platform QE")

On a cold winter Friday in 2007 I left my job as a software developer in Sofia,
packed my stuff together, purchased my [first laptop](http://amzn.to/1hlPuyr) and
on Sunday jumped the train to Brno to join the Release Test Team at Red Hat.
Little did I know what it was all about. When I was offered the position
I was on a very noisy bus and had to pick between two positions. I didn't quite understood
what were the options and just picked the second one.
Luckily everything turned out great and continues to this day.

I'm sharing my experience and highlighting some bugs which I've found.
Hopefully you will find this interesting and amusing. If you are a QA engineer
I urge you to take a look at [my public bug portfolio](http://red.ht/1gbHElQ),
dive into details, read the comments and learn as much as you can.


What do I do exactly
--------------------

From all QE teams in Red Hat, Release Test Team is the first one and
last one to test a release. The team has both technical function and a more managerial one.
Our focus is on the core Red Hat Enterprise Linux product. 
Unfortunately I can't go into much details because this is not a public facing unit.
I will limit myself to **public and/or non-sensitive information**.


We are the first to test a new nightly build or a
snapshot of the upcoming RHEL release. If the tree is installable other teams take over
and do their magic. At the end when bits are published live we're the last to
verify that content is published where it is expected to be. In short this is
covering the work of the release engineering team which is to build a product and
publish the contents for consumption.

The same principles apply to Fedora although the engagement here is less demanding.

Personally I have been and continue to be responsible for Red Hat Enterprise Linux 5
family of releases. It's up to me to give the go ahead for further testing or request
a re-spin. This position
also has the power to block and delay the GA release if not happy with testing or
there is a considerable risk of failure until things are sorted out.


Like in other QA teams I create test plan documents, write test case scenarios,
implement test automation scripts (and sometimes tools), regularly execute said test
plans and test cases, find and report any new bugs and verify old ones are fixed. 
Most importantly make sure RHEL installs and is usable for further testing :).

Sometimes I have to deal with capacity planning and as RHEL 5 installation 
test lead I have to organize and manage the entire installation testing campaign
for that product.

My favorite testing technique is
[exploratory testing](https://en.wikipedia.org/wiki/Exploratory_testing).


Stats and Numbers
-----------------

It is hard (if not impossible) to [measure QA work](https://github.com/atodorov/qe-metrics)
with numbers alone but here are some interesting facts about my experience so far.

* Nearly 1400 bugs filed (1390 at the time of writing);
* Reported bugs across 32 different products. Top 3 being RHEL 6, RHEL 5 and Fedora (1000+ bugs);
* Top 3 components for reporting bugs against: anaconda, releng, kernel;
* Nearly 100 bugs filed in my first year 2007;
* The 3 most productive years being 2010, 2009, 2011 (800 + bugs); 
* Filed 200 bugs/year which is about 1 bug/day considering holidays;
* 35th top bug reporter (excluding robot accounts). I was in top 10 a few years back;

Many of [the bugs I report](http://red.ht/1gbHElQ) are private so if you'd like
to know more stats just ask me and I'll see what I can do.


2007
----

My very first bug is [RHBZ #231860](https://bugzilla.redhat.com/show_bug.cgi?id=231860)(private)
which is about the graphical update tool Pup which used to show the wrong number of available
updates.

Then I've played with adding [Dogtail](https://fedorahosted.org/dogtail/) support to Anaconda.
While initially this was rejected (Fedora 6/7), it was [implemented](https://fedoraproject.org/wiki/Anaconda/Features/Dogtail)
few years later (Fedora 9) and then removed once again during the big Anaconda rewrite.

I've spent my time working extensively on RHEL 5 battling with multi-lib issues, SELinux denials and
generally making the 5 family less rough. Because I was still on-boarding I generally worked
on everything I could get my hands on and also did some work on RHEL3-U9 (latest release
before EOL) and some RHEL4-U6 testing.

With ia64 on RHEL3 I found a corner case
[kernel bug](https://bugzilla.redhat.com/show_bug.cgi?id=240782) which flooded the serial
console with messages and caused a multi-CPU system to freeze.

In 2008 Time went backwards
---------------------------

My first bug in 2008 is [RHBZ #428280](https://bugzilla.redhat.com/show_bug.cgi?id=428280).
glibc introduced SHA-256/512 hashes for hashing passwords with crypt but that wasn't documented.

**UPDATE 2014-02-21**
While testing 5.1 to 5.2 updates I found
[RHBZ #435475](https://bugzilla.redhat.com/show_bug.cgi?id=435475) - a severe
**performance degradation** in the package installation process. Upgrades
took almost twice as much time to complete, rising **from 4 hours to 7 hours**
depending on hardware and package set. This was a tough one to test and verify.
**END UPDATE**


While dogfooding the 5.2 beta in March I hit
[RHBZ #437252](https://bugzilla.redhat.com/show_bug.cgi?id=437252) - kernel: Timer ISR/0: Time went backwards.
To this date this is one of my favorite bugs with a great error message!

Removal of a hack in RPM led to file conflicts under `/usr/share/doc` in several packages:
[RHBZ #448905](https://bugzilla.redhat.com/show_bug.cgi?id=448905),
[RHBZ #448906](https://bugzilla.redhat.com/show_bug.cgi?id=448906),
[RHBZ #448907](https://bugzilla.redhat.com/show_bug.cgi?id=448907),
[RHBZ #448909](https://bugzilla.redhat.com/show_bug.cgi?id=448909),
[RHBZ #448910](https://bugzilla.redhat.com/show_bug.cgi?id=448910),
[RHBZ #448911](https://bugzilla.redhat.com/show_bug.cgi?id=448911)
which is also the first time I happen to file several bugs in a row.

ia64 couldn't boot with encrypted partitions -
[RHBZ #464769](https://bugzilla.redhat.com/show_bug.cgi?id=464769),
RHEL 5 introduced support for ext4 - [RHBZ #465248](https://bugzilla.redhat.com/show_bug.cgi?id=465248)
and I've hit a fontconfig issue during upgrades - [RHBZ #469190](https://bugzilla.redhat.com/show_bug.cgi?id=469190)
which continued to resurface occasionally during the next 5 years.


This is the year when I took over responsibility for the general installation
testing of RHEL 5 from James Laska and will continue to do so until it reaches end-of-life!

I've also worked on RHEL 4, Fedora and even the OLPC project. On the testing side of things
I've participated in testing
[Fedora networking on the XO](https://fedoraproject.org/wiki/QA/TestPlans/Networking)
hardware and worked on translation and general issues.



2009 - here comes RHEL 6
------------------------

This year starts my 3 most productive years period. 

The second bug reported this
year is [RHBZ #481338](https://bugzilla.redhat.com/show_bug.cgi?id=481338) which
also mentions one of my hobbies - wrist watches. While browsing a particular
website Xorg CPU usage rose to 100%. I've seen a number of these through the years
and I'm still not sure if its Xorg or Firefox or both to blame. And I still see my
CPU usage go to 100% just like that and drain my battery. I'm open to suggestions how
to test and debug what's going on as it doesn't happen in a reproducible fashion.


I happened to work on RHEL 4, RHEL 5, Fedora and the upcoming RHEL 6 releases and
managed to file bugs in a row not once but twice. 
I wish I was paid per bug reported back then :).

The first series was about empty debuginfo packages with both empty packages which
shouldn't have existed at all
(e.g. [redhat-release](https://bugzilla.redhat.com/show_bug.cgi?id=500628)) 
and missing debuginfo information for binary packages
(e.g. [nmap](https://bugzilla.redhat.com/show_bug.cgi?id=500612)).

The second series is around 100 bugs which had to do with the texinfo
documentation of packages when installed with --excludedocs. The first one
is [RHBZ #515909](https://bugzilla.redhat.com/show_bug.cgi?id=515909) and the
last one [RHBZ #516014](https://bugzilla.redhat.com/show_bug.cgi?id=516014).
While this works great for bumping up your bug count it made lots of developers
unhappy and not all bugs were fixed. Still the use case is valid and these
were proper software errors. It is also the first time I've used a script to
file the bugs automatically and not by hand.


Near the end of the year I've started testing installation on new hardware
by the likes of Intel and AMD before they hit the market. I had the pleasure to work
with the latest chipsets and CPUs, even sometime pre-release versions and make sure
Red Hat Enterprise Linux installed and worked properly on them. I've stopped doing
this last year to free up time for other tasks.



2010 - one bug a day keeps developers at bay :)
-----------------------------------------------

My most productive year with 1+ bugs per day.

2010 starts with a bug about file conflicts (private one) and continues with the same
narrative throughout the year.
As a matter of fact I did a small experiment and found around **50000**
(you read that right, fifty thousand) potentially
conflicting files, mostly between multi-lib packages, which were being ignored by RPM
due to its multi-lib policies. However these were primarily man pages or documentation
and most of them didn't get fixed. The proper fix would have been to introduce a
-docs sub-package and split these files from the actual binaries. Fortunately the world
migrated to 64bit only and this isn't an issue anymore.

By that time RHEL 6 development was running at its peak capacity and there were Beta
versions available. Almost the entire year I've been working on internal RHEL 6 snapshots
and discovering the many new bugs introduced with tons of new features in the installer.
Some of the new features included better IPv6 support, dracut and KVM.

An interesting set of bugs from September are the rpmlint errors and warnings ones,
for example [RHBZ #634931](https://bugzilla.redhat.com/show_bug.cgi?id=634931). I just
run the most basic test tool against some packages. It generated lots of false negatives
but also revealed bugs which were fixed.

Although there were many bugs filed this year I don't see any particularly interesting ones.
It's been more like lots of work to improve the overall quality than exploring
edge cases and finding interesting failures. If you find a bug from this period that you
think is interesting I will comment on it.


2011 - Your system may be seriously compromised
-----------------------------------------------

This is the last year of my 3 year top cycle. 

It starts with [RHBZ #666687](https://bugzilla.redhat.com/show_bug.cgi?id=666687) -
a patch for my crappy printer-scanner-coffee maker which I've been carrying around
since [2009](https://bugzilla.redhat.com/show_bug.cgi?id=498228) when I bought it.

I was still working primarily on RHEL 6 but helped test the latest RHEL 4 release
before it went end-of-life. The interesting thing about it was that unlike other
released RHEL4-U9 was not available on installation media but only as an update from
RHEL4-U8. This was a great experience which you happen to see
[every 4 to 5 years](https://access.redhat.com/site/support/policy/updates/errata/) or so.

Btw I've also led the installation testing effort and RTT team through the last few
RHEL 4 releases but given the product was approaching EOL there weren't many changes
and things went smoothly.

A minor side activity was me playing around with
[USB Multi-seat](/blog/2011/03/14/usb-multi-seat-on-red-hat-enterprise-linux-6/)
and finding a few bugs here and there along the way.


Another interesting activity in 2011 was proof-reading the entire product documentation
before its release which I can now relate to the 
[Testing Documentation](/blog/2014/02/03/fosdem-2014-report-day-2-testing-and-automation/)
talk at FOSDEM 2014.

In 2011 I've started using the cloud and most notably Red Hat's OpenShift PaaS service.
First internally as an early adopter and later externally after the product was announced
to the public. There are a few interesting bugs here but they are private and I'm not
at liberty to share although they've all been fixed since then.

An interesting bug with NUMA, Xen and ia64
([RHBZ #696599](https://bugzilla.redhat.com/show_bug.cgi?id=696599) - private) had
me and devel banging our heads against the wall until we figured out that on this
particular system the NUMA configuration was not suitable for running Xen virtualization.

Can you spot the problem here ?
{% codeblock lang:python %}
try:
    import kickstartGui
except:
    print (_("Could not open display because no X server is running."))
    print (_("Try running 'system-config-kickstart --help' for a list of options."))
    sys.exit(0)
{% endcodeblock %}

Be honest and use the comments form to tell me what you've found. If you struggled
then see [RHBZ #703085](https://bugzilla.redhat.com/show_bug.cgi?id=703085) and come
back again to comment. I'd love to hear from you.


What do you do when you see an error message saying: 
**Your system may be seriously compromised! /usr/sbin/NetworkManager tried to load a kernel module.**
This is the scariest error message I've ever seen. Luckily its just
SELinux overreacting, see [RHBZ #704090](https://bugzilla.redhat.com/show_bug.cgi?id=704090).


2012 is in the red zone
-----------------------

While the number of reported bugs dropped significantly compared to previous
years this is the year when I've reported almost exclusively high priority and
urgent bugs, the first one being 
[RHBZ #771901](https://bugzilla.redhat.com/show_bug.cgi?id=771901).

[RHBZ #799384](https://bugzilla.redhat.com/show_bug.cgi?id=799384)(against Fedora)
is one of the rare cases when I was able to contribute
(although just by raising awareness) to localization and improved support for
Bulgarian and Cyrillic. 
The other one case was [last year](http://atodorov.org/blog/2013/10/11/fedora-20-gnome-3-dot-10-test-day-post-mortem/).
Btw I find it strange that although 
[Cyrillic was invented by Bulgarians](https://en.wikipedia.org/wiki/Cyrillic_script)
we didn't (or still don't) have a native font co-maintainer.
Somebody please step up!

The red zone bugs continue to span till the end of the year across RHEL 5, 6 and
early cuts of RHEL 7 with a pinch of OpenShift and some internal and external test tools.


In 2013 Bugzilla hit 1 million bugs
-----------------------------------

The year starts with a very annoying and still not fixed bug against ABRT.
It's very frustrating when the tool which is supposed to help you file bugs
doesn't work properly, see [RHBZ #903591](https://bugzilla.redhat.com/show_bug.cgi?id=903591).
It's a known fact that
[ABRT has problems](/2012/07/13/mission-impossible-abrt-bugzilla-plugin-on-rhel6/)
and for this scenario I may have a 
[tip](/blog/2013/10/12/tip-installing-missing-debuginfo-packages-for-abrt/) for you.

[RHBZ #923416](https://bugzilla.redhat.com/show_bug.cgi?id=923416) - another one of these
100% CPU bugs. As I said they happen from time to time and mostly go by unfixed or
partially fixed because of their nature. Btw as I'm writing this post and have
a few tabs open in Firefox it keeps using between 15% and 20% CPU and the CPU
temperature is over 90 degrees C. And all I'm doing is writing text in the console.
Help!

[RHBZ #967229](https://bugzilla.redhat.com/show_bug.cgi?id=967229) - a minor one but
reveals an important thing - your output (and input for that matter) methods may
be producing different results. Worth testing if your software supports more than one.

This year I did some odd jobs working on several of Red Hat's layered products mainly
Developer Toolset. It wasn't a tough job and was a refreshing break away from the mundane
installation testing.

While I stopped working actively on the various RHEL families which are under development
or still supported I happened to be one of top 10 bug reporters for high/urgent priority bugs
for RHEL 7. In appreciation Red Hat sent me lots of corporate gifts and the Platform QE hoodie
pictured at the top of the page. Many thanks!

In the summer Red Hat's 
[Bugzilla hit One Million bugs](/blog/2013/08/23/red-hats-bugzilla-hits-one-million-bugs/).
The closest I come to this milestone is
[RHBZ #999941](https://bugzilla.redhat.com/show_bug.cgi?id=999941).

I finally managed to transfer most of my responsibilities to co-workers and joined
the Fedora QA team as a part-time contributor. I had some highs and lows with
[Fedora test days in Sofia](/blog/2013/10/07/fedora-20-virtualization-and-gnome-test-days-at-init-lab-this-week/)
as well. Good thing is I scored another 15 bugs across the
[virtualization stack](/blog/2013/10/08/fedora-20-virtualization-test-day-post-mortem/)
and [GNOME 3.10](/blog/2013/10/11/fedora-20-gnome-3-dot-10-test-day-post-mortem/).



The year wraps up with another series of identical bugs,
[RHBZ #1024729](https://bugzilla.redhat.com/show_bug.cgi?id=1024729) and
[RHBZ #1025289](https://bugzilla.redhat.com/show_bug.cgi?id=1025289) for example.
As it [turned out](/blog/2013/12/24/upstream-test-suite-status-of-fedora-20/)
lots of packages don't have any test suites at all and those
which do don't always execute them automatically in %check. I've promised myself
to improve this but still haven't had time to work on it. Hopefully by
March I will have something in the works.

2014 - Fedora QA improvement
----------------------------

Last two months I've been working on some internal projects and looking
a little bit into improving processes, test coverage and QA infrastructure - 
[RHBZ #1064895](https://bugzilla.redhat.com/show_bug.cgi?id=1064895).
And Rawhide (upcoming Fedora 21) isn't behaving -
[RHBZ #1063245](https://bugzilla.redhat.com/show_bug.cgi?id=1063245).


My goal for this year is to do more work on improving the overall test coverage
of Fedora and together with the Fedora QA team bring an
[open testing infrastructure](/blog/2013/11/19/open-source-quality-assurance-infrastructure-for-fedora-qa/)
to the community. 

Let's see how well that plays out!




What do I do now
----------------

During the last year I have gradually changed my responsibilities to work more on Fedora.
As a volunteer in the Fedora QA I'm regularly testing installation
of Rawhide trees and try to work closely with the community. I still have to
manage RHEL 5 test cycles where I don't expect nothing disruptive at this stage in the
product life-cycle!

I'm open to any ideas and help which can improve test coverage and quality of software
in Fedora. If you're just joining the open source world this is an excellent
opportunity to do some good, get noticed and even maybe get a job. I will definitely
help you get through the process if you're willing to commit your time to this.

I hope this long post has been useful and fun to read. Please use the comments form to tell
me if I'm missing something or you'd like to know more.

*Looking forward to the next 7 years!*

