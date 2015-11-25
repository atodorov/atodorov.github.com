---
layout: post
Title: Django Template Tag Inheritance How-to
date: 2013-12-22 23:02
comments: true
Tags: 'Django'
---

While working on open-sourcing [Difio](http://www.dif.io) I needed to remove
all hard-coded URL references from the templates. My solution was to essentially
inherit from the standard `{% raw %}{% url %}{% endraw %}` template tag. Here is how to do it.

Background History
------------------

Difio is not hosted on a single server. Parts of the website are static HTML,
hosted on Amazon S3. Other parts are dynamic - hosted on OpenShift. It's also
possible but not required at the moment to host at various PaaS providers for
redundancy and simple load balancing. 

As an easy fix I had hard-coded some URLs to link to the static S3 pages and others
go link to my PaaS provider.

I needed a simple solution which can be extended to allow for multiple domain hosting.


The Solution
------------

The solution I came up with is to override the standard `{% raw %}{% url %}{% endraw %}`
tag and use it everywhere in my templates. The new tag will produce absolute URLs containing
the specified protocol plus domain name and view path. For this to work you have to
inherit the standard `URLNode` class and override the `render()` method to include the new
values.

You also need to register a tag method to utilize the new class. My approach was to use
the existing `url()` method to do all background processing and simply casting the result
object to the new class. 

All code is available at <https://djangosnippets.org/snippets/3013/>. 

To use in your templates simply add

{% codeblock %}{% raw %}
{% load fqdn_url from fqdn_url %}
<a href="{% fqdn_url 'dashboard' %}">Dashboard</a>
{% endraw %}{% endcodeblock %}
