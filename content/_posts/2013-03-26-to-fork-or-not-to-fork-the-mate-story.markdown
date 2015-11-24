---
layout: post
Title: To fork or not to fork - the MATE story
date: 2013-03-26 10:46
comments: true
categories: 
---

!["MATE Desktop"](/images/MATE.png "MATE Desktop")

In the open source world
[forking](https://en.wikipedia.org/wiki/Fork_%28software_development%29)
is a common concept, largely endorsed by GitHub's fork & pull requests work-flow.
Forking a large and successful project and creating a new one, with its own
eco-system is rare though.

Recently I came across the [MATE](http://mate-desktop.org) desktop environment
which is a fork of GNOME 2. Even more interesting is that they forked lots of
standard GNOME [applications](http://mate-desktop.org/applications/) as well.
Being behind the [world's leading enterprise OS](http://www.redhat.com/products/enterprise-linux/)
where maintaining a private fork is sometimes necessary I wondered why MATE had to do this.

Here are some interesting responses from
[mate-dev](http://ml.mate-desktop.org/pipermail/mate-dev/2013-March/000090.html):

{% blockquote Stefano Karapetsas http://ml.mate-desktop.org/pipermail/mate-dev/2013-March/000091.html %}
Well, MATE is born in a time of fear, so Perberos forked almost all 
GNOME 2 applications. Currently, we are dropping a lot of packages to 
focus our effort on what we need really.
...
The main reason of this is to have a base set of apps in GTK 2. Another 
reason, most GNOME apps (like Evince) are suffering mockups that dont 
follow the traditional idea of MATE.

When MATE will be GTK3, we'll consider again if keeping or not such 
applications.
{% endblockquote %}

{% blockquote Michael Steenbeek http://ml.mate-desktop.org/pipermail/mate-dev/2013-March/000092.html %}
A similar question was also asked not long after the MATE forum was 
created, which was probably somewhere early in 2012. Steve Zesch 
answered that we would be sure that we wouldn't be affected by 
feature/UI choices of the GNOME developers, which we would have been if 
MATE relied on GNOME 3 applications. He used Caja as an example. Caja 
looked -of course- similar to Nautilus. It had some features Nautilus 3 
didn't, but the reverse was true as well. Nautilus 3 looked better, 
though, so it was not very surprising that we got (and get) this 
question. But Steve's example of Caja turned out to be pretty much spot 
on, when Nautilus 3.6 was released, and almost all of the changes were 
removed features (it was even described by a former GNOME developer as 
'vandalism'). Canonical decided to use 3.4 for Ubuntu 12.10, although 
the original plan was to include 3.6. Linux Mint forked 3.4 as Nemo.

And there's no good reason for this, as far as I can see. The interfaces 
of Gnome have always been simple enough not to be overwhelming for 
novice users, but at the same time powerful enough for the power users. 
Which is a fine - and rare - balance. They completely messed it up in 
Gnome 3. 
...
So although Gedit, Evince and GNOME Terminal are fine now, I doubt it's 
safe to assume they will stay that way. Especially since we've already 
seen what happened to the fallback mode of Gnome 3 (completely removed, 
although many people use it and Ubuntu's Unity depends on it) and 
Nautilus (vandalised).
...
Well, ok, that was a big rant. But to summarise my post (and Stefano's): 
it was a decision that had to be taken quickly, and from the integration 
and control viewpoint, it seems like was a good idea after all. 
Especially now many deprecated underlying technologies have been replaced.
{% endblockquote %}


{% blockquote Michael Steenbeek http://ml.mate-desktop.org/pipermail/mate-dev/2013-March/000095.html %}
Well, when two teams are maintaining applications with very little 
differences, that can be considered a waste of time and effort. It was 
very easy to say about the MATE applications as well, before we knew 
what GNOME would do to its applications. Now GNOME is removing more and 
more features from its applications and changing their GUI to a tablet 
interface, it turned to be the right decision.
{% endblockquote %}

