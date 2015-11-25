---
layout: post
Title: Performance test of MD5, SHA1, SHA256 and SHA512
date: 2013-02-05 10:33
comments: true
Tags: 'Python', 'performance testing', 'QA'
---

A few months ago I wrote
[django-s3-cache](https://github.com/atodorov/django-s3-cache).
This is Amazon Simple Storage Service (S3) cache backend for Django
which uses hashed file names.
django-s3-cache uses `sha1` instead of `md5` which appeared to be
faster at the time. I recall that my testing wasn't very robust so I did another
round.

Test Data
---------

The file [urls.txt](http://s3.amazonaws.com/atodorov/blog/urls.txt.gz)
contains 10000 unique paths from the [dif.io](http://www.dif.io)
website and looks like this:

    /updates/Django-1.3.1/Django-1.3.4/7858/
    /updates/delayed_paperclip-2.4.5.2 c23a537/delayed_paperclip-2.4.5.2/8085/
    /updates/libv8-3.3.10.4 x86_64-darwin-10/libv8-3.3.10.4/8087/
    /updates/Data::Compare-1.22/Data::Compare-Type/8313/
    /updates/Fabric-1.4.0/Fabric-1.4.4/8652/


Test Automation
---------------

I used the standard [timeit](http://docs.python.org/2/library/timeit.html)
module in Python.

{% codeblock test.py lang:python %}
#!/usr/bin/python

import timeit

t = timeit.Timer(
"""
import hashlib
for line in url_paths:
    h = hashlib.md5(line).hexdigest()
#    h = hashlib.sha1(line).hexdigest()
#    h = hashlib.sha256(line).hexdigest()
#    h = hashlib.sha512(line).hexdigest()
"""
,
"""
url_paths = []
f = open('urls.txt', 'r')
for l in f.readlines():
    url_paths.append(l)
f.close()
"""
)

print t.repeat(repeat=3, number=1000)
{% endcodeblock %}

Test Results
------------

The main statement hashes all 10000 entries one by one. This statement is
executed 1000 times in a loop, which is repeated 3 times. I have Python 2.6.6
on my system. After every test run the system was rebooted.
Execution time in seconds is available below.

    MD5     10.275190830230713, 10.155328989028931, 10.250311136245728
    SHA1    11.985718965530396, 11.976419925689697, 11.86873197555542
    SHA256  16.662450075149536, 21.551337003707886, 17.016510963439941
    SHA512  18.339390993118286, 18.11187481880188,  18.085782051086426


Looks like I was wrong the first time! MD5 is still faster but not that much.
I will stick with SHA1 for the time being.

As always I’d love to hear your thoughts and feedback. Please use the comment form below.
