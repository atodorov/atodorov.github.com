---
layout: post
Title: Python Twitter + django-social-auth == Hello New User
date: 2013-03-07 21:47
comments: true
categories: ['Django', 'django-social-auth', 'Twitter', 'tips']
---

I have been experimenting with the [twitter](https://pypi.python.org/pypi/twitter)
module for Python and decided to combine it with 
[django-social-auth](https://github.com/omab/django-social-auth) to welcome new
users who join [Difio](http://www.dif.io). In this post I will show you how to
tweet on behalf of the user when they join your site and send them a welcome email.

Configuration
-------------

In django-social-auth the authentication workflow is handled by an operations
pipeline where custom functions can be added or default items can be removed to
provide custom behavior. This is how our pipeline looks:

{% codeblock settings.py lang:python %}
SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    #'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'myproject.tasks.welcome_new_user'
)
{% endcodeblock %}

This is the default plus an additional method at the end to welcome new users.

You also have to create and configure a Twitter application so that users
can login with Twitter OAuth to your site.
[RTFM](http://django-social-auth.readthedocs.org/en/latest/backends/index.html)
for more information on how to do this.

Custom pipeline actions
-----------------------

This is how the custom pipeline action should look:

{% codeblock myproject/tasks.py lang:python %}
from urlparse import parse_qs

def welcome_new_user(backend, user, social_user, is_new=False, new_association=False, *args, **kwargs):
    """
        Part of SOCIAL_AUTH_PIPELINE. Works with django-social-auth==0.7.21 or newer
        @backend - social_auth.backends.twitter.TwitterBackend (or other) object
        @user - User (if is_new) or django.utils.functional.SimpleLazyObject (if new_association)
        @social_user - UserSocialAuth object
    """
    if is_new:
        send_welcome_email.delay(user.email, user.first_name)

    if backend.name == 'twitter':
        if is_new or new_association:
            access_token = social_user.extra_data['access_token']
            parsed_tokens = parse_qs(access_token)
            oauth_token = parsed_tokens['oauth_token'][0]
            oauth_secret = parsed_tokens['oauth_token_secret'][0]
            tweet_on_join.delay(oauth_token, oauth_secret)

    return None
{% endcodeblock %}

This code works with django-social-auth==0.7.21 or newer. In older versions the
`new_association` parameter is missing as 
[I discovered](https://groups.google.com/forum/?fromgroups=#!topic/django-social-auth/Nxf-0iRD27Y).
If you use an older version you won't be able to distinguish between newly created
accounts and ones which have associated another OAuth backend. You are warned!

Tweet & email
--------------

Sending the welcome email is out of the scope of this post. I am using
[django-templated-email](https://github.com/bradwhittington/django-templated-email)
to define how emails look and sending them via Amazon SES. See 
[Email Logging for Django on RedHat OpenShift With Amazon SES](/blog/2013/02/28/email-logging-django-redhat-openshift-amazon-ses/)
for more information on how to configure emailing with SES.

Here is how the Twitter code looks:

{% codeblock myproject/tasks.py lang:python %}

import twitter
from celery.task import task
from settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET

@task
def tweet_on_join(oauth_token, oauth_secret):
    """
        Tweet when the user is logged in for the first time or
        when new Twitter account is associated.

        @oauth_token - string
        @oauth_secret - string
    """
    t = twitter.Twitter(
            auth=twitter.OAuth(
                oauth_token, oauth_secret,
                TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET
            )
        )
    t.statuses.update(status='Started following open source changes at http://www.dif.io!')
{% endcodeblock %}

This will post a new tweet on behalf of the user, telling everyone they joined
your website!

**NOTE:**
`tweet_on_join` and `send_welcome_email` are Celery tasks, not ordinary Python
functions. This has the advantage of being able to execute these actions async
and not slow down the user interface.


Are you doing something special when a user joins your website? Please share
your comments below. Thanks!
