---
layout: post
Title: Speeding up Celery Backends, Part 1
date: 2014-11-05 15:20
comments: true
Tags: Python, Django, QA
---

I'm working on an application which fires a lot of Celery tasks - the more
the better! Unfortunately Celery backends seem to be rather slow :(.
Using the [celery_load_test.py](https://gist.github.com/atodorov/0156cc41491a5e1ff953)
command for Django I was able to capture some metrics:

* Amazon SQS backend: 2 or 3 tasks/sec
* Filesystem backend: 2000 - 2500 tasks/sec
* Memory backend: around 3000 tasks/sec

Not bad but I need in the order of 10000 tasks created per sec!
The other noticeable thing is that memory backend isn't much faster compared to
the filesystem one! NB: all of these backends actually come from the kombu package.

Why is Celery slow ?
--------------------

Using `celery_load_test.py` together with 
[cProfile](/blog/2014/11/05/performance-profiling-in-python-with-cprofile/) I
was able to pin-point some problematic areas:

* `kombu/transports/virtual/__init__.py`: class Channel.basic_publish() - does
self.encode_body() into base64 encoded string. Fixed with custom transport backend
I called fastmemory which redefines the body_encoding property:

        :::python
        @cached_property
        def body_encoding(self):
            return None

* Celery uses json or pickle (or other) serializers to serialize the data.
While json yields between 2000-3000 tasks/sec, pickle does around 3500 tasks/sec.
Replacing with a custom serializer which just returns
the objects (since we read/write from/to memory) yields about 4000 tasks/sec tops:

        :::python
        from kombu.serialization import register
        
        def loads(s):
            return s
        
        def dumps(s):
            return s
        
        register('mem_serializer', dumps, loads,
                content_type='application/x-memory',
                content_encoding='binary')

* `kombu/utils/__init__.py`: def uuid() - generates random unique identifiers
which is a slow operation. Replacing it with `return "00000000"` boosts performance
to 7000 tasks/sec.

It's clear that a constant UUID is not of any practical use but serves well to illustrate
how much does this function affect performance. 

**Note:**
Subsequent executions of `celery_load_test` seem to report degraded performance even with
the most optimized transport backend. I'm not sure why is this. One possibility is the random
UUID usage in other parts of the Celery/Kombu stack which drains entropy on the system and
generating more random numbers becomes slower. If you know better please tell me!

I will be looking for a better understanding
of these IDs in Celery and hope to be able to produce a faster uuid() function. Then I'll be
exploring the transport stack even more in order to reach the goal of 10000 tasks/sec.
If you have any suggestions or pointers please share them in the comments.

