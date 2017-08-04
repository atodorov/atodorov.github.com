Title: TransactionManagementError during testing with Django 1.10
Headline: caused by nested HttpResponse objects
date: 2017-08-04 22:30
comments: true
Tags: fedora.planet, QA, Django

During the past 3 weeks I've been debugging a weird error which
started happening after I migrated [KiwiTestPad](http://MrSenko.com/kiwi/) to
Django 1.10.7. Here is the reason why this happened.


Symptoms
--------

After migrating to Django 1.10 all tests appeared to be working locally
on SQLite however they
[failed on MySQL](https://travis-ci.org/MrSenko/Kiwi/jobs/258309883) with

    TransactionManagementError: An error occurred in the current transaction. You can't execute queries until the end of the 'atomic' block.

The exact same test cases
[failed on PostgreSQL](https://travis-ci.org/MrSenko/Kiwi/jobs/258309884) with:

    InterfaceError: connection already closed


Since version 1.10 Django executes all tests inside transactions so my first
thoughts were related to the auto-commit mode. However upon closer inspection
we can see that the line which triggers the failure is

    self.assertTrue(users.exists())

which is essentially a `SELECT` query aka
`User.objects.filter(username=username).exists()`!

**My tests were failing on a SELECT query!**


Reading the numerous posts about `TransactionManagementError` I discovered it may
be caused by a run-away cursor. The application did use raw SQL statements which
I've converted promptly to ORM queries, that took me some time. Then I also fixed
a couple of places where it used `transaction.atomic()` as well. No luck!


Then, after numerous experiments and tons of logging inside Django's own code I was
able to figure out when the failure occurred and what events were in place. The test
code looked like this:

    :::python
    response = self.client.get('/confirm/')
    
    user = User.objects.get(username=self.new_user.username)
    self.assertTrue(user.is_active)

**The failure was happening after the view had been rendered upon the
first time I do a SELECT against the database!**

**The problem was that the connection to the database had been closed
midway during the transaction!**

In particular (after more debugging of course) the sequence of events was:

1. execute `django/test/client.py::Client::get()`
2. execute `django/test/client.py::ClientHandler::__call__()`, which takes
   care to disconnect/connect `signals.request_started` and `signals.request_finished`
   which are responsible for tearing down the DB connection, so problem not here
3. execute `django/core/handlers/base.py::BaseHandler::get_response()`
4. execute `django/core/handlers/base.py::BaseHandler::_get_response()` which goes through
   the middleware (needless to say I did inspect all of it as well since there
   have been some changes in Django 1.10)
5. execute `response = wrapped_callback()` while still inside `BaseHandler._get_response()`
6. execute `django/http/response.py::HttpResponseBase::close()` which looks like

        :::python
        # These methods partially implement the file-like object interface.
        # See https://docs.python.org/3/library/io.html#io.IOBase
         
        # The WSGI server must call this method upon completion of the request.
        # See http://blog.dscpl.com.au/2012/10/obligations-for-calling-close-on.html
        def close(self):
            for closable in self._closable_objects:
                try:
                    closable.close()
                except Exception:
                    pass
            self.closed = True
            signals.request_finished.send(sender=self._handler_class)

7. `signals.request_finished` is fired
8. `django/db/__init__.py::close_old_connections()` closes the connection!

**IMPORTANT:** On MySQL setting `AUTO_COMMIT=False` and `CONN_MAX_AGE=None` helps
workaround this problem but is not the solution for me because it didn't help on
PostgreSQL.

Going back to `HttpResponseBase::close()` I started wondering who calls this method.
The answer was it was getting called by the `@content.setter` method at
`django/http/response.py::HttpResponse::content()` which is even more weird because
we assign to `self.content` inside `HttpResponse::__init__()`

Root cause
----------

The root cause of my problem was precisely this `HttpResponse::__init__()` method
or rather the way we arrive at it inside the application. 

The offending view last line was

    :::python
    return HttpResponse(Prompt.render(
         request=request,
         info_type=Prompt.Info,
         info=msg,
         next=request.GET.get('next', reverse('core-views-index'))
    ))

and the Prompt class looks like this

    :::python
    from django.shortcuts import render
    
    class Prompt(object):
        @classmethod
        def render(cls, request, info_type=None, info=None, next=None):
            return render(request, 'prompt.html', {
                'type': info_type,
                'info': info,
                'next': next
            })


Looking back at the internals of `HttpResponse` we see that

- if content is a string we call `self.make_bytes()`
- if the content is an iterator then we assign it and if the object has a close method
  then it is executed.

`HttpResponse` itself is an iterator, inherits from `six.Iterator` so when we initialize
`HttpResponse` with another `HttpResponse` object (aka the content) we execute `content.close()`
which unfortunately happens to close the database connection as well.

**IMPORTANT:** note that from the point of view of a person using the application the
HTML content is exactly the same regardless of whether we have nested `HttpResponse` objects
or not.
Also during normal execution the code doesn't run inside a transaction so we never notice
the problem in production.

The fix of course is very simple, just `return Prompt.render()`!

Thanks for reading and happy testing!
