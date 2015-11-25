---
layout: post
Title: This Week: Python Testing, Chris DiBona on Open Source and OpenShift ENV Variables
date: 2013-10-11 10:45
comments: true
Tags: 'Python', 'cloud', 'OpenShift'
---

Here is a random collection of links I came across this week which
appear interesting to me but I don't have time to blog about in details.

Making a Multi-branch Test Server for Python Apps
-------------------------------------------------

If you are wondering how to test different feature branches of your Python
application but don't have the resources to create separate test servers this
is for you: 
<http://depressedoptimism.com/blog/2013/10/8/making-a-multi-branch-test-server>!

*Kudos to the python-django-bulgaria Google group for finding this link!*

OpenSource.com Interview with Chris DiBona
---------------------------------------

Just read it at
<http://opensource.com/business/13/10/interview-chris-dibona>.

I particularly like the part where he called open source "brutal".

{% blockquote %}
You once called open source “brutal”. What did you mean by that?

...

I think that it is because open source projects are able to only work with the
productive people and ignore everyone else. That behavior can come across as
very harsh or exclusionary, and that's because it is that: brutally harsh and
exclusionary of anyone who isn't contributing.

...

So, I guess what I'm saying is that survival of the fittest as practiced in the
open source world is a pretty brutal mechanism, but it works very very well for
producing quality software. Boy is it hard on newcomers though...
{% endblockquote %}

OpenShift Finally Introduces Environment Variables
---------------------------------------------------

Yes! Finally! 

        rhc set-env VARIABLE1=VALUE1 -a myapp

No need for 
[my work around](/blog/2013/07/08/tip-setting-secure-env-variables-on-red-hat-openshift/)
anymore! I will give the new feature a go very soon. 

Read more about it at the OpenShift blog:
<https://www.openshift.com/blogs/taking-advantage-of-environment-variables-in-openshift-php-apps>.


Have you found anything interesting this week? Please share in the comments below! Thanks!
