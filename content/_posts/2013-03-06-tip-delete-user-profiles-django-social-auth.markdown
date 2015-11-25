---
layout: post
Title: Tip: Delete User Profiles with django-social-auth
date: 2013-03-06 21:02
comments: true
Tags: tips, Django, django-social-auth
---

Common functionality for websites is the 'DELETE ACCOUNT' or 'DISABLE ACCOUNT'
button. This is how to implement it if using 
[django-social-auth](https://github.com/omab/django-social-auth).

{% codeblock views.py lang:python %}
delete_objects_for_user(request.user.pk) # optional
UserSocialAuth.objects.filter(user=request.user).delete()
User.objects.filter(pk=request.user.pk).update(is_active=False, email=None)
return HttpResponseRedirect(reverse('django.contrib.auth.views.logout'))
{% endcodeblock %}

This snippet does the following:

* Delete (or archive) all objects for the current user;
* Delete the social auth profile(s) because there is no way to disable them.
DSA will create new objects if the user logs in again;
* Disable the `User` object. You could also delete it but mind foreign keys;
* Clear the email for the `User` object - if a new user is created after deletion
we don't want duplicated email addresses in the database;
* Finally redirect the user to the logout view.

