---
layout: post
Title: Mocking Django AUTH_PROFILE_MODULE without a Database
date: 2014-02-27 16:18
comments: true
Tags: Django
Slug: mocking-django-auth-profile-module-without-database
---

[Difio](http://www.dif.io) is a Django based service which uses a profile
model to provide site-specific, per-user information.
In the process of [open sourcing Difio](https://github.com/difio/difio) its core
functionality becomes available as a Django app. The trouble is that the 
`UserProfile` model contains site-specific and proprietary data which doesn't
make sense to the public nor I want to release it.

The solution is to have a `MockProfile` model and work with
that by default while [www.dif.io](http://www.dif.io) and other implementations
override it as needed.
**How do you do that without creating useless table and records in the database
but still have the profiles created automatically for every user?**

It turns out the solution is quite simple. See my comments inside the code below.

    :::python
    class AbstractMockProfile(models.Model):
        """
            Any AUTH_PROFILE_MODULE model should inherit this
            and override the default methods.
    
            This model provides the FK to User!
        """
        user = models.ForeignKey(User, unique=True)
    
        def is_subscribed(self):
            """ Is this user subscribed for our newsletter? """
            return True
    
        class Meta:
            # no DB table created b/c model is abstract
            abstract = True
    
    class MockProfileManager(models.Manager):
        """
            This manager creates MockProfile's on the fly without
            touching the database. It is needed by User.get_profile()
            b/c we can't have an abstract base class as AUTH_PROFILE_MODULE.
        """
        def using(self, *args, **kwargs):
            """ It doesn't matter which database we use! """
            return self
    
        def get(self, *args, **kwargs):
            """
                User.get_profile() calls .using(...).get(user_id__exact=X)
                so we instrument it here to return a MockProfile() with
                user_id=X parameter. Anything else may break!!!
            """
            params = {}
            for p in kwargs.keys():
                params[p.split("__")[0]] = kwargs[p]
    
            # this creates an object in memory. To save it to DB
            # call obj.save() which we DON'T do anyway!
            return MockProfile(params)
    
    
    class MockProfile(AbstractMockProfile):
        """
            In-memory (fake) profile class used by default for
            the AUTH_PROFILE_MODULE setting.
        """
        objects = MockProfileManager()
    
        class Meta:
            # DB table is NOT created automatically
            # when managed = False
            managed = False
    


In Difio core the user profile is always used like this

    profile = request.user.get_profile()
    if profile.is_subscribed():
        pass

and by default

    AUTH_PROFILE_MODULE = "difio.MockProfile"

Voila!
