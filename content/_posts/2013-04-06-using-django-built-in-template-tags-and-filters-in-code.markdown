---
layout: post
Title: Using Django built-in template tags and filters in code
date: 2013-04-06 22:26
comments: true
Tags: tips, Django, Python
---

In case you are wondering how to use Django's
[built-in template tags and filters](https://docs.djangoproject.com/en/dev/ref/templates/builtins/)
in your source code, not inside a template here is how:

    :::python
    >>> from django.template.defaultfilters import *
    >>> filesizeformat(1024)
    u'1.0 KB'
    >>> filesizeformat(1020)
    u'1020 bytes'
    >>> filesizeformat(102412354)
    u'97.7 MB'
    >>> 

All built-ins live in `pythonX.Y/site-packages/django/template/defaultfilters.py`.
