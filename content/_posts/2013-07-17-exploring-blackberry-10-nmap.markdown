---
layout: post
title: "Exploring BlackBerry 10 - nmap"
date: 2013-07-17 23:16
comments: true
categories: ['BlackBerry', 'Z10']
---

This is the first post in upcoming series while I explore my
[BlackBerry Z10](http://amzn.to/12y4ewJ) device and figure out what's on it.

First configure Z10 for
[USB networking](/blog/2013/07/17/tip-how-to-enable-usb-networking-between-blackberry-z10-and-red-hat-enterprise-linux-6/).
Then from `Settings - Security and Privacey - Development Mode` turn 
`Use Development Mode` to `On`.
From my Linux box I run nmap against the usb (169.254.0.1) and
wi-fi (192.168.0.100) addresses of Z10:

{% codeblock lang:bash %}

$ nmap 169.254.0.1

Starting Nmap 5.51 ( http://nmap.org ) at 2013-07-17 23:03 EEST
Nmap scan report for 169.254.0.1
Host is up (0.00087s latency).
Not shown: 994 closed ports
PORT     STATE    SERVICE
80/tcp   open     http
139/tcp  open     netbios-ssn
443/tcp  open     https
445/tcp  open     microsoft-ds
1111/tcp filtered lmsocialserver
8443/tcp open     https-alt

Nmap done: 1 IP address (1 host up) scanned in 21.41 seconds


$ nmap 192.168.0.100

Starting Nmap 5.51 ( http://nmap.org ) at 2013-07-17 23:04 EEST
Nmap scan report for 192.168.0.100
Host is up (0.0035s latency).
Not shown: 998 closed ports
PORT     STATE    SERVICE
443/tcp  open     https
1111/tcp filtered lmsocialserver

Nmap done: 1 IP address (1 host up) scanned in 15.64 seconds

{% endcodeblock %}

Firefox says the certificate used for https is invalid:

        The certificate is not trusted because it is self-signed.
        The certificate is only valid for PlayBook: 1c:69:a5:d0:10:cd

`1c:69:a5:d0:10:cd` is the wi-fi interface MAC address.
All the http ports produce a 404 with `index.html` not found!

Trying some UDP scan:

{% codeblock lang:bash %}

# nmap -sU 169.254.0.1

Starting Nmap 5.51 ( http://nmap.org ) at 2013-07-17 23:32 EEST
Nmap scan report for 169.254.0.1
Host is up (0.00075s latency).
Not shown: 995 closed ports
PORT     STATE         SERVICE
67/udp   open|filtered dhcps
68/udp   open|filtered dhcpc
137/udp  open          netbios-ns
138/udp  open|filtered netbios-dgm
5353/udp open          zeroconf
MAC Address: 1E:69:A5:D0:10:CD (Unknown)

# nmap -sU 192.168.0.100

Starting Nmap 5.51 ( http://nmap.org ) at 2013-07-17 23:33 EEST
Nmap scan report for 192.168.0.100
Host is up (0.065s latency).
Not shown: 995 closed ports
PORT     STATE         SERVICE
67/udp   open|filtered dhcps
68/udp   open|filtered dhcpc
137/udp  open|filtered netbios-ns
138/udp  open|filtered netbios-dgm
5353/udp open|filtered zeroconf
MAC Address: 1C:69:A5:D0:10:CD (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 143.65 seconds

{% endcodeblock %}
