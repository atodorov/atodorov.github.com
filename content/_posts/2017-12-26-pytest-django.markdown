Title: On Pytest-django and LiveServerTestCase with initial data
date: 2017-12-26 11:20
comments: true
Tags: fedora.planet, Django


While working on [Kiwi TCMS](http://kiwitcms.org) I've had the opportunity to
learn in-depth about how the standard test case classes in Django work. This
is a quick post about creating initial data and order of execution!


Initial test data for TransactionTestCase or LiveServerTestCase
---------------------------------------------------------------

`class LiveServerTestCase(TransactionTestCase)`, as the name suggests, provides a running
Django instance during testing. We use that for Kiwi's XML-RPC API tests, issuing
http requests against the live server instance and examining the responses!
For testing to work we also need some initial data. There are few key items
that need to be taken into account to accomplish that:

- `self._fixture_teardown()` - performs `./manage.py flush` which
  deletes all records from the database, including the ones created during initial
  migrations;
- `self.serialized_rollback` - when set to True will serialize initial
  records from the database into a string and then load this back. Required if
  subsequent tests need to have access to the records created during migrations!
- `cls.setUpTestData` is an attribute of `class TestCase(TransactionTestCase)` and hence
  can't be used to create records before any transaction based test case is executed.
- `self._fixture_setup()` is where the serialized rollback happens, thus it can
  be used to create initial data for your tests!

In Kiwi TCMS all XML-RPC test classes have `serialized_rollback = True` and
implement a `_fixture_setup()` method instead of `setUpTestData()` to create the
necessary records before testing!


**NOTE:** you can also use fixtures in the above scenario but I don't like using them
and we've deleted all fixtures from Kiwi TCMS a long time ago so I didn't feel like
going back to that!


Order of test execution
-----------------------

From
[Django's docs](https://docs.djangoproject.com/en/2.0/topics/testing/overview/#order-in-which-tests-are-executed):

> In order to guarantee that all TestCase code starts with a clean database, the Django test runner reorders
> tests in the following way:
>
> - All TestCase subclasses are run first.
> - Then, all other Django-based tests (test cases based on SimpleTestCase, including TransactionTestCase) are run
>   with no particular ordering guaranteed nor enforced among them.
> - Then any other unittest.TestCase tests (including doctests) that may alter the database without restoring it to
>   its original state are run.

This is not of much concern most of the time but becomes important when you decide
to mix and match transaction and non-transaction based tests into one test suite.
As seen in [Job #471.1](https://travis-ci.org/kiwitcms/Kiwi/jobs/321018491)
`tcms/xmlrpc/tests/test_serializer.py` tests errored out! If you execute these tests
standalone they all pass! The root cause is that these serializer tests are based on
Django's `test.TestCase` class and are executed after a `test.LiveServerTestCase` class!

The tests in `tcms/xmlrpc/tests/test_product.py` will flush the database, removing all
records, including the ones from initial migrations. Then when `test_serializer.py` is
executed it will call its factories which in turn rely on initial records being available
and produces an error because these records have been deleted!

The reason for this is that **pytest doesn't respect the order of execution for Django tests**!
As seen
in the build log above tests are executed in the order in which they were discovered!
My solution was not to use pytest (I don't need it for anything else)!



At the moment I'm dealing with strange errors/segmentation faults when running Kiwi's tests
under Django 2.0. It looks like the http response has been closed before the client side
tries to read it. Why this happens I have not been able to figure out yet. Expect another
blog post when I do.


Thanks for reading and happy testing!
