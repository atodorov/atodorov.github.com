---
layout: post
title: "Email Logging for Django on RedHat OpenShift with Amazon SES"
date: 2013-02-28 23:19
comments: true
categories: ['tips', 'Django', 'Amazon', 'SES', 'OpenShift', 'cloud']
---

Sending email in the cloud can be tricky. IPs of cloud providers are blacklisted
because of frequent abuse. For that reason I use
[Amazon SES](http://aws.amazon.com/ses/) as my email backend. Here is how to
configure [Django](https://www.djangoproject.com/) to send emails to site admins
when something goes wrong.

{% codeblock settings.py lang:python %}
# Valid addresses only.
ADMINS = (
    ('Alexander Todorov', 'atodorov@example.com'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
 
# Used as the From: address when reporting errors to admins
# Needs to be verified in Amazon SES as a valid sender
SERVER_EMAIL = 'django@example.com'

# Amazon Simple Email Service settings
AWS_SES_ACCESS_KEY_ID = 'xxxxxxxxxxxx'
AWS_SES_SECRET_ACCESS_KEY = 'xxxxxxxx'
EMAIL_BACKEND = 'django_ses.SESBackend'
{% endcodeblock %}

You also need the [django-ses](https://github.com/hmarr/django-ses)
dependency.

See <http://docs.djangoproject.com/en/dev/topics/logging> for
more details on how to customize your logging configuration.


I am using this configuration successfully at RedHat's OpenShift PaaS environment.
Other users have
[reported](https://openshift.redhat.com/community/forums/express/missing-email-on-500-ise-w-django)
it works for them too. Should work with any other PaaS provider.



