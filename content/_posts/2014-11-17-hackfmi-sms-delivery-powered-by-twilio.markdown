---
layout: post
Title: HackFMI SMS Delivery Powered by Twilio
date: 2014-11-17 15:00
comments: true
categories: ['Twilio']
---

Ten days ago the regular [HackFMI](http://hackfmi.com/) competition was held.
This year they tried sending SMS notifications to all participants which was powered
by [Twilio](http://twilio.com) both in terms of infrastructure and cost.

**Twilio** provided a **20$ upgrade code** valid in the next 6 months for all new accounts.
This was officially announced at the opening ceremony (although at the last possible time) of the
competition, however no teams decided to incorporate SMS/Voice into their games.
I'm a little disappointed by this fact.

In terms of software a simple [Django app](https://github.com/atodorov/django-twilio-sms)
was used. It is by no means production ready but does the job and was quick to write.

A little over 300 messages were sent with number distribution as follows:

* Mtel - 166
* Globul - 86
* Vivacom - 50

The total price for Mtel and Globul messages is roughly the same because sending
SMS to Globul via Twilio is as twice expensive. The total sums up to about 25 $.
HackFMI team used two accounts to send the messages - one using the provided
20$ upgrade code from Twilio and the second one was mine.

