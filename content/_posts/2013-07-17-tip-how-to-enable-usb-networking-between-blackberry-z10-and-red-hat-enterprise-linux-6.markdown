---
layout: post
Title: Tip: How To Enable USB Networking Between BlackBerry Z10 and Red Hat Enterprise Linux 6
date: 2013-07-17 11:06
comments: true
Tags: 'tips', 'RHEL', 'BlackBerry', 'Z10'
---

On Linux there is a feature called USB networking which provides you with a 
TCP/IP connection to another device connected via USB cable. Here is how to
connect your [BlackBerry Z10](http://amzn.to/12y4ewJ)
to your Linux laptop over USB. I use Red Hat Enterprise Linux but should work
out of the box for other distros too.

Connect the Z10 to your laptop:

        $ lsusb
        Bus 001 Device 005: ID 0fca:8020 Research In Motion, Ltd. Blackberry Playbook (CD-Rom mode)

By default many USB devices will present a virtual CD-ROM with drivers for Windows.
This is the case here too. To change it go to `Settings - Storage and Access` and
set `USB Connection` to `Connect to Mac`!

If necessary plug out and back in the Z10. 

        $ lsusb
        Bus 001 Device 007: ID 0fca:8013 Research In Motion, Ltd.

        $ ifconfig
        usb0      Link encap:Ethernet  HWaddr 1E:69:A5:D0:11:0A  
                  inet addr:169.254.0.2  Bcast:169.254.0.3  Mask:255.255.255.252
                  inet6 addr: fe80::1c69:a5ff:fed0:110a/64 Scope:Link
                  UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                  RX packets:49 errors:0 dropped:0 overruns:0 frame:0
                  TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
                  collisions:0 txqueuelen:1000 
                  RX bytes:16002 (15.6 KiB)  TX bytes:1152 (1.1 KiB)



**IMPORTANT:** In the same `Storage and Access` screen scroll down to
`USB Mass Storage` and turn it `Off`. If you don't do this your Z10 will appear
as USB flash drive and no USB networking will be available. This is how it looks:


        $ lsusb
        Bus 001 Device 008: ID 0fca:8014 Research In Motion, Ltd. 


**IMPORTANT:** If you need your Z10 storage accessible together with USB networking
you can try accessing the device over Wi-Fi.
Configure it from the same `Storage and Access` screen. Then your device will be
available through Samba on its wireless IP address. I've tried it, works for me!


You don't need anything else to get this working. All set!

My intention is to use either USB networking or Wi-Fi to
[connect to the Z10 shell](http://supportforums.blackberry.com/t5/Testing-and-Deployment/How-to-use-blackberry-connect-to-Enable-SSH-Access/ta-p/1515447)
and explore it in more details.
