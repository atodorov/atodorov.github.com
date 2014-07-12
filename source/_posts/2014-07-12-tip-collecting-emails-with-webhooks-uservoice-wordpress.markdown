---
layout: post
title: "Tip: Collecting Emails - Webhooks for UserVoice and WordPress.com"
date: 2014-07-12 23:15
comments: true
categories: ['tips', 'Django', 'start-up']
---

In my practice I like to use webhooks and integrate auxiliary services with
my internal processes or businesses. One of these is the collection of emails.
In this short article I'll show you an example of how to collect email addresses
from the comments of a WordPress.com blog and the UserVoice feedback/ticketing system.

WordPress.com
--------------

For your WordPress.com blog from the Admin Dashboard navigate to 
Settings -> Webhooks and add a new webhook with action `comment_post`
and fields `comment_author`, `comment_author_email`. A simple
Django view that handles the input is shown below.

{% codeblock lang:python %}
@csrf_exempt
def hook_wp_comment_post(request):
    if not request.POST:
        return HttpResponse("Not a POST\n", content_type='text/plain', status=403)

    hook = request.POST.get("hook", "")

    if hook != "comment_post":
        return HttpResponse("Go away\n", content_type='text/plain', status=403)

    name = request.POST.get("comment_author", "")
    first_name = name.split(' ')[0]
    last_name = ' '.join(name.split(' ')[1:])

    details = {
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : request.POST.get("comment_author_email", ""),
    }

    store_user_details(details)

    return HttpResponse("OK\n", content_type='text/plain', status=200)
{% endcodeblock %}


UserVoice
---------

For UserVoice navigate to Admin Dashboard -> Settings -> Integrations -> 
Service Hooks and add a custom web hook for the New Ticket notification.
Then use a sample code like that:

{% codeblock lang:python %}
@csrf_exempt
def hook_uservoice_new_ticket(request):
    if not request.POST:
        return HttpResponse("Not a POST\n", content_type='text/plain', status=403)

    data = request.POST.get("data", "")
    event = request.POST.get("event", "")

    if event != "new_ticket":
        return HttpResponse("Go away\n", content_type='text/plain', status=403)

    data = json.loads(data)

    details = {
        'email' : data['ticket']['contact']['email'],
    }

    store_user_details(details)

    return HttpResponse("OK\n", content_type='text/plain', status=200)
{% endcodeblock %}


`store_user_details()` is a function which handles the email/name received in the webhook,
possibly adding them to a database or anything else.

I find webhooks extremely easy to setup and develop and used them whenever they are
supported by the service provider. What other services do you use webhooks for? Please
share your story in the comments.


