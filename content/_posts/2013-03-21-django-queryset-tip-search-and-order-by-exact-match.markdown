---
layout: post
title: "Django QuerySet tip - Search and Order By Exact Match"
date: 2013-03-21 22:56
comments: true
categories: ['tips', 'Django']
---

How do you order Django QuerySet results so that first item is the
exact match if using `contains` or `icontains` ? Both solutions were proposed on the
[django-users](https://groups.google.com/d/topic/django-users/OCNmIXrRgag/discussion)
mailing list.

{% codeblock Solution by Tom Evans, example is mine lang:python %}
>>> from django.db.models import Q
>>> Package.objects.filter(
        Q(name='Django') | Q(name__icontains='Django')
    ).extra(
        select={'match' : 'name = "Django"'}
    ).order_by('-match', 'name')
[<Package: Django>, <Package: appomatic_django_cms>, <Package: appomatic_django_filer>,
<Package: appomatic_django_vcs>, <Package: BabelDjango>, <Package: BDD4Django>,
<Package: blanc-django-admin-skin>, <Package: bootstrap-django-forms>,
<Package: capistrano-django>, <Package: ccnmtldjango>, <Package: collective.django>,
<Package: csdjango.contactform>, <Package: cykooz.djangopaste>,
<Package: cykooz.djangorecipe>, <Package: d51.django.virtualenv.test_runner>,
<Package: django-4store>, <Package: django-503>, <Package: django-absolute>,
<Package: django-abstract-templates>, <Package: django-account>,
'...(remaining elements truncated)...']
>>> 
{% endcodeblock %}

Another one:

{% blockquote Gabriel https://groups.google.com/d/topic/django-users/OCNmIXrRgag/discussion %}
I'm not sure this is the right way, but you could drop the Q objects, use
only icontains and sort by the length of 'name'
{% endblockquote %}

{% codeblock Example is mine lang:python %}
>>> packages = [p.name for p in Package.objects.filter(name__icontains='Dancer')]
>>> sorted(packages, key=len)
[u'Dancer', u'Dancer2', u'breakdancer', u'Task::Dancer', u'App::Dancer2', u'Dancer::Routes',
u'DancerX::Routes', u'DancerX::Config', u'Task::DWIM::Dancer', u'Dancer::Plugin::CDN',
u'Dancer::Plugin::Feed', u'Dancer::Plugin::LDAP', u'Dancer::Plugin::Lucy', 
'...(remaining elements truncated)...']
>>> 
{% endcodeblock %}

That's all folks. If you have other more interesting sorting needs please comment below.
Thanks!
