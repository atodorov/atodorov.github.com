---
layout: post
Title: python-libs in RHEL 7.2 broke SSL verification in s3cmd
date: 2015-11-24 21:44
comments: true
Tags: QA, fedora.planet, RHEL, Python
Slug: python-libs-in-rhel-7.2-broke-ssl-verification-in-s3cmd
---

Today started with [Planet Sofia Valley](http://planet.sofiavalley.com) being
broken again. Indeed it's been broken since last Friday when I've upgraded to
the latest RHEL 7.2. I quickly identified that I was hitting
[Issue #647](https://github.com/s3tools/s3cmd/issues/647). Then I tried the
git checkout without any luck. This is when I started to suspect that python-libs
has been updated in an incompatible way.

After series of reported bugs,
[rhbz#1284916](https://bugzilla.redhat.com/show_bug.cgi?id=1284916),
[rhbz#1284930](https://bugzilla.redhat.com/show_bug.cgi?id=1284930),
[Python#25722](http://bugs.python.org/issue25722), it was clear that
`ssl.py` was working according to RFC6125, that Amazon S3 was not playing
nicely with this same RFC and that my patch proposal was wrong.
This immediately had me looking upper in the stack at `httplib.py` and `s3cmd`.

Indeed there was a change in `httplib.py` which introduced two parameters,
*context* and *check_hostname*, to `HTTPSConnection.__init__`. The change
also supplied the logic which performs SSL hostname validation.

    if not self._context.check_hostname and self._check_hostname:
        try:
            ssl.match_hostname(self.sock.getpeercert(), server_hostname)
        except Exception:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
            raise

This looks a bit doggy as I don't quite understand the intention behind
*not PREDICATE and PREDICATE*. Anyway to disable the validation you need
both parameters set to False, which is
[PR #668](https://github.com/s3tools/s3cmd/pull/668).

Notice the two try-except blocks. This is in case we're running with a
version that has a context but not the check_hostname parameter. I've found
the *inspect.getmembers* function which can be used to figure out what
parameters are there for the init method but a solution based on it
doesn't appear to be more elegant. I will describe this in more details in
my next post.
