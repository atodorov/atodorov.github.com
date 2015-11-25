---
layout: post
Title: Speeding up Celery Backends, Part 2
date: 2014-11-07 15:48
comments: true
Tags: 'Python', 'Django', 'QA'
---

In the [first part](/blog/2014/11/05/speeding-up-celery-backends/) of this
post I looked at a few celery backends and discovered they didn't meet my needs.
Why is the Celery stack slow? How slow is it actually?

How slow is Celery in practice
------------------------------

* Queue: 500`000 msg/sec
* Kombu:  14`000 msg/sec
* Celery:  2`000 msg/sec


Detailed test description
--------------------------

There are three main components of the Celery stack: 

* Celery itself
* Kombu which handles the transport layer
* Python Queue()'s underlying everything

Using the [Queue and Kombu tests](https://gist.github.com/atodorov/2bc1fcd34531ad260ed7)
run for 1 000 000 messages I got the following results:

* Raw Python Queue: Msgs per sec: 500`000
* Raw Kombu without Celery where `kombu/utils/__init__.py:uuid()` is set to return 0
    * with json serializer: Msgs per sec: 5`988
    * with pickle serializer: Msgs per sec: 12`820
    * with the custom mem_serializer from [part 1](/blog/2014/11/05/speeding-up-celery-backends/):
Msgs per sec: 14`492

**Note:** when the test is executed with 100K messages mem_serializer yielded
25`000 msg/sec then the performance is saturated. I've observed similar behavior 
with raw Python Queue()'s. I saw some cache buffers being managed internally to avoid OOM
exceptions. This is probably the main reason performance becomes saturated over a longer
execution.

* Using [celery_load_test.py](https://gist.github.com/atodorov/0156cc41491a5e1ff953) modified to
loop 1 000 000 times I got 1908.0 tasks created per sec.


Another interesting this worth outlining - in the kombu test there are these lines:
{% codeblock %}
with producers[connection].acquire(block=True) as producer:
    for j in range(1000000):
{% endcodeblock %}

If we swap them the performance drops down to 3875 msg/sec which is comparable with the
Celery results. Indeed inside Celery there's the same `with producer.acquire(block=True)`
construct which is executed every time a new task is published. Next I will be looking 
into this to figure out exactly where the slowliness comes from.
