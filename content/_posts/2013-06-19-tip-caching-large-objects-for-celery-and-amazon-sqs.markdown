---
layout: post
Title: Tip: Caching Large Objects for Celery and Amazon SQS 
date: 2013-06-19 14:29
comments: true
Tags: tips, Amazon, SQS, cloud
---

Some time ago a guy called Matt
[asked](https://groups.google.com/forum/?fromgroups=#!topic/celery-users/RFAuGjZwtmg)
about passing large objects through their messaging queue. They were switching from
RabbitMQ to Amazon SQS which has a limit of 64K total message size.

Recently I've made some changes in [Difio](http://www.dif.io) which require passing
larger objects as parameters to a Celery task. Since Difio is also using SQS I faced the
same problem. Here is the solution using a cache back-end: 

    :::python
    from celery.task import task
    from django.core import cache as cache_module
    
    def some_method():
        ... skip ...
    
        task_cache = cache_module.get_cache('taskq')
        task_cache.set(uuid, data, 3600)
    
        handle_data.delay(uuid)
    
        ... skip ...
    
    @task
    def handle_data(uuid):
        task_cache = cache_module.get_cache('taskq')
        data = task_cache.get(uuid)
    
        if data is None:
            return
    
        ... do stuff ...

Objects are persisted in a secondary cache back-end, not the default one, to avoid
accidental destruction. `uuid` parameter is a string.

Although the objects passed are smaller than 64K I haven't seen any issues
with this solution so far. Let me know if you are using something similar in your code
and how it works for you. 


