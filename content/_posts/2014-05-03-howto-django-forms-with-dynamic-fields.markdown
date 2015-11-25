---
layout: post
Title: Howto: Django Forms with Dynamic Fields
date: 2014-05-03 16:58
comments: true
Tags: Django
---

Last week at [HackFMI 3.0](http://hackfmi.com) one team had to display a form
which presented multiple choice selection for filtering, where the filter keys
are read from the database. They've solved the problem by simply building up the
HTML required inside the view. I was wondering if this can be done with forms.

    :::python
    >>> from django import forms
    >>>
    >>> class MyForm(forms.Form):
    ...     pass
    ...
    >>> print(MyForm())
    
    >>> MyForm.__dict__['base_fields']['name'] = forms.CharField()
    >>> MyForm.__dict__['base_fields']['age'] = forms.IntegerField()
    >>> print(MyForm())
    <tr><th><label for="id_name">Name:</label></th><td><input id="id_name" name="name" type="text" /></td></tr>
    <tr><th><label for="id_age">Age:</label></th><td><input id="id_age" name="age" type="number" /></td></tr>
    >>>
    >>>
    >>> POST = {'name' : 'Alex', 'age' : 0}
    >>> f = MyForm(POST)
    >>> print(f)
    <tr><th><label for="id_name">Name:</label></th><td><input id="id_name" name="name" type="text" value="Alex" /></td></tr>
    <tr><th><label for="id_age">Age:</label></th><td><input id="id_age" name="age" type="number" value="0" /></td></tr>
    >>> f.is_valid()
    True
    >>> f.is_bound
    True
    >>> f.errors
    {}
    >>> f.cleaned_data
    {'age': 0, 'name': u'Alex'}


So if we were to query all names from the database then we could build up the
class by adding a BooleanField using the object primary key as the name.

    :::python
    >>> MyForm.__dict__['base_fields']['123'] = forms.BooleanField()
    >>> print(MyForm())
    <tr><th><label for="id_123">123:</label></th><td><input id="id_123" name="123" type="checkbox" /></td></tr>
    >>> f = MyForm({'123' : True})
    >>> f.is_valid()
    True
    >>> f.cleaned_data
    {'123': True}

