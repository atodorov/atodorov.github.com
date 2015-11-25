---
layout: post
Title: SMS PIN Verification with Twilio and Django
date: 2014-03-19 11:41
comments: true
Tags: Django, cloud, Twilio
---

This is a quick example of SMS PIN verification using Twilio cloud services and
Django which I did for a small site recently.

![SMS PIN form](/images/sms_pin.png "SMS PIN form")

The page template contains the following HTML snippet

{% codeblock lang:html %}
<input type="text" id="mobile_number" name="mobile_number" placeholder="111-111-1111" required>
<button class="btn" type="button" onClick="send_pin()"><i class="icon-share"></i> Get PIN</button>
{% endcodeblock %}

and a JavaScript function utilizing jQuery:

{% codeblock lang:javascript %}
function send_pin() {
    $.ajax({
                {% raw %}url: "{% url 'ajax_send_pin' %}",{% endraw %}
                type: "POST",
                data: { mobile_number:  $("#mobile_number").val() },
            })
            .done(function(data) {
                alert("PIN sent via SMS!");
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
                alert(errorThrown + ' : ' + jqXHR.responseText);
            });
}
{% endcodeblock %}

Then create the following views in Django:

{% codeblock lang:python %}
def _get_pin(length=5):
    """ Return a numeric PIN with length digits """
    return random.sample(range(10**(length-1), 10**length), 1)[0]


def _verify_pin(mobile_number, pin):
    """ Verify a PIN is correct """
    return pin == cache.get(mobile_number)


def ajax_send_pin(request):
    """ Sends SMS PIN to the specified number """
    mobile_number = request.POST.get('mobile_number', "")
    if not mobile_number:
        return HttpResponse("No mobile number", mimetype='text/plain', status=403)

    pin = _get_pin()

    # store the PIN in the cache for later verification.
    cache.set(mobile_number, pin, 24*3600) # valid for 24 hrs

    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
                        body="%s" % pin,
                        to=mobile_number,
                        from_=settings.TWILIO_FROM_NUMBER,
                    )
    return HttpResponse("Message %s sent" % message.sid, mimetype='text/plain', status=200)

def process_order(request):
    """ Process orders made via web form and verified by SMS PIN. """
    form = OrderForm(request.POST or None)

    if form.is_valid():
        pin = int(request.POST.get("pin", "0"))
        mobile_number = request.POST.get("mobile_number", "")

        if _verify_pin(mobile_number, pin):
            form.save()
            return redirect('transaction_complete')
        else:
            messages.error(request, "Invalid PIN!")
    else:
        return render(
                    request,
                    'order.html',
                    {
                        'form': form
                    }
                )
{% endcodeblock %}

PINs are only numeric and are stored in the CACHE instead of the database which
I think is simpler and less expensive in terms of I/O operations.
