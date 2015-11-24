---
layout: post
Title: Duplicate Amazon SQS Messages Cause Multiple Emails
date: 2013-12-06 22:47
comments: true
categories: ['cloud', 'Amazon', 'SQS', 'SES']
---

Beware if using Amazon Simple Queue Service to send email messages!
Sometime SQS messages are duplicated which results in multiple copies of
the messages being sent. This happened today at [Difio](http://www.dif.io)
and is really annoying to users. In this post I will explain why there is no easy
way of fixing it.

{% blockquote Amazon FAQ %}
Q: Can a deleted message be received again?

Yes, under rare circumstances you might receive a previously deleted message again.
This can occur in the rare situation in which a DeleteMessage operation doesn't
delete all copies of a message because one of the servers in the distributed
Amazon SQS system isn't available at the time of the deletion. That message copy
can then be delivered again. You should design your application so that no errors
or inconsistencies occur if you receive a deleted message again.
{% endblockquote %}

In my case the cron scheduler logs say:

    >>> <AsyncResult: a9e5a73a-4d4a-4995-a91c-90295e27100a>

While on the worker nodes the logs say:

    [2013-12-06 10:13:06,229: INFO/MainProcess] Got task from broker: tasks.cron_monthly_email_reminder[a9e5a73a-4d4a-4995-a91c-90295e27100a]
    [2013-12-06 10:18:09,456: INFO/MainProcess] Got task from broker: tasks.cron_monthly_email_reminder[a9e5a73a-4d4a-4995-a91c-90295e27100a]

This clearly shows the same message (see the UUID) has been processed twice!
This resulted in hundreds of duplicate emails :(.

Why This Is Hard To Fix
-----------------------

There are two basic approaches to solve this issue:

* Check some log files or database for previous record of the message having
been processed;
* Use idempotent operations that if you process the message again, you
get the same results, and that those results don't create duplicate files/records.

The problem with checking for duplicate messages is: 

*  There is a race condition between marking the message as processed and the
second check;
* You need to use some sort of locking mechanism to safe-guard against the race condition;
* In the event of an eventual consistency of the log/DB you can't guarantee that
the previous attempt will show up and so can't guarantee that you won't process
the message twice.

All of the above don't seem to work well for distributed applications not to mention
Difio processes millions of messages per month, per node and the logs are quite big.


The second option is to have control of the Message-Id or some other email header
so that the second message will be discarded either at the server (Amazon SES in my case)
or at the receiving MUA. I like this better but I don't think it is technically possible
with the current environment. Need to check though. 


I've asked AWS support to look into
[this thread](https://forums.aws.amazon.com/thread.jspa?threadID=140782) and hopefully
they will have some more hints. If you have any other ideas please post in the comments!
Thanks!

