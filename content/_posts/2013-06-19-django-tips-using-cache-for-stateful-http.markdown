---
layout: post
Title: Django Tips: Using Cache for Stateful HTTP
date: 2013-06-19 13:50
comments: true
Tags: 'Django', 'tips', 'Twilio', 'cloud'
---

How do you keep state when working with a stateless protocol like HTTP? 
One possible answer is to use a cache back-end. 

I'm working on an IVR application demo with Django and Twilio. The caller
will make multiple choices using the phone keyboard. All of this needs to be
put together and sent back to another server for processing. In my views
I've added a simple cache get/set lines to preserve the selection.


Here's how it looks with actual application logic omitted

{% codeblock lang:python %}

def incoming_call(request):
    call_sid = request.GET.get('CallSid', '')
    caller_id = request.GET.get('From', '')

    state = {'from' : caller_id}
    cache.set(call_sid, state)

    return render(request, 'step2.xml')

def step2(request):
    call_sid = request.GET.get('CallSid', '')
    selection = int(request.GET.get('Digits', 0))

    state = cache.get(call_sid, {})
    state['step2_selection'] = selection
    cache.set(call_sid, state)

    return render(request, 'final_step.xml')


def final_step(request):
    call_sid = request.GET.get('CallSid', '')
    selection = int(request.GET.get('Digits', 1))

    state = cache.get(call_sid, {})
    state['final_step_selection'] = selection

    Backend.process_user_selections(state)

    return render(request, 'thank_you.xml')

{% endcodeblock %}

At each step Django will update the current state associated with this call and return
a [TwiML](https://www.twilio.com/docs/api/twiml) XML response. `CallSid` is a handy unique
identifier provided by Twilio.

I am using the latest [django-s3-cache](http://github.com/atodorov/django-s3-cache) version
which properly works with directories. When going to production that will likely switch to
Amazon ElastiCache.



