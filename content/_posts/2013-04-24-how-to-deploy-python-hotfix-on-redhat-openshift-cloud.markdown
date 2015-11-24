---
layout: post
title: "How to Deploy Python Hotfix on RedHat OpenShift Cloud"
date: 2013-04-24 11:58
comments: true
categories: ['tips', 'Python', 'OpenShift', 'cloud']
---

In this article I will show you how to deploy hotfix versions for
Python packages on the RedHat [OpenShift](http://openshift.com) PaaS cloud.

Background
----------

You are already running a Python application on your OpenShift instance.
You are using some 3rd party dependencies when you find a bug in one of them.
You go forward, fix the bug and submit a
[pull request](https://github.com/ahupp/python-magic/pull/31).
You don't want to wait for upstream to release a new version but rather
build a hotfix package yourself and deploy to production immediately.

Solution
---------

There are two basic approaches to solving this problem: 

1. Include the hotfix package source code in your application, i.e.
add it to your git tree or;
2. Build the hotfix separately and deploy as a dependency. Don't
include it in your git tree, just add a requirement on the hotfix version. 

I will talk about the later. The tricky part here is to instruct the cloud environment
to use your package (including the proper location) and not upstream or their local
mirror.

Python applications hosted at [OpenShift](http://openshift.com) don't support
`requirements.txt` which can point to various package sources and even install
packages directly from GitHub. They support `setup.py` which fetches packages
from <http://pypi.python.org> but it is flexible enough to support other locations.


Building the hotfix
-------------------

First of all we'd like to build a hotfix package. This will be the upstream
version that we are currently using plus the patch for our critical issue:

    $ wget https://pypi.python.org/packages/source/p/python-magic/python-magic-0.4.3.tar.gz
    $ tar -xzvf python-magic-0.4.3.tar.gz 
    $ cd python-magic-0.4.3
    $ curl https://github.com/ahupp/python-magic/pull/31.patch | patch 

Verify the patch has been applied correctly and then modify `setup.py` to
increase the version string. In this case I will set it to `version='0.4.3.1'`.

Then build the new package using `python setup.py sdist` and upload it to a web server.


Deploying to OpenShift
-----------------------

Modify `setup.py` and specify the hotfix version. Because this version is not on PyPI
and will not be on OpenShift's local mirror you need to provide the location where it can
be found. This is done with the `dependency_links` parameter to `setup()`. Here's how it looks:

{% codeblock lang:diff %}
diff --git a/setup.py b/setup.py
index c6e837c..2daa2a9 100644
--- a/setup.py
+++ b/setup.py
@@ -6,5 +6,6 @@ setup(name='YourAppName',
       author='Your Name',
       author_email='example@example.com',
       url='http://www.python.org/sigs/distutils-sig/',
-      install_requires=['python-magic==0.4.3'],
+      dependency_links=['https://s3.amazonaws.com/atodorov/blog/python-magic-0.4.3.1.tar.gz'],
+      install_requires=['python-magic==0.4.3.1'],
      )
{% endcodeblock %}

Now just git push to OpenShift and observe the console output:

    remote: Processing dependencies for YourAppName==1.0
    remote: Searching for python-magic==0.4.3.1
    remote: Best match: python-magic 0.4.3.1
    remote: Downloading https://s3.amazonaws.com/atodorov/blog/python-magic-0.4.3.1.tar.gz
    remote: Processing python-magic-0.4.3.1.tar.gz
    remote: Running python-magic-0.4.3.1/setup.py -q bdist_egg --dist-dir /tmp/easy_install-ZRVMBg/python-magic-0.4.3.1/egg-dist-tmp-R_Nxie
    remote: zip_safe flag not set; analyzing archive contents...
    remote: Removing python-magic 0.4.3 from easy-install.pth file
    remote: Adding python-magic 0.4.3.1 to easy-install.pth file

Congratulations! Your hotfix package has just been deployed.

This approach should work for other cloud providers and other programming languages
as well. Let me know if you have any experience with that.


