---
layout: post
Title: Bug in Python URLGrabber/cURL on Fedora and Amazon Linux
date: 2013-11-29 14:05
comments: true
Tags: Fedora, QA, cloud, Python
---

Accidentally I have discovered a bug for Python's
URLGrabber module which has to do with change in behavior in libcurl.

{% codeblock lang:python %}
>>> from urlgrabber.grabber import URLGrabber
>>> g = URLGrabber(reget=None)
>>> g.urlgrab('https://s3.amazonaws.com/production.s3.rubygems.org/gems/columnize-0.3.6.gem', '/tmp/columnize.gem')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/celeryd/.virtualenvs/difio/lib/python2.6/site-packages/urlgrabber/grabber.py", line 976, in urlgrab
    return self._retry(opts, retryfunc, url, filename)
  File "/home/celeryd/.virtualenvs/difio/lib/python2.6/site-packages/urlgrabber/grabber.py", line 880, in _retry
    r = apply(func, (opts,) + args, {})
  File "/home/celeryd/.virtualenvs/difio/lib/python2.6/site-packages/urlgrabber/grabber.py", line 962, in retryfunc
    fo = PyCurlFileObject(url, filename, opts)
  File "/home/celeryd/.virtualenvs/difio/lib/python2.6/site-packages/urlgrabber/grabber.py", line 1056, in __init__
    self._do_open()
  File "/home/celeryd/.virtualenvs/difio/lib/python2.6/site-packages/urlgrabber/grabber.py", line 1307, in _do_open
    self._set_opts()
  File "/home/celeryd/.virtualenvs/difio/lib/python2.6/site-packages/urlgrabber/grabber.py", line 1161, in _set_opts
    self.curl_obj.setopt(pycurl.SSL_VERIFYHOST, opts.ssl_verify_host)
error: (43, '')
>>> 
{% endcodeblock %}

The code above works fine with curl-7.27 or older while it breaks with curl-7.29 and
newer. As explained by 
[Zdenek Pavlas](http://lists.baseurl.org/pipermail/yum-devel/2013-November/010428.html)
the reason is an internal change in libcurl which doesn't accept a value of 1 anymore!

The bug is reproducible with a newer libcurl version and a vanilla urlgrabber==3.9.1
from PyPI (e.g. inside a virtualenv). The latest python-urlgrabber RPM packages in both
Fedora and Amazon Linux already have the fix.


I have tested the patch proposed by Zdenek and it works for me. I still have no idea why
there aren't any updates released on PyPI though!

