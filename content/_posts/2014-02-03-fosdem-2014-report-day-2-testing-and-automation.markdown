---
layout: post
Title: FOSDEM 2014 Report - Day #2 Testing and Automation
date: 2014-02-03 22:54
comments: true
categories: ['events', 'Fedora', 'QA']
---

![Testing and Automation](/images/fosdem/2014/testing_automation.jpg "Testing and Automation")

FOSDEM was hosting the
[Testing and automation devroom](https://fosdem.org/2014/schedule/track/testing_and_automation/)
for the second year and this was the very reason I attended the conference. I managed to get in
early and stayed until 15:00 when I had to leave to catch my flight (which was late :(). 

There were 3 talks given by Red Hat employees in the testing devroom which was a nice opportunity
to meet some of the folks I've been working on IRC with. Unfortunately I didn't meet anyone from
Fedora QA. Not sure if they were attending or not. 

All the talks were interesting so see the official schedule and video for more details. I will
highlight only the items I saw as particularly interesting or have not heard of before. 

ANSTE
-----

ANSTE - Advanced Network Service Testing Environment is a test infrastructure controller,
something like our own [Beaker](http://beaker-project.org/) but designed to create complex
networking environments. I think it lacks many of the provisioning features built in Beaker
and integration with various hypervisors and bare-metal provisioning. What it seems to do better
(as far as I can tell from the talk) is to deploy virtual systems and create more complex network
configuration between them. Not something I will need in the near future but definitely worth
a look at. 


cwrap
------

{% blockquote %}
cwrap is...

a set of tools to create a fully isolated network environment to test client/server components on a single host.
It provides synthetic account information, hostname resolution and support for privilege separation.
The heart of cwrap consists of three libraries you can preload to any executable.
{% endblockquote %}

That one was the coolest technology I've seen so far although I may not need to use it at all,
hmmm maybe testing DHCP fits the case.

It evolved from the Samba project and takes advantage of the order in which
libraries are searched when resolving functions. When you preload the project libraries
to any executable they will override standard libc functions for working with sockets,
user accounts and privilege escalation.

The socket_wrapper library redirects networking sockets through local UNIX sockets and
gives you the ability to test applications which need privileged ports with a local developer
account. 

The nss_wrapper library provides artificial information for user and group accounts,
network name resolution using a hosts file and loading and testing of NSS modules.


The uid_wrapper library allows uid switching as a normal user (e.g. fake root) and
supports user/group changing in the local thread using the syscalls (like glibc).


All of these wrapper libraries are controlled via environment variables and definitely
makes testing of daemons and networking applications easier.


Testing Documentation
----------------------

That one was just scratching the surface of an entire branch of testing which I've not
even considered before. The talk also explains why it is hard to test documentation and
what possible solutions there are. 

If you write user guides and technical articles which need to
stay current with the software this is definitely the place to start.


Automation in the Foreman Infrastructure
----------------------------------------

The last [talk](http://ftp.osuosl.org/pub/fosdem//2014/previews/fosdem/fosdem_2014/dv/UD2218A/2014-02-02/12_51_36.ogv)
I've listened to. Definitely the best one from a general testing approach
point of view. Greg talked about starting with Foreman unit tests, then testing the merged PR,
then integration tests, then moving on to test the package build and then the resulting packages themselves. 

These guys try to even test their own infrastructure (infra as code) and the test suites
they use to test everything else. It's all about automation and the level of confidence
you have in the entire process.


I like the fact that no single testing approach can make you confident enough before shipping
the code and that they've taken into account changes which get introduced at various places
(e.g. 3rd party package upgrades, distro specific issues, infrastructure changes and such) 

If I had to attend only one session it would have been this one. There are many things for me
to take back home and apply to my work on Fedora and RHEL.



If you find any of these topics remotely interesting I advise you to wait until FOSDEM video
team uploads the recordings and watch the entire session stream. I'm definitely missing a lot
of stuff which can't be easily reproduced in text form.


You can also find my report of the first FOSDEM'14 day on Saturday
[here](/blog/2014/02/03/fosdem-2014-report-day-1-python-stands-lightning-talks/).
