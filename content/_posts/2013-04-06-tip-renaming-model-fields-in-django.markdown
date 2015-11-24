---
layout: post
title: "Tip: Renaming Model Fields in Django"
date: 2013-04-06 01:18
comments: true
categories: ['tips', 'Django']
---

Did you ever have to re-purpose a column in your database schema? 
Here's a quick and easy way to do this if you happen to be using Django.

Scenario
--------

I had an integer field in my model called `lines` which counted the lines of 
code in a particular tar.gz package. I figured the file size is a better indicator
so decided to start using it. I was not planning to use the old field anymore and
I didn't care about the data it was holding. So I decided to re-purpose it
as the `size` field.

Possible methods
----------------

Looking around I figured several different ways to do this: 

1. Continue using the existing `lines` field and keep referencing the old name in the code.
This is no-brainer but feels awkward and is a disaster waiting to happen;
1. Add new `size` field and remove the old `lines` field. This involves modification to
the DB schema and requires at least a backup with possible down time. Not something
I will jump at right away;
1. Add a `size` property in the model class which will persist to `self.lines`.
This is a quick way to go but I'm not sure if one can use the property with the
Django QuerySet API (objects.filter(), objects.update(), etc.) I suspect not.
If you don't filter by the property or use it in bulk operations this method is fine though;
1. Change the field name to `size` but continue to use the `lines` DB column;
Mind my wording here :);
1. Rename the column in the DB schema and then update the model class field.

How I did it
------------

I decided to go for option 4 above: 
change the field name to `size` but continue to use the `lines` DB column.

{% codeblock lang:diff %}
diff --git a/models.py b/models.py
index e06d2b2..18cad6f 100644
--- a/models.py
+++ b/models.py
@@ -667,7 +667,7 @@ class Package(models.Model):
-    lines = models.IntegerField(default=None, null=True, blank=True)
+    size  = models.IntegerField(default=None, null=True, blank=True, db_column='lines')
{% endcodeblock %}

1. Removed all references to `lines` from the code except the model class. This served as clean up as well. 
1. Renamed the model field to `size` but continued using the `lines` DB column as shown above.
Django's *db_column* option makes this possible.
1. From the Django shell (./manage.py shell) reset `size` to None (NULL) for all objects;
1. Finally implement my new code and functionality behind the `size` field.

The entire process happened for under 10 minutes. I will also opt for renaming the DB column at a later time.
This is to sync the naming used in Python code and in MySQL in case I ever need to use raw SQL or anything but Django.

If you were me, how would you do this? Please share in the comments below.


