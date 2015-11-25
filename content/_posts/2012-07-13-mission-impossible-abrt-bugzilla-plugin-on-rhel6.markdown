---
layout: post
Title: Mission Impossible - ABRT Bugzilla Plugin on RHEL6
date: 2012-07-13 13:21
comments: true
Tags: 'QA', 'RHEL'
---

Some time ago Red Hat introduced Automatic Bug Reporting Tool to their Red Hat Enterprise Linux
platform. This is a nice tool which lets users report bugs easily to Red Hat.
However one of the plugins in the latest version doesn't seem usable at all.

First make sure you have `libreport-plugin-bugzilla` package installed. This is the plugin to
report bugs directly to [Bugzilla](https://bugzilla.redhat.com). It may not be installed by default
because customers are supposed to report issues to Support first - this is why they pay anyway.
If you are a tech savvy user though, you may want to skip Support and go straight to the developers.

To enable Bugzilla plugin: 

* Edit the file `/etc/libreport/events.d/bugzilla_event.conf` change the line

        EVENT=report_Bugzilla analyzer=libreport reporter-bugzilla -b

to

        EVENT=report_Bugzilla reporter-bugzilla -b


* Make sure ABRT will collect meaningful backtrace. If debuginfo is missing it will not let you continue.
Edit the file `/etc/libreport/events.d/ccpp_event.conf`. There should be something like this:

        EVENT=analyze_LocalGDB analyzer=CCpp
                abrt-action-analyze-core --core=coredump -o build_ids &&
                abrt-action-generate-backtrace &&
                abrt-action-analyze-backtrace
                (
                    bug_id=$(reporter-bugzilla -h `cat duphash`) &&
                    if test -n "$bug_id"; then
                        abrt-bodhi -r -b $bug_id
                    fi
                )

* Change it to look like this - i.e. add the missing `/usr/libexec/` line:

        EVENT=analyze_LocalGDB analyzer=CCpp
                abrt-action-analyze-core --core=coredump -o build_ids &&
                /usr/libexec/abrt-action-install-debuginfo-to-abrt-cache --size_mb=4096 &&
                abrt-action-generate-backtrace &&
                abrt-action-analyze-backtrace &&
                (
                    bug_id=$(reporter-bugzilla -h `cat duphash`) &&
                    if test -n "$bug_id"; then
                        abrt-bodhi -r -b $bug_id
                    fi
                )


Supposedly after everything is configured properly ABRT will install missing debuginfo packages,
generate the backtrace and let you report it to Bugzilla. Because of
[bug 759443](https://bugzilla.redhat.com/show_bug.cgi?id=759443) this will not happen.

To work around the problem you can try to manually install the missing debuginfo packages.
Go to your system profile in RHN and subscribe the system to all appropriate debuginfo channels.
Then install the packages. In my case:

        # debuginfo-install firefox


And finally - [bug 800754](https://bugzilla.redhat.com/show_bug.cgi?id=800754) which was already reported!
