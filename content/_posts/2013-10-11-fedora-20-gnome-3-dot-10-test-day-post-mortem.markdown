---
layout: post
Title: Fedora 20 GNOME 3.10 Test Day Post-mortem
date: 2013-10-11 12:25
comments: true
Tags: Fedora, QA
---

!["Fedora sausage banner"](/images/fedora/sausage-banner.png "Fedora sausage banner")

Here is my summary of the second Fedora Test Day hosted at
[init Lab](http://initlab.org) yesterday.

Local attendance was a total disaster, in fact I was testing once again by my own.
This time
there were more people in the lab, all busy with their daily routines and tasks.
There were no people who came for the testing :(. I will have to try different
venues in the future and see if the situation improves.

On the testing front I managed to score 5 bugs against
[GNOME](https://bugzilla.gnome.org/buglist.cgi?bug_id=709797,709799,709806,709810)
and [Fedora](https://bugzilla.redhat.com/show_bug.cgi?id=1017807).
You can see the other test results and bugs on the
[wiki](https://fedoraproject.org/wiki/Test_Day:2013-10-10_Gnome_3.10).


There are two things I didn't like in particular

* GNOME 3 as well as its classic mode - simply not the environment I'm used to;
* Having to record test results in the wiki! I'm
[writing](https://lists.fedoraproject.org/pipermail/test/2013-October/118284.html)
to the Fedora QA mailing list about that as we speak.


At one time I was engaged in a discussion about which Bulgarian keyboard layout
should be the default in GNOME simply because of
[GNOME #709799](https://bugzilla.gnome.org/show_bug.cgi?id=709799). The default
keyboard layout will be Bulgarian (traditional phonetic) aka bg+phonetic.

{% blockquote %}
(16,13,26) rtcm: atodorov: are you bulgarian and/or live in bulgaria?
(16,14,20) rtcm: atodorov: if yes, I wanted to know which keyboard layout most people expect there to be the default
(16,16,34) atodorov: rtcm: I'm a Bulgarian, however I can't tell which one. Both Phonetic and standard (BDS) are common
(16,16,54) atodorov: a safe bet is to go with phonetic I guess. 
(16,19,46) rtcm: atodorov: can you tell me which one is it in XKB terms? is it "bg", "bg+bas_phonetic" or "bg+phonetic" ?
(16,20,51) rtcm: they're labeled as "Bulgarian", "Bulgarian (new phonetic)" and "Bulgarian (traditional phonetic)"
(16,21,30) atodorov: bg+phonetic is the traditional phonetic
(16,22,04) atodorov: bg labeled as "Bulgarian" is the standard one I guess. Here we call it BDS after the standardization institute
(16,22,34) atodorov: bg+bas_phonetic is created from the Bulgarian Academy of Science and is not very popular as far as I know. I've never seen it in use
(16,23,15) rtcm: atodorov: all I want to know is what most people would expect? like what does windows do by default? that's a good bet
(16,27,46) atodorov: rtcm: I'm just being told that new Windows releases use yet another layout by default, which is like phonetic but with some characters in new places and people don't like that
(16,27,53) atodorov: my safe bet goes to bg+phonetic
(16,29,05) rtcm: ok, thanks
{% endblockquote %}

It is a rare occasion when you get to make a decision that affects a large group
of people and I hope you don't hate me for that! 

Do you want to see more Fedora Test Days happening in Sofia? Join me and I will
organize some more!
