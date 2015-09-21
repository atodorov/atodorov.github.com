---
layout: post
title: "Pedometer Bug in Samsung Gear Fit Smartwatch"
date: 2015-01-09 10:53
comments: true
categories: ['QA', 'Samsung']
---

<a style="float:left;display:inline-block;margin-right:10px;" href="http://www.amazon.com/gp/product/B00J4DY8RU/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00J4DY8RU&linkCode=as2&tag=atodorovorg-20&linkId=RNJGVYUTOOJFGWOU">
<img src="/images/samsung/gear_fit.jpg" />
</a>
<sub>
Image source [Pocketnow](http://pocketnow.com/2014/05/02/samsung-gear-fit-review-pre-buttal-video)
<sub>


Recently I've been playing around with a
<a href="http://www.amazon.com/gp/product/B00J4DY8RU/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00J4DY8RU&linkCode=as2&tag=atodorovorg-20&linkId=RNJGVYUTOOJFGWOU">Samsung Gear Fit</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B00J4DY8RU" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
and while the hardware seems good I'm a bit disapointed on the software side.
There is at least one bug which is clearly visible - **pedometer counts calories twice
when it's on and exercise mode is started**.


How to test:

* Start the *Pedometer* app and record any initial readings;
* Walk a fixed distance and at the end record all readings;
* Now go back to the *Exercise* app and select a *Walking*
exercise from the menu. Tap *Start*;
* Walk back the same distance/road as before. At the end of the journey
stop the walking exercise and record all readings.

Expected results:

At the end of the trip I expect to see roughly the same calories burned
for both directions.

Actual results:

The return trip counted twice as many calories compared to the forward trip.
Here's some actual data to prove it:

{% codeblock %}
+--------------------------+----------+----------------+---------+-------------+---------+
|                          | Initial  | Forward trip   |         | Return trip |         |
|                          | Readings | Pedometer only |  Delta  | Pedometer & |  Delta  |
|                          |          |                |         | Exercise    |         |
+--------------------------+----------+----------------+---------+-------------+---------+
|              Total Steps | 14409 st | 14798 st       | 389 st  | 15246 st    | 448 st  |
+--------------------------+----------+----------------+---------+-------------+---------+
|           Total Distance | 12,19 km | 12,52 km       | 0,33 km | 12,90 km    | 0,38 km |
+--------------------------+----------+----------------+---------+-------------+---------+
| Cal burned via Pedometer |  731 Cal |  751 Cal       | 20 Cal  |  772 Cal    | 21 Cal  |
+--------------------------+----------+----------------+=========+-------------+=========+
| Cal burned via Exercise  |  439 Cal |  439 Cal       | 0       |  460 Cal    | 21 Cal  |
+--------------------------+----------+----------------+---------+-------------+=========+
|    Total calories burned | 1170 Cal | 1190 Cal       | 20 cal  | 1232 Cal    | 42 Cal  |
+--------------------------+----------+----------------+=========+-------------+=========+
{% endcodeblock %}

**Note:** Data values above were taken from Samsung's *S Health* app which is easier to work with
instead of the Gear Fit itself.

The problem is that both apps are accessing the sensor simultaneously and not aware of each other.
In theory it should be relatively easy to block access of one app while the other is running but
that may not be so easy to implement on the limited platform the Gear Fit is.




