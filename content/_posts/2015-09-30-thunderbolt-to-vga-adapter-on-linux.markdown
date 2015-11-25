---
layout: post
Title: Thunderbolt to VGA adapter on Linux
date: 2015-09-30 11:59
comments: true
Tags: 'Mac', 'RHEL', 'fedora.planet'
---

I've previously written about my
[Thunderbolt to Ethernet adapter working on Linux](blog/2015/05/04/thunderbolt-to-ethernet-adapter-on-linux/)
despite claims that it should not. Recently I've used my MacBook to do a presentation
and the Thunderbolt to VGA adapter worked well enough.

It was an Acer adapter but I have no more details b/c it wasn't mine.

Before the event I've tested it and it worked so on the day of the event I've
freshly rebooted my laptop to be sure no crashed processes or anything like that
was running and gave it a go.

First time I plugged in the MacBook everything worked like a charm. Then my computer was
unplugged and the lid closed, causing it to suspend. The second time I've plugged it in
I was told there was nothing showing on the projector so I quickly plugged the adapter out
and then back in. It worked more or less.

At the time I had LibreOffice Impress in presentation
mode but I did see ABRT detecting a kernel problem. When my slides popped up the text
on the first one was mostly missing but the rest were ok!

Mind you I'm still running [RHEL 7 on my MacBook Air](/blog/categories/mac/). The above is
with kernel-3.10.0-229.14.1.el7.x86_64.
