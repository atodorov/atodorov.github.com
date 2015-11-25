---
layout: post
Title: django-social-auth tip: Reminder of Login Provider
date: 2013-03-14 12:04
comments: true
Tags: 'tips', 'Django', 'django-social-auth'
---

Every now and then users forget their passwords. This is why I prefer using
OAuth and social network accounts like GitHub or Twitter. But what do you do
when somebody forgets which OAuth provider they used to login to your site?
Your website needs a reminder. This is how to implement one if using
django-social-auth.


Back-end
-------

Create a similar view on your Django back-end

{% codeblock views.py lang:python %}
def ajax_social_auth_provider_reminder(request):
    """
        Remind the user which social auth provider they used to login.
    """
    if not request.POST:
        return HttpResponse("Not a POST", mimetype='text/plain', status=403)

    email = request.POST.get('email', "")
    email = email.strip()
    if not email or (email.find("@") == -1):
        return HttpResponse("Invalid address!", mimetype='text/plain', status=400)

    try:
        user = User.objects.filter(email=email, is_active=True).only('pk')[0]
    except:
        return HttpResponse("No user with address '%s' found!" % email, mimetype='text/plain', status=400)

    providers = []
    for sa in UserSocialAuth.objects.filter(user=user.pk).only('provider'):
        providers.append(sa.provider.title())

    if len(providers) > 0:
        send_templated_mail(
            template_name='social_provider_reminder',
            from_email='Difio <reminder@dif.io>',
            recipient_list=[email],
            context={'providers' : providers},
        )
        return HttpResponse("Reminder sent to '%s'" % email, mimetype='text/plain', status=200)
    else:
        return HttpResponse("User found but no social providers found!", mimetype='text/plain', status=400)
{% endcodeblock %}

This example assumes it is called via POST request which contains the email address.
All responses are handled at the front-end via JavaScript. If a user with the specified
email address exists this address will receive a reminder listing all social auth providers
associated with the user account.

Front-end
--------

On the browser side I like to use [Dojo](http://dojotoolkit.org).
Here is a simple script which connects to a form and POSTs the data
back to the server.

{% codeblock lang:javascript %}
require(["dojo"]);
require(["dijit"]);

function sendReminderForm(){
    var form = dojo.byId("reminderForm");

    dojo.connect(form, "onsubmit", function(event){
        dojo.stopEvent(event);
        dijit.byId("dlgForgot").hide();
        var xhrArgs = {
            form: form,
            handleAs: "text",
            load: function(data){alert(data);},
            error: function(error, ioargs){alert(ioargs.xhr.responseText);}
        };
        var deferred = dojo.xhrPost(xhrArgs);
    });
}
dojo.ready(sendReminderForm);
{% endcodeblock %}

You can try this out at [Difio](http://www.dif.io) and let me know how it works for you!

