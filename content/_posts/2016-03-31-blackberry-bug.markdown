Title: Time Calculation bug in BlackBerry Z10
date: 2016-03-31 16:34
comments: true
Tags: QA
og_image: images/bbz10_calls_bug_small.png
twitter_image: images/bbz10_calls_bug_small.png

![BlackBerry Z10 bug](/images/bbz10_calls_bug.png "BlackBerry Z10 bug")

I thought BlackBerry 10 is dead but apparently they still provide updates
and introduce new bugs :). This one happened a few days ago with
Software Release 10.3.2.2474. As you can see the time calculations are totally
wrong!

The current
time is 12:45, March 28th. The last call is reported as *5 minutes ago*
but its time stamp is 3 and a half hours ago!

The second call is reported as *11 minutes ago* but in reality it is
3 days ago. I'm not sure about the time stamp but that is probably wrong
as well.

The reason for this IMO is their design to have a fixed start of the epoch
for every OS release - probably the build time of the release. When the OS
is fully booted and connected to network it synchronizes with time servers
and updates the local time. This of course fails in case of no WiFi, no
cellular data or if automatic time synchronization is turned off!

The result is that every object (calls, images, etc) which has a time stamp
attached to it gets an incorrect value. Maybe some of these are recalculated
back to the current time, once it is synchronized, and others probably not.
Otherwise I'd expect all calls to be reported way back in time!


For more information about time related bugs checkout
[Tom Scott's Why 1/1/1970 Bricks Your iPhone](https://www.youtube.com/watch?v=MVI87HzfskQ)
video and read my article
[Floating-point precision error with Ruby]({filename}2016-03-08-ruby-time-now-to_f.markdown).
