Title: 3 Bugs in Grajdanite
date: 2016-04-17 10:34
comments: true
Tags: QA,
og_image: images/grajdanite/bug1.png
twitter_image: images/grajdanite/bug1.png

[Grajdanite](https://play.google.com/store/apps/details?id=com.xevica.grajdanite)
is a social app that allows everyone (in Bulgaria) to photograph vehicles in breach of
traffic rules or misbehaving drivers, upload them online and ask them to
appologize. They also offer some functionality to report offenses to the
authorities are are partnering with local municipalities and law enforcement
agencies to make the process easier. And of course this is one of my
favorite apps as of latest.


Missing Icon in My Profile
---------------------------

![Missing icon](/images/grajdanite/bug1.png "Missing icon bug")

The more offenses you report the more points you get.
Points lead to ranks (e.g. junior officer, senior officer, etc).
The page showing your points and rank is missing an icon. If I had to guess
this is the badge which comes with different ranks.

Preloading the Very First Form Value
-------------------------------------

![Preloading gone wrong](/images/grajdanite/bug2.png "Preloading gone wrong")

Once you opt for reporting an offence to the authorities you need to specify
the address where the action took place, your name, phone and e-mail address.
The app correctly saves your details and pre-loads them later to speed-up
data entry. However I typed my e-mail wrong the very first time. Now every time
I want to report something the app pre-loads the wrong address. Even after I
change it to the correct one, the next time I still see the very first, wrong value.

In code this is probably something like:

    # pre-load
    form.email = store.get("email", "")
    form.show()
    
    # save
    if form.firstTime():
        store.save("email", form.email)

The fix is to save the form value every time (not expensive operation here)
or check if the current value is different from the last time and only then save it.


DST and Time Sync
------------------

The last bug is in the app confirmation email. Once an offence is reported the
user receives an email with the uploaded photo and the information they have
provided. The email includes a timestamp. However the email timestamp is 
1 hour off from the actual time. In particular it is 1 hour behind the current time
and I think the email server doesn't follow summer time.

The result from this is:

* Report an offense
* Wait 1 minute for the email to be received;
* The email says the offense happened 1 hour ago!

All of these bugs are in version 3.86.3, which is the latest one.
