---
layout: post
Title: Bug in the Fridge
date: 2013-03-29 15:09
comments: true
categories: ['QA']
---

<img src="/images/liebherr_kbgb_3864.jpg" alt="Liebherr KBGB 3864" style="float:left; margin-right: 20px;" />

Once you've been into
<a target="_blank" href="http://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-keywords=quality%20assurance&linkCode=ur2&rh=i%3Aaps%2Ck%3Aquality%20assurance&sprefix=quality%20ass%2Caps%2C273&tag=atodorovorg-20&url=search-alias%3Daps">Quality Assurance</a><img src="https://www.assoc-amazon.com/e/ir?t=atodorovorg-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
for 5+ years you start to notice [bugs everywhere](/blog/categories/qa/)
and develop a sixth sense for it. Today I found a bug in my
<a target="_blank" href="http://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-keywords=liebherr&linkCode=ur2&rh=n%3A2619525011%2Ck%3Aliebherr&sprefix=Liebherr%2Caps%2C273&tag=atodorovorg-20&url=search-alias%3Dappliances">Liebherr</a><img src="https://www.assoc-amazon.com/e/ir?t=atodorovorg-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
KBGB 3864 refrigerator, caused by what looks like a race-condition.

This appliance starts beeping in case the door is left open for more than 60 seconds.
The alarm stops if door is closed or can be muted manually while the door is still open.

The Bug
-------

It happened so that I had the door open for nearly one minute and as it was closing 
I heard a beep. This time however the beeping didn't stop after the door had closed.
The alarm continued beeping with the door closed so I tried to re-open and close it again.
It didn't stop! I had to open the door and manually mute the alarm for it to stop. 

<div style="display:block; clear:both;">&nbsp;</div>

The Root Cause
--------------

While not entirely sure, I think the reason for this malfunction
was a race-condition. The alarm went on at nearly the same time when the 
controlling timer should have gone off (when closing the door).

Steps To Reproduce
------------------

I tried reproducing several times afterwards by opening and closing the door
at the last possible moment. I used a stop-watch to time my actions. However
I wasn't able to reproduce twice. Every time I tried, there was only one single
beep as the door was closing and no more.

I guess then, like we say in QE, *WORKS FOR ME*!





