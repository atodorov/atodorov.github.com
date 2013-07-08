---
layout: post
title: "Performance test: Amazon ElastiCache vs Amazon S3"
date: 2013-06-26 21:22
comments: true
categories: ['Amazon', 'Django', 'S3', 'ElastiCache', 'QA', 'performance testing', 'cloud']
---

Which Django cache backend is faster? Amazon ElastiCache or Amazon S3 ?

Previously I've mentioned about
[using Django's cache to keep state between HTTP requests](/blog/2013/06/19/django-tips-using-cache-for-stateful-http/).
In my demo described there I was using [django-s3-cache](http://github.com/atodorov/django-s3-cache).
It is time to move to production so I decided to measure the performance difference between the two
cache options available at Amazon Web Services.

**Update 2013-07-01**: my initial test may have been false since I had not configured
ElastiCache access properly. I saw no errors but discovered the issue today on another
system which was failing to store the cache keys but didn't show any errors either. 
I've re-run the tests and updated times are shown below.


Test infrastructure
-------------------

* One Amazon S3 bucket, located in US Standard (aka US East) region;
* One Amazon ElastiCache cluster with one Small Cache Node (cache.m1.small) with Moderate I/O capacity;
* One Amazon Elasticache cluster with one Large Cache Node (cache.m1.large) with High I/O Capacity;
* **Update:** I've tested both `python-memcached` and `pylibmc` client libraries for Django;
* **Update:** Test is executed from an EC2 node in the us-east-1a availability zone;
* **Update:** Cache clusters are in the us-east-1a availability zone.

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
    my_cache.set(i, MyObject)
"""
,
"""
from django.core import cache

my_cache = cache.get_cache('default')

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
    MyObject = my_cache.get(i)
"""
,
"""
from django.core import cache

my_cache = cache.get_cache('default')
"""
)

### skip ###
{% endcodeblock %}


Tests were executed from the Django shell <del>on my laptop</del>
on an EC2 instance in the us-east-1a availability zone. ElastiCache nodes
were freshly created/rebooted before test execution. S3 bucket had no objects.

{% codeblock lang:python %}

$ ./manage.py shell
Python 2.6.8 (unknown, Mar 14 2013, 09:31:22) 
[GCC 4.6.2 20111027 (Red Hat 4.6.2-2)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from test import *
>>> 
>>> 
>>> 
>>> s3_set.repeat(repeat=3, number=1)
[68.089607000350952, 70.806712865829468, 72.49261999130249]
>>> 
>>> 
>>> s3_get.repeat(repeat=3, number=1)
[43.778793096542358, 43.054368019104004, 36.19232702255249]
>>> 
>>> 
>>> pymc_set.repeat(repeat=3, number=1)
[0.40637087821960449, 0.3568730354309082, 0.35815882682800293]
>>> 
>>> 
>>> pymc_get.repeat(repeat=3, number=1)
[0.35759496688842773, 0.35180497169494629, 0.39198613166809082]
>>> 
>>> 
>>> libmc_set.repeat(repeat=3, number=1)
[0.3902890682220459, 0.30157709121704102, 0.30596804618835449]
>>> 
>>> 
>>> libmc_get.repeat(repeat=3, number=1)
[0.28874802589416504, 0.30520200729370117, 0.29050207138061523]
>>> 
>>> 
>>> libmc_large_set.repeat(repeat=3, number=1)
[1.0291709899902344, 0.31709098815917969, 0.32010698318481445]
>>> 
>>> 
>>> libmc_large_get.repeat(repeat=3, number=1)
[0.2957158088684082, 0.29067802429199219, 0.29692888259887695]
>>> 
{% endcodeblock %}

Results
--------

As expected ElastiCache is much faster (10x) compared to S3. However the difference
between the two ElastiCache node types is subtle. I will stay with the smallest
possible node to minimize costs. Also as seen, pylibmc is a bit faster compared to
the pure Python implementation. 

Depending on your objects size or how many set/get operations you perform per
second you may need to go with the larger nodes. Just test it!


<del>It surprised me how slow django-s3-cache is.</del>
The false test showed django-s3-cache to be 100x slower but new results are better.
10x decrease in performance sounds about right for a filesystem backed cache.

A quick look at the code
of the two backends shows some differences. The one I immediately see is that
for every cache key django-s3-cache creates an sha1 hash which is used as the
storage file name. This was modeled after the filesystem backend but I think the
design is wrong - the memcached backends don't do this.

Another one is that django-s3-cache time-stamps all objects and uses pickle to serialize them. 
I wonder if it can't just write them as binary blobs directly. There's definitely lots
of room for improvement of django-s3-cache. I will let you know my findings once I
get to it. 
