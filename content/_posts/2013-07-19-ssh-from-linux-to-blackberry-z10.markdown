---
layout: post
Title: SSH from Linux to BlackBerry Z10
date: 2013-07-19 23:31
comments: true
Tags: tips, BlackBerry, Z10, RHEL
---

You can SSH into a [BlackBerry Z10](http://amzn.to/12y4ewJ) device even on Linux.
I'm using Red Hat Enterprise Linux 6 and here is how to establish the connection.


1) [Enable USB networking](/blog/2013/07/17/tip-how-to-enable-usb-networking-between-blackberry-z10-and-red-hat-enterprise-linux-6/)
between your Linux desktop and the Z10;

2) Install the [Momentics IDE](https://developer.blackberry.com/develop/platform_choice/ndk.html).
You need it to create debug tokens and to start the SSH daemon on the device;

3) Obtain [signing keys](https://www.blackberry.com/SignedKeys/codesigning.html)
and create a debug token by following the wizard in the IDE.
I just started a new project and followed the instructions;

4) Install debug token on device using the IDE. From `Window - Preferences` select
`Blackberry - Signing`. Just create and deploy the debug token on the device. Mine was
automatically discovered so I just had to follow the prompts;

5) Reboot and re-enable development mode (I'm not sure if this was necessary);

6) Generate a **4096 bit** key for SSH. Smaller keys won't work. You can use your
current key if it is 4096 bit;

{% codeblock lang:bash %}
$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/atodorov/.ssh/id_rsa): /home/atodorov/.rim/testKey_4096_rsa
/home/atodorov/.rim/testKey_4096_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/atodorov/.rim/testKey_4096_rsa.
Your public key has been saved in /home/atodorov/.rim/testKey_4096_rsa.pub.
The key fingerprint is:
77:73:55:03:e1:fc:5b:df:a6:e9:2c:b4:d4:1e:0c:b2 atodorov@redbull.mini
The key's randomart image is:
+--[ RSA 4096]----+
|             oo..|
|            o   o|
|             o  .|
|          . . .. |
|        S .oo+...|
|         .E.oo+ =|
|           o o o+|
|            o..+ |
|             o=  |
+-----------------+
{% endcodeblock %}

7) Update key permissions, since ssh complains:

        $ chmod 600 ~/.rim/testKey_4096_rsa.pub


8) By default SSH is not listening on your BlackBerry. Use the `blackberry-connect`
command to start the SSH daemon on the device. It will upload your public SSH key
to the device and start the SSH daemon on the other side. `password` is your device
password;

{% codeblock lang:bash %}
$ pwd
/home/atodorov/bbndk/host_10_1_0_231/linux/x86/usr/bin

$ ./blackberry-connect 169.254.0.1 -password 123456 -sshPublicKey ~/.rim/testKey_4096_rsa.pub
Info: Connecting to target 169.254.0.1:4455
Info: Authenticating with target 169.254.0.1:4455
Info: Encryption parameters verified
Info: Authenticating with target credentials.
Info: Successfully authenticated with target credentials.
Info: Sending ssh key to target 169.254.0.1:4455
Info: ssh key successfully transferred.
Info: Successfully connected. This application must remain running in order to use debug tools. Exiting the application will terminate this connection.
{% endcodeblock %}

9) Check if SSH is running on the device

{% codeblock lang:bash %}
$ nmap 169.254.0.1

Starting Nmap 5.51 ( http://nmap.org ) at 2013-07-18 10:19 EEST
Stats: 0:00:01 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 14.30% done; ETC: 10:20 (0:00:06 remaining)
Nmap scan report for 169.254.0.1
Host is up (0.00097s latency).
Not shown: 991 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
139/tcp  open  netbios-ssn
443/tcp  open  https
445/tcp  open  microsoft-ds
1111/tcp open  lmsocialserver
5555/tcp open  freeciv
8000/tcp open  http-alt
8443/tcp open  https-alt

Nmap done: 1 IP address (1 host up) scanned in 12.47 seconds
{% endcodeblock %}

10)  Use SSH with the specified key to connect to the Z10. Username is `devuser`.
Here's a simple session:

{% codeblock lang:bash %} 
$ ssh -i ~/.rim/testKey_4096_rsa devuser@169.254.0.1
$ 
$ pwd
/accounts/devuser
$ uname -a 
QNX atodorovZ10 8.0.0 2013/05/02-08:42:48EDT OMAP4470_ES1.0_HS_London_Rev:08 armle
$ date
Fri Jul 19 23:39:19 EEST 2013
$ ifconfig 
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 33192
    inet 127.0.0.1 netmask 0xff000000
    inet6 ::1 prefixlen 128
    inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
tiw_drv0: flags=8c02<BROADCAST,OACTIVE,SIMPLEX,MULTICAST> mtu 1500
    address: 1c:69:a5:d0:10:cd
tiw_sta0: flags=40008c43<UP,BROADCAST,RUNNING,OACTIVE,SIMPLEX,MULTICAST,ACCEPTRTADV> mtu 1500
    address: 1c:69:a5:d0:10:cd
    inet 192.168.0.100 netmask 0xffffff00 broadcast 192.168.0.255
    inet6 fe80::1e69:a5ff:fed0:10cd%tiw_sta0 prefixlen 64 scopeid 0x12
tiw_p2pdev0: flags=8c02<BROADCAST,OACTIVE,SIMPLEX,MULTICAST> mtu 1500
    address: 1c:69:a5:d0:10:cd
tiw_p2pgrp0: flags=8c02<BROADCAST,OACTIVE,SIMPLEX,MULTICAST> mtu 1500
    address: 1c:69:a5:d0:10:cd
tiw_ibss0: flags=8c02<BROADCAST,OACTIVE,SIMPLEX,MULTICAST> mtu 1500
    address: 1c:69:a5:d0:10:cd
pflog0: flags=0 mtu 33192
lo2: flags=8048<LOOPBACK,RUNNING,MULTICAST> mtu 33192
cellular0: flags=8810<POINTOPOINT,SIMPLEX,MULTICAST> mtu 1500
cellular1: flags=8810<POINTOPOINT,SIMPLEX,MULTICAST> mtu 1500
cellular2: flags=8810<POINTOPOINT,SIMPLEX,MULTICAST> mtu 1500
cellular3: flags=8810<POINTOPOINT,SIMPLEX,MULTICAST> mtu 1500
cellular4: flags=8810<POINTOPOINT,SIMPLEX,MULTICAST> mtu 1500
bptp0: flags=8043<UP,BROADCAST,RUNNING,MULTICAST> mtu 1356
    inet6 fe80::1e69:a5ff:fed0:10cd%bptp0 prefixlen 64 scopeid 0x2d
    inet6 fd02:42ac:77b2:d543:c158:fabb:6276:80e6 prefixlen 8
ecm0: flags=8a43<UP,BROADCAST,RUNNING,ALLMULTI,SIMPLEX,MULTICAST> mtu 1500
    address: 1e:69:a5:d0:10:cd
    inet 169.254.0.1 netmask 0xfffffffc broadcast 169.254.0.3
    inet6 fe80::1c69:a5ff:fed0:10cd%ecm0 prefixlen 64 scopeid 0x2e
{% endcodeblock %}


**IMPORTANT:** you can also use the WiFi address of the device to pass to
`backberry-connect` and ssh. It works for me.

I'm starting to explore the dark world of QNX in the next couple of days
and will keep you posted! Until then - happy hacking.



