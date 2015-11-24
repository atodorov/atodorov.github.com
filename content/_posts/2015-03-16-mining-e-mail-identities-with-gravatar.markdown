---
layout: post
Title: Mining E-mail Identities with Gravatar
date: 2015-03-16 23:16
comments: true
categories: 
---

Recently I've laid my hands on a list of little over 7000 email addresses.
This begs the question how much of them are still in use and what for ?

My data is not fresh so I've uploaded the list to Facebook and created a custom
audience. 2400 of 7129 addresses were recognized - 30% of these addresses are
on Facebook and easy to target! Need to figure out which ones. 

I could have tried some sort of batch search combined with the custom audience
functionality but I didn't find an API for that and decided not to bother.
Instead I've opted for Gravatar.


{% codeblock lang:bash gravatars.sh %}
#!/bin/bash

while read LINE; do
    HASH=`echo -n $LINE | md5sum | cut -f1 -d' '`
    wget "http://gravatar.com/avatar/$HASH" -O "$LINE"
done < /dev/stdin
{% endcodeblock %}


Feed `gravatars.sh` with the email list and it will download all images to the
current working directory and use the address as the file name. After 
`md5sum *@* | cut -f1 -d' ' | sort | uniq -c` I quickly noticed the following:

* 4563 addresses have the `a1719586837f0fdac8835f74cf4ef04a` check-sum; These are
not found on Gravatar.
* 2400 addresses have the `d5fe5cbcc31cff5f8ac010db72eb000c` check-sum. These are
addresses which are registered with Gravatar but didn't bother to change the default
image.
* 166 remaining addresses, each with a different check-sum. These have their custom
pictures uploaded to Gravatar and probably much more actively used.


A second check with Facebook reveals 900 out of these 2566 addresses were recognized.
This begs the question is Facebook showing incorrect stats or are there 1500 addresses
using Gravatar (or have used at some point) which are not on Facebook ?

At least some of the remaining 4000 addresses are still active and used to send emails.
Next I will be looking for ways to identify them. Any suggestions and comments are more
than welcome!



