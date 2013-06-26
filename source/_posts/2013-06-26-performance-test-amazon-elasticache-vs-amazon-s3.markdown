---
layout: post
title: "Performance test: Amazon ElastiCache vs Amazon S3"
date: 2013-06-26 21:22
comments: true
categories: ['Amazon', 'Django', 'S3', 'ElastiCache', 'QA', 'performance-testing']
---

Which Django cache backend is faster? Amazon ElastiCache or Amazon S3 ?

Previously I've mentioned about
[using Django's cache to keep state between HTTP requests](/blog/2013/06/19/django-tips-using-cache-for-stateful-http/).
In my demo described there I was using [django-s3-cache](http://github.com/atodorov/django-s3-cache).
It is time to move to production so I decided to measure the performance difference between the two
cache options available at Amazon Web Services.


Test infrastructure
-------------------

* One Amazon S3 bucket, located in US Standard (aka US East) region;
* One Amazon ElastiCache cluster with one Small Cache Node (cache.m1.small) with Moderate I/O capacity;
* One Amazon Elasticache cluster with one Large Cache Node (cache.m1.large) with High I/O Capacity.

Test Scenario
-------------

The test platform is Django. I've created a
[skeleton project](https://github.com/atodorov/Amazon-ElastiCache-vs-Amazon-S3-Django)
with only `CACHES` settings
defined and necessary dependencies installed. A file called `test.py` holds the
test cases, which use the standard timeit module. The object which is stored in cache
is very small - it holds a phone/address identifiers and couple of user made selections.
The code looks like this:

{% codeblock lang:python %}
import timeit

s3_set = timeit.Timer(
"""
for i in range(1000):
    s3_cache.set(i, MyObject)
"""
,
"""
from django.core import cache

s3_cache = cache.get_cache('default')

MyObject = {
    'from' : '359123456789',
    'address' : '6afce9f7-acff-49c5-9fbe-14e238f73190',
    'hour' : '12:30',
    'weight' : 5,
    'type' : 1,
}
"""
)

s3_get = timeit.Timer(
"""
for i in range(1000):
    MyObject = s3_cache.get(i)
"""
,
"""
from django.core import cache

s3_cache = cache.get_cache('default')
"""
)

### skip ###
{% endcodeblock %}


Tests were executed from the Django shell on my laptop:

{% codeblock lang:python %}

$ ./manage.py shell
Python 2.6.6 (r266:84292, Oct 12 2012, 14:23:48) 
[GCC 4.4.6 20120305 (Red Hat 4.4.6-4)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from test import *
>>>
>>>
>>>
>>> s3_set.repeat(repeat=3, number=1)
[534.49202704429626, 515.13989496231079, 515.26534104347229]
>>>
>>> ecs_set.repeat(repeat=3, number=1)
[3.1153659820556641, 3.102524995803833, 3.1101429462432861]
>>>
>>> ecl_set.repeat(repeat=3, number=1)
[3.1070160865783691, 3.1004979610443115, 3.1082391738891602]
>>>
>>>
>>>
>>> s3_get.repeat(repeat=3, number=1)
[354.0339789390564, 383.1578528881073, 371.23516583442688]
>>>
>>> ecs_get.repeat(repeat=3, number=1)
[3.0982329845428467, 3.1075088977813721, 3.1198301315307617]
>>>
>>> ecl_get.repeat(repeat=3, number=1)
[3.1206800937652588, 3.0972812175750732, 3.1136119365692139]


{% endcodeblock %}

Results
--------

As expected ElastiCache is much faster compared to S3. However the difference
between the two ElastiCache node types is subtle. I will stay with the smallest
possible node to minimize costs.

Depending on your objects size or how many set/get operations you perform per
second you may need to go with the larger nodes. Just test it!


It surprised me how slow django-s3-cache is. A quick look at the code
of the two backends shows some differences. The one I immediately see is that
for every cache key django-s3-cache creates an sha1 hash which is used as the
storage file name. This was modeled after the filesystem backend but I think the
design is wrong. 

Another one is that django-s3-cache time-stamps all objects and uses pickle to serialize them. 
I wonder if it can't just write them as binary blobs directly. There's definitely lots
of room for improvement of django-s3-cache. I will let you know my findings once I
get to it. 
