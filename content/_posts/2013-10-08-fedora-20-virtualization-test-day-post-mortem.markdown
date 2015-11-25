---
layout: post
Title: Fedora 20 Virtualization Test Day Post-mortem
date: 2013-10-08 22:01
comments: true
Tags: Fedora, QA
---

!["Fedora 20 banner"](/images/fedora/fedora20-banner.png "Fedora 20 banner")

Here is a quick summary of the first Fedora Test Day in Sofia I hosted at
[init Lab](http://initlab.org) today.

Attendance was quite poor, actually nobody else except me participated but
almost nobody else visited the hackespace as well. I get that it is a
working day and Test Days conflict with regular business hours but this
is not going to change anyway. On the other hand where were all the freelancers
and non-office job workers who usually hang around in the Lab? I have no idea!

On IRC there was much better activity, 5 or 6 people were testing across
Asia, Europe and USA time zones. You can see the test results
[here](http://209.132.184.192/testdays/show_event?event_id=7).
I've started filing quite a few bugs in the morning and continued well into the
afternoon. I've managed to file a total of
[10 bugs](https://bugzilla.redhat.com/buglist.cgi?bug_id=1016435,1016449,1016488,1016530,1016604,1016613,1016648,1016663,1016704,1016715).
Some of them were not related to virtualization and some of them turned out to be
duplicates or not a bug. I even managed to file 2 duplicate bugs which likely have the
same root cause myself :). 

I've also experienced two bugs filed by other people:
[RHBZ #967371](https://bugzilla.redhat.com/show_bug.cgi?id=967371) for MATE desktop
and [RHBZ #1015636](https://bugzilla.redhat.com/show_bug.cgi?id=1015636) for
virt-manager's Save/Restore functionality.

I've tried ARM on x86_64 but that didn't get anywhere near a running system.
I will make another post about ARM and what I've discovered there.

The one thing I liked is the 
[test results application](http://209.132.184.192/testdays/show_event?event_id=7).
It is not what I'm used to when dealing with RHEL, has far less features but is
very fast and easy to use and suits the Test Days participants just fine.
And is definitely much easier to use compared to filing results in the wiki.

Overall Fedora 20 virtualization status according to me is pretty good.

I hope to see more attendance [on Thursday](http://initlab.org/event/gnome-test-day)
when we're going to test GNOME 3.10.
