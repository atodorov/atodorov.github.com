Title: Don't Upgrade Galaxy S5 to Android 6.0
Headline: or shipping buggy software like a boss
date: 2016-06-09 00:10
comments: true
Tags: QA, fedora.planet, Samsung
og_image: images/samsung/lockscreen_bug.jpg
twitter_image: images/samsung/lockscreen_bug.jpg

Samsung is shipping out buggy software like a boss, no doubt about it.
I've written a bit about [their bugs]({tag}Samsung) previously.
However I didn't expect them to release Android 6.0.1 and render my
[Galaxy S5](http://amzn.to/1tiiqze) completely useless with respect
to the feature I use the most.

![Lockscreen](/images/samsung/lockscreen_bug.jpg "Lockscreen")

Tell me the weather for Brussels
---------------------------------

So on Monday I've let Android upgrade to 6.0.1 to be completely surprised
that the lockscreen shows the weather report for Brussels, while
I'm based in Sofia. I've checked *AccuWeather* (I did go to
[Brussels earlier this year]({filename}2016-02-02-fosdem-2016-report.markdown))
but it displayed only Sofia and Thessaloniki. To get rid of this widget
go to `
Settings -> Lockscreen -> Additional information` and turn it off!

I think this weather report comes from GPS/Location based data, which I
have turned off by default but did use a while back ago. After turning
the widget off and back on it didn't appear on the lockscreen. I suspect
they fall back to showing the last good known value when data is missing
instead of handling the error properly.

Apps are gone
--------------

Some of my installed apps are missing now. So far I've noticed that the
*Gallery* and *S Health* icons have disappeared from my homescreen. I think
*S Health* came from Samsung's app store but still they shouldn't have removed
it silently. Now I wonder what happened to my data.

I don't see why *Gallery* was removed though. The only way to view pictures
is to use the camera app preview functionality which is kind of grose.

Grayscale in powersafe mode is gone
-----------------------------------

The killer feature on these higher end Galaxy devices is the *Powersafe mode*
and *Ultra Powersafe mode*. I use them a lot and by default have my phone in
*Powersafe mode* with grayscale colors enabled. It is easier on the eyes and
also safes your battery.

**NOTE:** grayscale colors don't affect some displays but these devices use
AMOLED screens which need different amounts of power to display different
colors. More black means less power required!

After the upgrade grayscale is no more. There's not even an on/off switch.
I've managed to find a workaround though. First you need to enable developer mode
by tapping 7 times on `About device -> Build number`. Then go to
`Settings -> Developer options`, look for the `Hardware Accelerated Rendering`
section and select `Simulate Color Space -> Monochromacy`! This is a bit ugly
hack and doesn't have the convenience of turning colors on/off by tapping
the quick Powersafe mode button at the top of the screen!


It looks like Samsung didn't think this upgrade well enough or didn't test it
well enough ? In my line of work (installation and upgrade testing) I've rarely
seen such a big blunder. Thanks for reading and happy testing!
