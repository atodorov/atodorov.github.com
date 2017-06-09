---
layout: post
Title: Performance test of MD5, SHA1, SHA256 and SHA512
Headline: and BLAKE2 on Python 2.7 and 3.6
date: 2013-02-05 10:33
comments: true
Tags: Python, performance testing, QA
Slug: performance-test-md5-sha1-sha256-sha512
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

    :::python test.py
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

If you are interested in Performance Testing checkout the
<a target="_blank" href="http://www.amazon.com/s/ref=as_li_ss_tl?_encoding=UTF8&camp=1789&creative=390957&field-keywords=performance%20testing&linkCode=ur2&rh=n%3A283155%2Ck%3Aperformance%20testing&sprefix=performance%20testing%2Caps%2C270&tag=atodorovorg-20&url=search-alias%3Dstripbooks&linkId=UVEZLZJOVYOCVGOT">performance testing books on Amazon</a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=ur2&o=1" width="1" height="1" border="0" style="border:none !important; margin:0px !important;" />.

As always I’d love to hear your thoughts and feedback. Please use the comment form below.

Python 2.7 vs. 3.6 and BLAKE2
-----------------------------

**UPDATE: added on June 9th 2017**

After request from my reader *refi64* I've tested this again between different
versions of Python and included a few more hash functions. The test data is the same,
the test script was slightly modified for Python 3:

    :::python test3.py
    import timeit
    
    print (timeit.repeat(
    """
    import hashlib
    for line in url_paths:
    #    h = hashlib.md5(line).hexdigest()
    #    h = hashlib.sha1(line).hexdigest()
    #    h = hashlib.sha256(line).hexdigest()
    #    h = hashlib.sha512(line).hexdigest()
    #    h = hashlib.blake2b(line).hexdigest()
        h = hashlib.blake2s(line).hexdigest()
    """
    ,
    """
    url_paths = [l.encode('utf8') for l in open('urls.txt', 'r').readlines()]
    """,
    repeat=3, number=1000))

Test was repeated 3 times for each hash function and the best time was taken into account.
The test was performed on a recent Fedora 26 system. The results are as follows:

    Python 2.7.13
    
    MD5     [13.94771409034729, 13.931367874145508, 13.908519983291626]
    SHA1    [15.20741891860962, 15.241390943527222, 15.198163986206055]
    SHA256  [17.22162389755249, 17.229840993881226, 17.23402190208435]
    SHA512  [21.557533979415894, 21.51376700401306, 21.522911071777344]
    
    
    Python 3.6.1
    
    MD5     [11.770181038000146, 11.778772834999927, 11.774679265000032]
    SHA1    [11.5838599839999, 11.580340686999989, 11.585769942999832]
    SHA256  [14.836309305999976, 14.847088003999943, 14.834776135999846]
    SHA512  [19.820048629999746, 19.77282728099999, 19.778471210000134]
    
    BLAKE2b [12.665497404000234, 12.668979115000184, 12.667314543999964]
    BLAKE2s [11.024885618000098, 11.117366972000127, 10.966767880999669]

* Python 3 is faster than Python 2
* SHA1 is a bit faster than MD5, maybe there's been some optimization
* BLAKE2b is faster than SHA256 and SHA512
* BLAKE2s is the fastest of all functions

**Note:** BLAKE2b is optimized for 64-bit platforms, like mine and I thought it
will be faster than BLAKE2s (optimized for 8- to 32-bit platforms) but that's
not the case. I'm not sure why is that though. If you do, please let me know
in the comments below!
