---
layout: post
title: "Importing vCard Contacts To BlackBerry Z10 Sucks"
date: 2013-07-14 21:09
comments: true
categories: ['BlackBerry', 'Z10', 'Nokia']
---

I can honestly state that [BlackBerry Z10](http://amzn.to/12y4ewJ) sucks big
time when it comes to importing your contacts from another non-BlackBerry
device. I've been struggling to transfer my contacts from
[Nokia 6303](http://amzn.to/10USRm2) to the Z10 for one day.

I tried a simple sync of the contacts from Nokia to Z10 over Bluetooth but
that failed miserably, telling me the Z10 doesn't support this functionality.
This is what to do: 

* On Nokia - `Settings - Sync and backup - Create backup`;
* Then navigate to `Apps - Extras - Memory card - Backup files`;
* Select the most recent backup file, e.g. `Backup000.NBF` and 
transfer it via Bluetooth (or USB cable) to my laptop;

For the record: this is a ZIP file with different extension. I've tried also
to transfer it to the Z10 and open from File manager but to no avail.

* Just unzip the file on the computer;
* When extracted it will create multiple directories with meaningless names.
Just find whatever you need - in my case this was the `contacts/` directory
containing hundreds of `.vcf` files;
* Combine all the `.vcf` files into one. On Linux this is done with

        cat *.vcf > ../all.vcf

For the record: I've tried also sending all of these files to Z10. Via the 
File manager individual vCards open just fine but you need to `Save` them one
by one. The combined vCard file didn't display correctly at all. Showed only one
contact.

* Then go to Gmail (or any other CardDAV service) and import all your vCards.
Go to `Contacts - More - Import` - and select the combined vCard file since Gmail
doesn't support multi-file uploads;

* On your BlackBerry go to `Settings - Accounts` and add your Gmail account.
By default this will create profiles for mail, calendar and contacts which will
be synchronized with the device.

**WARNING** I had my Gmail previously configured on the Z10. Despite the account
was configured to re-sync every 15 minutes it took around 2 hours for phone numbers
to sync. And to make it worse there is no button for manual re-sync.


All of this done I have thousands of contacts on my Z10 spread across phone numbers,
emails, vCards and contacts from social networks. I've noticed some of them (my guess
those that had the same email or name) combined auto-magically. The rest can easily be
linked together using the Contacts app Link functionality.



For the record: It is also possible to send vCards one by one directly from Nokia to
Z10 via Bluetooth. The trouble is that for every entry you need to go through several
layers of menu options and confirmations. This makes it impractical.


Summary
-------

* Importing hundreds of contacts from Nokia to BlackBerry Z10 is MIA;
* BB Contacts app (and BB Hub) is cool but has some bugs;
* Needs manual contact re-sync button;
* Gmail re-sync took longer than expected;
* Contacts Link feature can be improved and made more easy to use, e.g.
    + grid style display
    + multiple select and link
    + swipe and link, etc;

* The current Link interface is sub-optimal
    - select a contact
    - tap Links
    - tap Add Link
    - tap Search
    - type and find the entries you'd like to link;

* The current Link interface is buggy - when searching contacts to add
as links it shows the currently opened contact too. Luckily it doesn't
crash when the same entry is selected :). I've tried.

This is with OS Version 10.0.10.261.

