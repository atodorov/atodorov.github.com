---
layout: post
Title: Beware of Django default Model Field Option When Using datetime.now()
date: 2014-04-15 15:54
comments: true
Tags: Django
Slug: beware-of-django-default-model-field-option-when-using-datetime-now
---

Beware if you are using code like this:

    models.DateTimeField(default=datetime.now())

i.e. passing a function return value as the default option for a model field in Django.
In some cases the value will be calculated once when the application starts or
the module is imported and will not be updated later. The most common scenario
is DateTime fields which default to now(). The correct way is to use a callable:


    models.DateTimeField(default=datetime.now)


I've hit this issue on a low volume application which uses cron to collect its own
metrics by calling an internal URL. The app was running as WSGI app and I wondered
why I got records with duplicate dates in the DB. A more detailed (correct) example follows:


    :::python
    def _strftime():
        return datetime.now().strftime('%Y-%m-%d')
    
    class Metrics(models.Model):
        key = models.IntegerField(db_index=True)
        value = models.FloatField()
        added_on = models.DateTimeField(db_index=True, default=datetime.now)
        added_on_as_text = models.CharField(max_length=16, default=_strftime)


[Difio](http://www.dif.io) also had the same bug but didn't exhibit the problem
because all objects with default date-time values were created on the backend nodes
which get updated and restarted very often.

For more info read this
[blog](http://david.feinzeig.com/blog/2011/12/06/how-to-properly-set-a-default-value-for-a-datetimefield-in-django/).
