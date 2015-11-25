---
layout: post
Title: Idempotent Django Email Sender with Amazon SQS and Memcache
date: 2013-12-11 23:29
comments: true
Tags: cloud, Amazon, SQS, Django, Python
---

Recently I wrote about my problem with
[duplicate Amazon SQS messages causing multiple emails](/blog/2013/12/06/duplicate-amazon-sqs-messages-cause-multiple-emails/)
for [Difio](http://www.dif.io). After considering several options and
feedback from 
[@Answers4AWS](https://twitter.com/atodorov_/status/409429840820199424)
I wrote a small decorator to fix this.

It uses the cache backend to prevent the task from executing twice
during the specified time frame. The code is available at
<https://djangosnippets.org/snippets/3010/>.

As stated on Twitter you should use Memcache (or ElastiCache) for this.
If using Amazon S3 with my
[django-s3-cache](https://github.com/atodorov/django-s3-cache) don't use the
`us-east-1` region because it is eventually consistent.

The solution is fast and simple on the development side and uses my existing
cache infrastructure so it doesn't cost anything more!

There is still a race condition between marking the message as processed
and the second check but nevertheless this should minimize the possibility of
receiving duplicate emails to an accepted level. Only time will tell though!
