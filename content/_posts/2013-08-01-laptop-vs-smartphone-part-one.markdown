---
layout: post
Title: Laptop vs Smartphone, Part 1, Requirements
date: 2013-08-01 21:02
comments: true
Tags: BlackBerry
Slug: laptop-vs-smartphone-part-one
---

As some of you may know or have heard I'm in the process of  ditching my 
[Lenovo X220](http://amzn.to/12y5hwp) in favor of a smartphone. The ultimate
goal is to not need a personal computer at all and use only one device for
all my processing needs. Everything else can be conveniently migrated to
the cloud. The current favorite device is [BlackBerry Z10](http://amzn.to/12y4ewJ)
but that may change as I explore the smartphone world and my requirements.

This is my list of requirements, mainly for my own reference but you are welcome
to comment and give me suggestions how to migrate.

Hardware
--------

    +-----------------------+--------------------+-------------------+-------------------+
    | Requirement           | Lenovo X220        | BlackBerry Z10    | Notes             |
    +-----------------------+--------------------+-------------------+-------------------+
    | Network Connectivity  | RJ-45, Wi-Fi,      | Wi-Fi, 3G         |                   |
    |                       | 3G (optional)      |                   |                   |
    |                       | or USB modem       |                   |                   |
    +-----------------------+--------------------+-------------------+-------------------+
    | Battery Life          | 8 hrs idle, 9 cell | 13 days standby   | TBC               |
    |                       | 5-6 hrs networking | 10 hrs talk (3G)  |                   |
    +-----------------------+--------------------+-------------------+-------------------+
    | Display Size          | 1366x768, 96 DPI   | 1280x768, 356 PPI |                   |
    +-----------------------+--------------------+-------------------+-------------------+
    | Sunlight Readable     | Very hard even at  | Yes, even at      | TBC               |
    |                       | full brightness    | medium brightness |                   |
    +-----------------------+--------------------+-------------------+-------------------+
    | Weight                | around 1,5 kg      | 136g              |                   |
    +-----------------------+--------------------+-------------------+-------------------+
    | Docking Capability    | Integrated or USB  | unknown, N/A      | for desk usage    |
    +-----------------------+--------------------+-------------------+-------------------+
    | External video/audio  | VGA,  3,5mm jack   | Micro HDMI, 3,5mm | presentation mode |
    +-----------------------+--------------------+-------------------+-------------------+
    | External Connectivity | USB 2.0 and 3.0,   | micro USB 2.0,    |                   |
    |                       | Bluetooth          | Bluetooth, NFC    |                   |
    +-----------------------+--------------------+-------------------+-------------------+
    | Storage               | 320GB, ~ 50G used  | 16GB internal     | TODO: speed test  |
    |                       |                    | 32GB microSD      |                   |
    +-----------------------+--------------------+-------------------+-------------------+
    | RAM                   | 8GB                | 2GB               | TBC               |
    |                       |                    | 1GB on Dev device |                   |
    +-----------------------+--------------------+-------------------+-------------------+
    | CPU virtualization    | Yes, full virt     | No                | loading other OS  |
    |                       |                    |                   | ** critical       |
    +-----------------------+--------------------+-------------------+-------------------+
    | UPDATE 2013-08-03     | Yes                | No,               |** essential       |
    | USB host mode         |                    | ETA 10.2 Aug 2013 |                   |
    +-----------------------+--------------------+-------------------+-------------------+


**Notes:**

* I need a test for the battery life of a smartphone in use and while traveling
and connected to the Internet. Data shown is as given by manufacturer. Talking
from experience the 10 hrs talk time are roughly equivalent to 10 hrs of Internet
and apps usage. I have to charge my Z10 almost every day and I still don't use it
that actively.

* The displays of all recent smartphones are far better than notebooks. I can read
my phone outside but haven't actually tried a direct sunlight exposure. Will do this
and update with more info.

* Speed storage may be an issue, although I don't use storage intensive applications.
Will test this and report with more info.

* RAM is a **BIG** issue. Currently my desktop utilizes around 4GB but on x86_64
objects are bigger (Python objects are 4x compared to i386). I've previously used
an old Lenovo T60 with only 2GB of RAM and i386 environment. Didn't have any issues.

On Z10 the memory is not utilized in the best fashion. Something is eating away
RAM and I'm left with around 150MB of free memory after some phone use. For one
`/tmp ` is mounted directly into RAM and some apps are misbehaving. I've seen a low
cost Android tablets and phones running with 512MB of RAM. Need to investigate more.

* Virtualization and most importantly USB pass-through is a critical issue. I have
a proprietary smart-card electronic signature device which needs to continue working.
I have no problems running a cloud instance but haven't figured out how to do USB
pass-through between local hardware and cloud instance.


* **UPDATE 2013-08-03**: USB host mode is essential for some docking hardware. This means that the phone
will be able to connect to external USB devices such as USB drives or cameras.
For more info read
[here](http://forums.crackberry.com/news-rumors-f40/usb-host-mode-806937/) and
[here](https://developer.blackberry.com/native/download/roadmap/).


Software
--------

Here things get hairy as I use quite a lot of software.

    +----------------------+---------------------+------------------------------------------------+
    | Linux Software       | BlackBerry 10 OS    | Notes                                          |
    +----------------------+---------------------+------------------------------------------------+
    | UPDATE 2013-08-02    | Built-in            | I need to check if BB encryption meets my      |
    | LUKS/disk encryption |                     | enterprise requirements.                       |
    +----------------------+---------------------+------------------------------------------------+
    | Bash shell           | v5.2.14 99/07/13.2  | I have no idea how compatible PD KSH is.       |
    |                      |                     | For serious scripting I will need Bash anyway. |
    +----------------------+---------------------+------------------------------------------------+
    | GNU Coreutils        |                     | Some tools are present but not all.            |
    |                      |                     | No idea if GNU or other implementation (BSD)   |
    +----------------------+---------------------+------------------------------------------------+
    | OpenSSH              |                     | There are some apps available, need to test UX |
    +----------------------+---------------------+------------------------------------------------+
    | Serial console       |                     | I use several on Linux, mostly                 |
    | access tools         |                     | `conserver-client`.                            |
    +----------------------+---------------------+------------------------------------------------+
    | Kerberos tools       |                     | Internal apps I use authenticate with Kerberos |
    +----------------------+---------------------+------------------------------------------------+
    | Cisco VPN            | Built-in            | Several GW types supported. Not tested.        |
    +----------------------+---------------------+------------------------------------------------+
    | OpenVPN client       | N/A AFAIK           |                                                |
    +----------------------+---------------------+------------------------------------------------+
    | Python 2.6           | Python 2.7 and 3.2  | `devuser` has no permissions to run Python 2.7 |
    +----------------------+---------------------+------------------------------------------------+
    | Ruby                 |                     | Mostly for cloud related mgmt commands.        |
    +----------------------+---------------------+------------------------------------------------+
    | Firefox              | built-in Browser    | Missing plugins functionality.                 |
    +----------------------+---------------------+------------------------------------------------+
    | Thunderbird          | BlackBerry Hub      | Messaging experience on BB is quite cool but   |
    | email & RSS          | RSS Savvy           | missing multiple sender addresses and RSS does |
    |                      |                     | not integrate into BB Hub                      |
    +----------------------+---------------------+------------------------------------------------+
    | Social Networks      | Stand alone apps    | Integrate well with BlackBerry Hub.            |
    +----------------------+---------------------+------------------------------------------------+
    | Rhythmbox            | built-in player     | Not tested but I need to bookmark online radio |
    | Totem (audio)        |                     | stations.                                      |
    +----------------------+---------------------+------------------------------------------------+
    | Totem (video)        | built-in player     | Works fine, already watched MPEG v4 videos.    |
    +----------------------+---------------------+------------------------------------------------+
    | Transmission         | N/A                 | No bittorrent client apps available but        |
    |                      |                     | BB fork for Transmission exists on GitHub.     |
    +----------------------+---------------------+------------------------------------------------+
    | Evince (PDF)         | Adobe Reader        | Not tested yet.                                |
    +----------------------+---------------------+------------------------------------------------+
    | -                    | Kindle              | eBook reader, Android version. Works fine.     |
    +----------------------+---------------------+------------------------------------------------+
    | Libre Office         | Docs To Go          | MS office compatible, displays presentations,  |
    |                      |                     | limited editing, mostly read-only mode.        |
    +----------------------+---------------------+------------------------------------------------+
    | Text Editor          | Several             | None tested yet.                               |
    +----------------------+---------------------+------------------------------------------------+
    | Purple               | Yaairc              | I need IRC and XMPP (Gtalk) mostly. Dodo seems |
    |                      | Dodo                | to have some issues, I can't receive messages. |
    +----------------------+---------------------+------------------------------------------------+
    | Twinkle (SIP)        |                     | Several available but not tested.              |
    +----------------------+---------------------+------------------------------------------------+
    | GIMP                 |                     | Image cropping and resizing mostly.            |
    +----------------------+---------------------+------------------------------------------------+
    | Inkscape             |                     | Simple drawings and graphics.                  |
    +----------------------+---------------------+------------------------------------------------+
    | CUPS (printing)      |                     | Should be able to print stuff.                 |
    +----------------------+---------------------+------------------------------------------------+
    | xSane (scanner)      |                     | Documents scanning, can do pictures too.       |
    +----------------------+---------------------+------------------------------------------------+

I will describe my software use cases in details in a later update. Most important of all is
a nice text editor to write code and text (mainly this blog) and the shell tools.


Roll-out Plan
-------------

To make things easier I will first transition entertainment and personal
activities and later work related ones. 

In the next few days I will start
by exploring all the hardware requirements first and update this blog with
some of the findings. Along with this I will share the personal activities
progress.


