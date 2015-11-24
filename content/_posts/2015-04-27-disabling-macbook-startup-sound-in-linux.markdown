---
layout: post
title: "Disabling MacBook Startup Sound in Linux"
date: 2015-04-27 23:23
comments: true
categories: ['Mac', 'fedora.planet', 'RHEL']
---

There is an easy way to disable the MacBook startup sound
(boot chime) even after wiping out OS X and installing Linux.

This sound can be easily disabled if you mute the volume in OS X
and shutdown the computer. The value is stored in NVRAM.


1. Reboot the computer and hold Cmd+Alt(Option)+R. This will start
OS X Internet recovery mode;
2. Open the terminal and issue the following command

        nvram SystemAudioVolume=%00

3. Reboot.

Voila. In Linux try this:

    # efivar -l | grep SystemAudioVolume
     7c436110-ab2a-4bbb-a880-fe41995c9f82-SystemAudioVolume
     7c436110-ab2a-4bbb-a880-fe41995c9f82-SystemAudioVolumeDB
    
    # efivar -n 7c436110-ab2a-4bbb-a880-fe41995c9f82-SystemAudioVolume -p
    GUID: 7c436110-ab2a-4bbb-a880-fe41995c9f82
    Name: "SystemAudioVolume"
    Attributes:
        Non-Volatile
        Boot Service Access
        Runtime Service Access
    Value:
    00000000  00                                                |.               |
    
    # efivar -n 7c436110-ab2a-4bbb-a880-fe41995c9f82-SystemAudioVolumeDB -p
    GUID: 7c436110-ab2a-4bbb-a880-fe41995c9f82
    Name: "SystemAudioVolumeDB"
    Attributes:
        Non-Volatile
        Boot Service Access
        Runtime Service Access
    Value:
    00000000  00 
    #

**Note 1**: Before disabling both variables had non zero values. Also *SystemAudioVolumeDB*
doesn't seem to have any effect.

**Note 2:** RHEL or CentOS users need to rebuild *efivar* from the 
[Fedora src.rpm](https://kojipkgs.fedoraproject.org//packages/efivar/0.14/1.fc22/src/efivar-0.14-1.fc22.src.rpm).

**Note 3:** several Internet sources suggest that writing EFI variables from Linux
may sometimes corrupt your Apple firmware. I didn't research this any further. If you
happen to figure out how to successfully write to these variables under Linux please let
everyone know in the comments (in case OS X recovery mode goes missing, you know).

Thanks to my reader Alexander, who
[gave me the hint](/blog/2015/04/26/installing-red-hat-enterprise-linux-7-on-macbook-air-2015/#disqus_thread)
in a previous blog post.
