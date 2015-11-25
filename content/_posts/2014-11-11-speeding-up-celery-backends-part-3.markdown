---
layout: post
Title: Speeding Up Celery Backends, Part 3
date: 2014-11-11 15:59
comments: true
Tags: 'Python', 'Django', 'QA'
---

In the second part of this article we've seen 
[how slow Celery actually is](/blog/2014/11/07/speeding-up-celery-backends-part-2/).
Now let's explore what happens inside and see if we can't speed things up.

I've used [pycallgraph](http://pycallgraph.slowchop.com/en/latest/) to create
call graph visualizations of my application. It has the nice feature to also show
execution time and use different colors for fast and slow operations.

Full command line is:

    pycallgraph -v --stdlib --include ... graphviz -o calls.png -- ./manage.py celery_load_test

where the `--include` is used to limit the graph to a particular Python module(s).

General findings
----------------

![call graph](/images/celery/general.png "call graph")

* The first four calls is where most of the time is spent as seen on the picture. 
* As it seems most of the slow down comes from Celery itself, not the underlying messaging
transport Kombu (not shown on picture)
* `celery.app.amqp.TaskProducer.publish_task` takes half of the execution time of
`celery.app.base.Celery.send_task`
* `celery.app.task.Task.delay` directly executes `.apply_async` and can be skipped if one
rewrites the code.


More findings
-------------

In `celery.app.base.Celery.send_task` there is this block of code:

    349         with self.producer_or_acquire(producer) as P:
    350             self.backend.on_task_call(P, task_id)
    351             task_id = P.publish_task(
    352                 name, args, kwargs, countdown=countdown, eta=eta,
    353                 task_id=task_id, expires=expires,
    354                 callbacks=maybe_list(link), errbacks=maybe_list(link_error),
    355                 reply_to=reply_to or self.oid, **options
    356             )


`producer` is always None because delay() doesn't pass it as argument.
I've tried passing it explicitly to apply_async() as so:

    from djapp.celery import *

    # app = debug_task._get_app() # if not defined in djapp.celery
    producer = app.amqp.producer_pool.acquire(block=True)
    debug_task.apply_async(producer=producer)


However this doesn't speedup anything. If we replace the above code block like this:

    349         with producer as P:

it blows up on the second iteration because producer and its channel is already None !?!

If you are unfamiliar with the with statement in Python please read
[this article](http://effbot.org/zone/python-with-statement.htm). In short the with statement is
a compact way of writing try/finally. The underlying `kombu.messaging.Producer` class does a
`self.release()` on exit of the with statement.


I also tried killing the with statement and using producer directly but with limited success. While
it was not released(was non None) on subsequent iterations the memory usage grew much more and there
wasn't any performance boost.

Conclusion
----------

The with statement is used throughout both Celery and Kombu and I'm not at all sure if
there's a mechanism for keep-alive connections. My time constraints are limited and I'll probably
not spend anymore time on this problem soon.

Since my use case involves task producer and consumers on localhost I'll try to workaround the
current limitations by using Kombu directly 
(see [this gist](https://gist.github.com/atodorov/2bc1fcd34531ad260ed7)) with a transport that
uses either a UNIX domain socket or a name pipe (FIFO) file.


