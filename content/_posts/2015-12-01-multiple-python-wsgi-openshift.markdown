Title: Hosting Multiple Python WSGI Scripts on OpenShift
date: 2015-12-01 13:34
comments: true
Tags: fedora.planet, Python, OpenShift

With [OpenShift](http://openshift.com) you can host WSGI Python
applications. By default the Python cartridge comes with a simple WSGI app
and the following directory layout

    ./
    ./.openshift/
    ./requirements.txt
    ./setup.py
    ./wsgi.py

I wanted to add my
[GitHub Bugzilla Hook]({filename}/_posts/2015-11-24-github-bugzilla-hook.markdown)
in a subdirectory (git submodule actually) and simply reserve a URL which will
be served by this app. My intention is also to add other small scripts to the
same cartridge in order to better utilize the available resources.

Using `WSGIScriptAlias` inside `.htaccess` **DOESN'T WORK**! OpenShift errors
out when `WSGIScriptAlias` is present. I suspect this to be a known limitation
and I have an open support case with Red Hat to confirm this.

My workaround is to configure the URL paths from the `wsgi.py` file in the root
directory. For example

    :::diff
    diff --git a/wsgi.py b/wsgi.py
    index c443581..20e2bf5 100644
    --- a/wsgi.py
    +++ b/wsgi.py
    @@ -12,7 +12,12 @@ except IOError:
     # line, it's possible required libraries won't be in your searchable path
     #
     
    +from github_bugzilla_hook import wsgi as ghbzh
    +
     def application(environ, start_response):
    +    # custom paths
    +    if environ['PATH_INFO'] == '/github-bugzilla-hook/':
    +        return ghbzh.application(environ, start_response)
     
         ctype = 'text/plain'
         if environ['PATH_INFO'] == '/health':

This does the job and is almost the same as configuring the path in `.htaccess`.
I hope it helps you!
