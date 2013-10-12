---
layout: post
title: "Tip: Installing Missing debuginfo Packages for ABRT"
date: 2013-10-12 14:38
comments: true
categories: ['tips', 'Fedora']
---

!["Reporting disabled"](/images/reporting_disabled.png "Reporting disabled")

Every once in a while ABRT will tell you that reporting is disabled because
backtrace is unusable. What it means is that it can't read some of the debugging
symbols and the most likely reason for that is debuginfo packages are missing.

To install them first locate the directory containing the files for that particular
crash. Use the `executable` file to find out if you are looking into the correct
directory. Then use this one liner to install the missing debuginfo packages.

    # pwd
    /var/tmp/abrt/ccpp-2013-10-10-15:55:18-15533
    # cat backtrace | grep lib | tr -s ' ' | cut -f4 -d' ' | sort | uniq | grep "/" | xargs rpm -qf --qf "%{name}\n" | xargs debuginfo-install -y
