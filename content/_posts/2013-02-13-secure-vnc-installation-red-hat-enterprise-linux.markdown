---
layout: post
Title: Secure VNC Installation of Red Hat Enterprise Linux 6
date: 2013-02-13 15:40
comments: true
Tags: RHEL, tips
Slug: secure-vnc-installation-red-hat-enterprise-linux
---

<img src="/images/rhel6_welcome.png" alt="RHEL 6 welcome screen" />
Image CC-BY-SA,
[Red Hat](https://access.redhat.com/knowledge/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Installation_Guide/sn-welcome-s390.html)


From time to time I happen to remotely
[install Red Hat Enterprise Linux](http://otb.bg)
servers via the Internet.
When the system configuration is not decided upfront you need
to use interactive mode. This means VNC in my case.

In this tutorial I will show you how to make VNC installations more secure
when using public networks to connect to the server.

Meet your tools
----------------

Starting with Red Hat Enterprise Linux 6 and all the latest Fedora releases, the
installer supports SSH connections during install.

> Note that by default, root has a blank password.
> 
> If you don't want any user to be able to ssh in and have full access to your hardware, 
> you must specify sshpw for username root. Also note that if Anaconda fails to parse the 
> kickstart file, it will allow anyone to login as root and have full access to your hardware.
> 
> Fedora Kickstart manual https://fedoraproject.org/wiki/Anaconda/Kickstart#sshpw

Preparation
-----------

We are going to use SSH port forwarding and tunnel VNC traffic through it.
Create a kickstart file as shown below:

    install
    url --url http://example.com/path/to/rhel6
    lang en_US.UTF-8
    keyboard us
    network --onboot yes --device eth0 --bootproto dhcp
    vnc --password=s3cr3t
    sshpw --user=root s3cr3t

The first 5 lines configure the loader portion of the installer. They will setup
networking and fetch the installer image called stage2. This is completely automated.
**NB:** If you miss some of the lines or have a syntax error the installer will prompt for
values. You either need a remote console access or somebody present at the server console!

The last 2 lines configure passwords for VNC and SSH respectively.

Make this file
[available](https://fedoraproject.org/wiki/Anaconda/Kickstart#Chapter_6._Making_the_Kickstart_File_Available)
over HTTP(S), FTP or NFS.

**NB:** Make sure that the file is available on the same network where your server is,
or use HTTPS if on public networks.


Installation
------------

Now, using your favorite installation media start the
installation process like this: 

    boot: linux sshd=1 ks=http://example.com/ks.cfg


After a minute or more the installer will load stage2, with the
interactive VNC session. You need to know the IP address or hostname
of the server. Either look into DHCP logs, have somebody look at the
server console and tell you that (it's printed on tty1) or script it in
a [%pre](https://fedoraproject.org/wiki/Anaconda/Kickstart#Chapter_4._Pre-installation_Script)
script which will send you an email for example.

When ready, redirect one of your local ports through SSH to the VNC port on the server:

    $ ssh -L 5902:localhost:5901 -N root@server.example.com


Now connect to DISPLAY :2 on your system to begin the installation:

    $ vncviewer localhost:2 &


Warning Bugs Present
---------------------

As it happens, I find bugs everywhere. This is no exception.
Depending on your network/DHCP configuration IP address during install may 
change mid-air and cause VNC client connection to freeze.

The reason for this bug is evident from the code (rhel6-branch):

    :::python iw/timezone_gui.py
    if not anaconda.isKickstart:
        self.utcCheckbox.set_active(not hasWindows(anaconda.id.bootloader))

    :::python textw/timezone_text.py
    if not anaconda.isKickstart and not hasWindows(anaconda.id.bootloader):
        asUtc = True

Because we are using a kickstart file Anaconda will assume the system clock **DOES NOT**
use UTC. If you forget to configure it manually you may see time on the server shifting
back or forward (depending on your timezone) while installing. If your DHCP is configured
for short lease time the address will expire before the installation completes. When new
address is requested from DHCP it may be different and this will cause your VNC connection
to freeze.

To workaround this issue select the appropriate value for the system clock settings during install
and possibly use static IP address during the installation.


Feedback
--------

As always I'd love to hear your feedback in the comments section below. Let me know 
your tips and tricks to perform secure remote installations using public networks.
