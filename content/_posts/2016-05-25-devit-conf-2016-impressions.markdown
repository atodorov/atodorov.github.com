Title: DEVit Conf 2016
date: 2016-05-25 16:01
comments: true
Tags: fedora.planet, events
twitter_image: images/devit2016.jpg
og_image: images/devit2016.jpg

It's been another busy week after [DEVit conf](http://devitconf.org/) took place in
Thessaloniki. Here are my impressions.

![DEVit 2016](/images/devit2016.jpg "DEVit 2016")


Pre-conference
--------------

[TechMinistry](http://techministry.gr) is Thessaloniki's hacker space which
is hosted at a central location, near major shopping streets.
I've attended an
[Open Source Wednesday](http://discourse.techministry.gr/t/18-05-2016-19-30-open-source-wednesday/67)
meeting. From the event description I thought that
there was going to be a discussion about getting involved with
Firefox. However that was not the case.
Once people started coming in they formed organic groups and
started discussing various topics on their own.

I was also shown their 3D printer which IMO is the most precise of 3D printers
I've seen so far. Imagine what it would be like to click *Print*, sometime
in the future, and have your online orders appear on your desk over night.
That would be quite cool!

I've met with [Christos Bacharakis](https://twitter.com/bacharakis), a Mozilla
representative for Greece, who gave me some goodies for my students at HackBulgaria!

On Thursday I spent the day merging pull requests for
[MrSenko/pelican-octopress-theme](https://github.com/MrSenko/pelican-octopress-theme)
and attended the DEVit Speakers dinner at
[Massalia](https://www.facebook.com/massaliathessaloniki/).
Food and drinks were very good and I even found a new recipe for mushrooms with
ouzo, of which I think I had a bit too many :).

I was also told that *"a full stack developer is a developer who can introduce
a bug to every layer of the software stack"*. I can't agree more!


DEVit
-----

The conference day started with a huge delay due to long queues for registration.
The fist talk I attended, and the best one IMO was
[Need It Robust? Make It Fragile!](https://www.youtube.com/watch?v=nCGBgI1MNwE&index=1&list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db)
by Yegor Bugayenko (watch the video). There he talked about two different approaches to writing
software: fail safe vs. fail fast.

He argues that when software is designed to
fail fast bugs are discovered earlier in the development cycle/software lifetime
and thus are easier to fix, making the whole system more robust and more stable.
On the other hand when software is designed to hide failures and tries to
recover auto-magically the same problems remain hidden for longer and when they
are finally discovered they are harder to fix. This is mostly due to the fact that
the original error condition is hidden and manifested in a different way which
makes it harder to debug.

Yegor made several examples, all of which are valid code, which he considers
bad practice. For example imagine we have a function that accepts a filename
as parameter:

    :::python
    def read_file_fail_safe(fname):
        if not os.path.exists(fname):
            return -1
    
        # read the file, do something else
        ...
        return bytes_read
    
    
    def read_file_fail_fast(fname):
        if not os.path.exists(fname):
            raise Exception('File does not exist')
    
        # read the file, do something else
        return bytes_read

In the first example `read_file_fail_safe` returns -1 on error. The trouble is
whoever is calling this method may not check for errors thus corrupting the
flow of the program further down the line. You may also want to collect metrics and
update your database with the number of bytes processed - this will totally
skew your metrics. C programmers out there will quickly remember at least
one case when they didn't check the return code for errors!

The second example `read_file_fail_fast` will raise an exception the moment
it encounters a problem. It's not its fault that the file doesn't exist and
there's nothing it can do about it, nor is its job to do anything about it.
Raising an exception will surface back to the caller and they will be notified
about the problem, taking appropriate actions to resolve it.

Yegor was also unhappy that many books teach fail safe and even IDEs (for Java)
generate fail safe boiler-plate code (need to check this)!
Indeed it is me who asks the first question
*Are there any tools to detect fail safe code patterns?* and it turns out there aren't
(for the majority of cases that is). If you happen to know such a tool
please post a link in the comments below.


I was a bit disappointed by the rest of the talks. They were all high-level
overviews IMO and didn't go deep technical. Last year was better. I also
wanted to attend the GitHub Patchwork workshop but looking at the agenda
it looked like this is for users who are starting with git and GitHub
(which I'm not).


The closing session of the day was
*"Real time front-end alchemy, or: capturing, playing, altering and encoding
video and audio streams, without servers or plugins!"* by Soledad Penades from
Mozilla. There she gave a demo about the latest and greatest in terms of
audio and video capturing, recording and mixing natively in the browser.
This is definitively very cool for apps in the audio/video space but I can
also imagine an application for us software testers.

Depending on computational and memory requirements you should be able to
record everything the user does in their browser (while on your website)
and send it back home when they want to report an error or contact support.
Definitely better than screenshots and having to go back and forth until
the exact steps to reproduce are established.



