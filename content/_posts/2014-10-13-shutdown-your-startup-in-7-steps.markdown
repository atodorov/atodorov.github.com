---
layout: post
Title: Shutdown Your Startup in 7 Steps
date: 2014-10-13 14:17
comments: true
categories: ['start-up']
---

A month ago one of my startups Difio stopped working forever.
This is the story of how to go about shutting down a working
web service and not about why it came around to this.


Step #1: Disable new registrations
-----------------------------------

You obviously need to make sure new customers
arriving at your web site will not sing up to only find the service is
shutting down later.

Disable whatever sign-on/registration system you have in place
but leave currently registered users to login as they wish.


Step #2: Disable payments
-------------------------

Difio had paying customers, just not enough of them and it was based on
a subscription model which was automatically renewed without any interaction
from the customer.

The first thing I did was to disable all payments for the service which
was quite easy (just a few comments) because Difio used an external payment
processor.

Next thing was to go through all subscriptions that were still active and
cancel them. This prevented the payment processor to automatically charge
the customers next time their subscription renewal was due.

Because all subscriptions were charged in advance and when canceled were
still considered active (due to expire at some later date) Difio had to
keep operating at least one month after all subscriptions have been canceled.


Step #3: Notify all customers that you are shutting down
---------------------------------------------------------

I scheduled this to happen right after the last subscription was canceled.
An email to everyone who registered to the website and a blog post should work
for most startups. See ours [here](http://www.dif.io/blog/2014/08/10/difio-is-shutting-down/).

Make sure to provide a gratis period if necessary. Difio had a gratis period
of one month after the shutdown announcement.

Step #4: Disable all external triggers
--------------------------------------

Difio was a complex piece of software which relied on external triggers like
web hooks and repetitive tasks executed by cron.

Disabling these will prevent external services or hosting providers 
getting errors about your URLs not being accessible. It is just polite
to do so. 

You may want to keep these still operational during the gratis period
before the physical shutdown or disable them straight away. In Difio's
case they were left operational because there were customers who have paid
in advance and relied on this functionality.


Step #5: Prepare your 'Service Disabled' banner
-----------------------------------------------

You will probably want to let people know why something isn't working
as it used (or is expected) to be. A simple page explaining that
you're going to shut down should be enough. 

Difio required the user to be logged in to see most of the website.
This made it very easy to redirect everything to the same page.
A few more places were linking to public URLs which were manually rewritten
to point to the same 'Service Disabled' page.

It is the same page used previously to redirect new registrations to.


Step #6: Terminate all processing resources
--------------------------------------------

Difio used both AWS EC2 instances and an OpenShift PaaS instance to do its
processing. Simply terminating all of them was enough. The only thing left
is a couple of static HTML pages behind the domain.


Step #7: Database archival
--------------------------

The last thing you need to do is archive your database. Although the
startup is out of business already you have gathered additional information
which may come handy at a later time.

Difio didn't collect any personal information about its users, except email
and didn't store financial information either. This made it safe to just make
a backup of the database and leave it lurking around on disk. 

However beware 
if you have collected personal and/or financial information from your customers.
You may want to erase/anonymize some of it before doing your backups and
probably safeguard them from unauthorized access.


That's it, your startup is officially dead now! Let me know if I've missed 
something in the comments below.


