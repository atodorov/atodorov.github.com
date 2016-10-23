Title: Animate & Automate
Headline: a testing technique by MentorMate
date: 2016-10-24 00:01
comments: true
Tags: QA

Recently I've attended a presentation by MentorMate where they talked about
testing CSS animations (
[video in Bulgarian](https://www.youtube.com/watch?v=MIxzzfFBR8o&list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db&index=6)
). The software under test was an ad tech SDK which
provides CSS based animations to mobile apps and games. The content
is displayed inside a webview and they had to make sure animations were
working correctly on different OS and devices.

Analyzing the content (aka getting to know the domain) they figured out
in reality there were about 20 basic movements and transformations. So the
problem was reduced to "How do we test these 20 basic movements under
various OSes and devices" or "How do we verify that basic CSS transformations
are supported under different versions and flavors of the OS"?

Their test bed included hand crafted web pages with each basic movement
and then several ones with more complex animations (aka integration testing).
The idea was to load
these pages under different devices and inspect whether or not the animations
were visualized properly.

A test script (aka their testing framework) was constantly recording the
coordinates of the elements under test to verify that they were really animated.
The idea was to use a sample rate of 20ms and expect at lest 20 different changes
to the element under test. Coordinates along with color and gradient were recorded
and then returned back and analyzed to report a PASS or FAIL result.

This simplistic framework has limitations of course. It is not currently checking
the boundaries of where the elements are rendered on the screen. Thus if everything
else works as expected this will be a false positive result. On their slides
this can be seen at [23:10](https://youtu.be/MIxzzfFBR8o?t=23m10s).

As a side note the entire effort took about 2 days, including research and preparing
the test content.

I really like the back to basics approach here and the simplistic framework that
MentorMate came up with. Sure it misses some problems but for that particular case
it is good enough, easy and fast to implement.

