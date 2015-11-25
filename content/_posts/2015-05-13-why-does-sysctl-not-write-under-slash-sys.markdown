---
layout: post
Title: Why does sysctl not write under /sys
date: 2015-05-13 12:34
comments: true
Tags: fedora.planet
---

Recently I've been looking into 
[fixing tilde and Fn keys mapping for MacBook Air](/blog/2015/04/30/fixing-tilde-and-function-keys-mapping-for-macbook-air-on-linux/)
and thought I could use `sysctl` to permanently set the desired values. Unfortunately this is not
possible. `sysctl` can only write under `/proc/sys` and this is 
[hard-coded in the source](https://gitlab.com/procps-ng/procps/blob/master/sysctl.c#L54):

    static const char PROC_PATH[] = "/proc/sys/";


IMO this is relatively easy to patch and allow sysctl to read/write values under /sys.
The only open question I see is backward compatibility - maybe adding new parameter (e.g. --sysfs)
or adding extended sytax e.g. if variable name starts with / then treat it as absolute path.

I've asked sysctl maintainers on the 
[procps mailing list](http://www.freelists.org/post/procps/Can-we-make-sysctl-readwrite-sys-values-along-with-procsys)
but so far got no answer. 

Is anyone else interested in this? How do you set parameter values under /sys then ?


**NOTE:** for my particular purposes I could have used config files under
*/etc/modprobe.d/* or a startup script (I used that) instead.
