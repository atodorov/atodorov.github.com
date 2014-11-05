---
layout: post
title: "Performance Profiling in Python with cProfile"
date: 2014-11-05 14:40
comments: true
categories: ['Python', 'QA']
---

This is a quick reference on profiling Python applications with
[cProfile](https://docs.python.org/2/library/profile.html#module-cProfile):

    $ python -m cProfile -s time application.py

The output is sorted by execution time `-s time`

{% codeblock %}
     9072842 function calls (8882140 primitive calls) in 9.830 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    61868    0.575    0.000    0.861    0.000 abstract.py:28(__init__)
    41250    0.527    0.000    0.660    0.000 uuid.py:101(__init__)
    61863    0.405    0.000    1.054    0.000 abstract.py:40(as_dict)
    41243    0.343    0.000    1.131    0.000 __init__.py:143(uuid4)
   577388    0.338    0.000    0.649    0.000 abstract.py:46(<genexpr>)
    20622    0.289    0.000    8.824    0.000 base.py:331(send_task)
    61907    0.232    0.000    0.477    0.000 datastructures.py:467(__getitem__)
    20622    0.225    0.000    9.298    0.000 task.py:455(apply_async)
    61863    0.218    0.000    2.502    0.000 abstract.py:52(__copy__)
    20621    0.208    0.000    4.766    0.000 amqp.py:208(publish_task)
   462640    0.193    0.000    0.247    0.000 {isinstance}
   515525    0.162    0.000    0.193    0.000 abstract.py:41(f)
    41246    0.153    0.000    0.633    0.000 entity.py:143(__init__)
{% endcodeblock %}

In the example above (actual application) first line is kombu's
`abstract.py: class Object(object).__init__()`
and the second one is Python's
`uuid.py: class UUID().__init__()`.
