---
layout: post
Title: Bug in Nokia software shows wrong caller ID
date: 2013-03-19 09:57
comments: true
categories: ['Nokia', 'QA']
---

During the past month one of my cell phones,
<a target="_blank" href="http://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-keywords=Nokia&linkCode=ur2&tag=atodorovorg-20&url=search-alias%3Daps">Nokia</a><img src="https://www.assoc-amazon.com/e/ir?t=atodorovorg-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
<a href="http://www.amazon.com/gp/product/B001SEAOC6/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B001SEAOC6&linkCode=as2&tag=atodorovorg-20">5800 XpressMusic</a><img src="http://www.assoc-amazon.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B001SEAOC6" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
, was not showing the caller name when a friend was calling.
The number in the contacts list was correct but the name wasn't showing,
nor the custom assigned ringing tone. It turned out to be a bug!

The story behind this is that accidentally the same number was saved again
in the contacts list, but without a name assigned to it.
The software was matching the later one, so no custom ringing tone,
no name shown. Removing the duplicate entry fixed the issue. Software version of this
phone is

    v 21.0.025
    RM-356
    02-04-09

I wondered what will happen with multiple duplicates and if this was fixed in a later
software version so I tested with another phone,
<a href="http://www.amazon.com/gp/product/B002RXEI6U/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B002RXEI6U&linkCode=as2&tag=atodorovorg-20">Nokia 6303</a><img src="http://www.assoc-amazon.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B002RXEI6U" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />.
Software version is

    V 07.10
    25-03-10
    RM-638


* Step 0 - add the number to the contacts list, with name `Buddy 1`
* Step 1 - add the same number to the contacts, with **empty name**.
**Result**: You get a warning this number is already present for `Buddy 1`!
When receiving a call, `Buddy 1` is displayed.
* Step 2 - edit the empty name contact and change the name to `Buddy 2`.
**Result**: when receiving a call `Buddy 2` is displayed.
* Step 3 - add the same number again, with name `Buddy 0`. This is the latest entry
but it is sorted before the previous two (this is important).
**Result**: You get a warning that this number is already present for `Buddy 1` and `Buddy 2`.
When receiving a call `Buddy 0` is displayed.


**Summary**: so it looks like Nokia fixed the issue with empty names, by simply ignoring them
but when multiple duplicate contacts are available it displays the name of the last entered in the
contact list, independent of name sort order.

<del>
Later today or tomorrow I will test on 
<a href="http://www.amazon.com/gp/product/B005MOW7S2/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B005MOW7S2&linkCode=as2&tag=atodorovorg-20">Nokia 700</a><img src="http://www.assoc-amazon.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B005MOW7S2" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
which runs Symbian OS and update this post with more results.
</del>

**Updated on 2013-03-19 23:50**

Finally managed to test on
<a href="http://www.amazon.com/gp/product/B005MOW7S2/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B005MOW7S2&linkCode=as2&tag=atodorovorg-20">Nokia 700</a><img src="http://www.assoc-amazon.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B005MOW7S2" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />.
Software version is:

    Release
    Nokia Belle Feature pack 1
    Software version
    112.010.1404
    Software version date
    2012-03-30
    Type
    RM-670

**Result**: If a duplicate contact entry is present it doesn't matter if the name is empty or not.
Both times no name was displayed when receiving a call. Looks like Nokia is not paying attention to
regressions at all.

Android and iPhone
------------------

I don't own any
<a target="_blank" href="http://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-keywords=Android&linkCode=ur2&tag=atodorovorg-20&url=search-alias%3Delectronics">Android</a><img src="https://www.assoc-amazon.com/e/ir?t=atodorovorg-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
or
<a target="_blank" href="http://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-keywords=iPhone&linkCode=ur2&rh=n%3A172282%2Ck%3AiPhone&tag=atodorovorg-20&url=search-alias%3Delectronics">iPhone</a><img src="https://www.assoc-amazon.com/e/ir?t=atodorovorg-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
devices so I'm not able to test on them. If you have one, please let me know if this bug is still present
and how does the software behave when multiple contacts share the same number or have empty names! Thanks!
