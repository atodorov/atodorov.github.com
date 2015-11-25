---
layout: post
Title: SNAKE is no Longer Needed to Run Installation Tests in Beaker
date: 2014-07-18 23:05
comments: true
Tags: 'Fedora', 'QA'
---

This is a quick status update for one of the pieces of
[Fedora QA infrastructure](/blog/2013/11/19/open-source-quality-assurance-infrastructure-for-fedora-qa/)
and mostly a self-note.

Previously to control the kickstart configuration used during installation in Beaker one
had to either modify the job XML in Beaker or use SNAKE (`bkr workflow-snake`) to render
a kickstart configuration from a Python template.

SNAKE presented challenges when deploying and using
[beaker.fedoraproject.org](https://beaker.fedoraproject.org) and is
virtually unmaintained.

I present the new `bkr workflow-installer-test` which uses Jinja2 templates to
generate a kickstart configuration when provisioning the system. This is already
available in beaker-client-0.17.1.


The templates make use of all Jinja2 features (as far as I can tell) so you can create
very complex ones. You can even include snippets from one template into another if required.
The standard context that is passed to the template is:

* **DISTRO** - if specified, the distro name
* **FAMILY** - as returned by Beaker server, e.g. *RedHatEnterpriseLinux6*
* **OS_MAJOR** and **OS_MINOR** - also taken from Beaker server. e.g. OS_MAJOR=6 and OS_MINOR=5 for RHEL 6.5
* **VARIANT** - if specified
* **ARCH** - CPU architecture like x86_64
* any parameters passed to the test job with `--taskparam`. They are processed last and can override previous values.


Installation related tests at [fedora-beaker-tests](https://bitbucket.org/fedoraqa/fedora-beaker-tests)
have been updated with a `ks.cfg.tmpl` templates to use with this new workflow.

This workflow also has the ability to return boot arguments for the installer if needed. 
If any, they should be defined in a {% raw %}{% block kernel_options %}{% endblock %}{% endraw %}
block inside the template. A simpler variant is to define a comment line that stars with
*## kernel_options:*


There are still a few issues which need to be fixed before beaker.fedoraproject.org
can be used by the general public though. I will be writing another post about that
so stay tuned.
