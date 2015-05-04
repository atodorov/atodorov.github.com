---
layout: post
title: "Installing Red Hat Enterprise Linux 7 on MacBook Air 2015"
date: 2015-04-26 20:33
comments: true
categories: ['fedora.planet', 'RHEL', 'Mac']
---

Recently I've upgraded to a new 
<a href="http://www.amazon.com/gp/product/B00UGECEUY/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00UGECEUY&linkCode=as2&tag=atodorovorg-20&linkId=3YENGI5TIYKEC5GM">MacBook Air</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B00UGECEUY" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
(13 inch, early 2015) laptop and luckily enough I'm running
Red Hat Enterprise Linux 7.1 on it. Here is how to install it.

Prepare boot media
-------------------

The easiest method is to boot from a USB stick which holds
either the entire DVD or just boot.iso. Since I happened to find a 1GB only USB stick I
went for the boot.iso. `dd if=boot.iso of=/dev/sdb` is the only thing you need to prepare
the boot media.

Initial boot
-------------

![Mac boot menu](/images/mac/boot_menu.jpg "Mac boot menu")

While computer is booting hold the (left) Alt (Option) key to enter *Startup Manager*.
Wait a second or two before it displays your local hard drive and the USB boot media.
Select the option *EFI boot* to boot the anaconda installer.

Installation
------------

Booting from a boot.iso means I need to use the network to grab the rest of the installation.
Because the wireless card needs proprietary drivers
I've tried both USB to Ethernet adapter and USB tethering with my phone.

**Note:** initially I have forgotten to plug in my USB networking card which resulted in 
[bug #1191286](https://bugzilla.redhat.com/show_bug.cgi?id=1191286). After cold-plugging and
rebooting the system everything was fine. Subsequently I don't see any problems with the
USB networking card. The bug should be fixed in RHEL 7.2 btw.

**Note:** I've been using a
<a href="http://www.amazon.com/gp/product/B002PONXAI/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B002PONXAI&linkCode=as2&tag=atodorovorg-20&linkId=N4KGQKYSBSDWMMM6">USB docking station from Plugable</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B002PONXAI" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
for years because their products are Linux friendly. In particular the networking chip is ASIX and
there is no problems with drivers for Linux.

**UPDATE 2015-05-04:**
You should also be able to use a Thunderbolt to Ethernet adapter which is more
common for Apple users. [See here for more info](/blog/2015/05/04/thunderbolt-to-ethernet-adapter-on-linux/);

In my case I've wiped out the entire SSD disk b/c I don't care about dual boot.
Previously I've heard about anaconda crashing while it tries to detect the Mac OS file system.
I've played around with Rawhide before going for RHEL 7.1 and didn't see any problems related to
foreign filesystems.

I've gone with the default partitioning scheme while slightly modifing the partition sizes, etc.


Post install
------------

There are several issues which still need attention. I didn't have enough time in the last few
days to check these out:

**Things which work**

* GNOME 3 sucks big time. Fortunately I was able to install MATE Desktop from EPEL;
* Wireless card needs drivers; I've managed to compile them myself, 
[see here](/blog/2015/04/27/compiling-broadcom-wl-kmod-wifi-driver-for-rhel-7/);
* Display brightness doesn't seem to work at all. On top of that the display goes full black
after suspend-resume. I could barely see anything on it. 
[Fixed here](http://localhost:4000/blog/2015/04/29/fixing-display-brightness-on-macbook-air-with-rhel-7/)!
* There is a very annoying boot chime <strike>which I have no idea how to disable</strike>
[Fixed here](/blog/2015/04/27/disabling-macbook-startup-sound-in-linux/);
* The onboard keyboard is quite annoying for previous ThinkPad user like myself. Most
importantly I need to press Fn to activate the F1, F2, etc keys which I use a lot in mcedit.
[Fixed here](/blog/2015/04/30/fixing-tilde-and-function-keys-mapping-for-macbook-air-on-linux/);
* Output sound works - both speakers and headphones;
* Microphone works (tested with a hands free device);
* Power manager was reporting my battery life totally wrong but after a full discharge/recharge
it seems to have calibrated itself;
* ATrpms and EPEL are still missing some codecs for RHEL 7 which means no movies;
 codecs seem to work now with the [NUX Desktop](http://li.nux.ro/repos.html)
repos. Not sure what I was missing when testing it initially;
* *UPDATE 2015-05-04:* I do have a Thunderbolt to Ethernet adapter and hot-plug seems to work
despite claims that this is not supported in Linux.
[See here for more info](/blog/2015/05/04/thunderbolt-to-ethernet-adapter-on-linux/);


**Things that don't work yet**

* *UPDATE 2015-04-30:* I'd like to remap the Cmd key to the Menu key found in PC keyboards;
* Camera doesn't work, reverse engineering a [driver](https://github.com/patjak/bcwc_pcie)
 is in progress;
* I'm missing the [ThinkLight](http://www.thinkwiki.org/wiki/ThinkLight) from my X220,
however the integrated Broadcom FaceTime HD camera doesn't seem to have a LED flash
which can be repurposed for this task;
* I need a CPU temperature monitor and maybe CPU fan speed needs adjustments;
* I have not yet tested presenting via projector but already have a few ideas how to make it work;

**UPDATE 2015-04-28:**
Check the list above for links to wifi and backlight drivers and how to disable the boot chime.

**UPDATE 2015-04-29:**
You can find precompiled RPMS in my
[Macbook Air RHEL 7 repository](/blog/2015/04/29/rhel-7-repository-for-macbook-air/).

**UPDATE 2015-04-30:**
Added more links and split the list into stuff which already works and stuff that doesn't.

**UPDATE 2015-05-04:**
Added info about Thunderbolt to Ethernet adapter.


Fedora 22 on MacBook Air
-------------------------

I did try Fedora 22 Beta and experienced 
[bug #1215458](https://bugzilla.redhat.com/show_bug.cgi?id=1215458).
Also for some reason the installation hit an error downloading a package and didn't let me retry
but forced me to exit the process.


I'll continue posting my updates until the system runs smoothly like it is supposed to.


Hardware info
-------------

**ADDED ON 2015-05-02**

{% codeblock %}
# dmidecode 
# dmidecode 2.12
# SMBIOS entry point at 0x8afae000
SMBIOS 2.7 present.
32 structures occupying 1663 bytes.
Table at 0x8AFAD000.

Handle 0x0000, DMI type 7, 19 bytes
Cache Information
    Socket Designation: L1 Cache
    Configuration: Enabled, Not Socketed, Level 1
    Operational Mode: Write Back
    Location: Internal
    Installed Size: 32 kB
    Maximum Size: 32 kB
    Supported SRAM Types:
	Synchronous
    Installed SRAM Type: Synchronous
    Speed: Unknown
    Error Correction Type: Parity
    System Type: Data
    Associativity: 8-way Set-associative

Handle 0x0001, DMI type 7, 19 bytes
Cache Information
    Socket Designation: L1 Cache
    Configuration: Enabled, Not Socketed, Level 1
    Operational Mode: Write Back
    Location: Internal
    Installed Size: 32 kB
    Maximum Size: 32 kB
    Supported SRAM Types:
	Synchronous
    Installed SRAM Type: Synchronous
    Speed: Unknown
    Error Correction Type: Parity
    System Type: Instruction
    Associativity: 8-way Set-associative

Handle 0x0002, DMI type 7, 19 bytes
Cache Information
    Socket Designation: L2 Cache
    Configuration: Enabled, Not Socketed, Level 2
    Operational Mode: Write Back
    Location: Internal
    Installed Size: 256 kB
    Maximum Size: 256 kB
    Supported SRAM Types:
	Synchronous
    Installed SRAM Type: Synchronous
    Speed: Unknown
    Error Correction Type: Single-bit ECC
    System Type: Unified
    Associativity: 8-way Set-associative

Handle 0x0003, DMI type 7, 19 bytes
Cache Information
    Socket Designation: L3 Cache
    Configuration: Enabled, Not Socketed, Level 3
    Operational Mode: Write Back
    Location: Internal
    Installed Size: 4096 kB
    Maximum Size: 4096 kB
    Supported SRAM Types:
	Synchronous
    Installed SRAM Type: Synchronous
    Speed: Unknown
    Error Correction Type: Multi-bit ECC
    System Type: Unified
    Associativity: 16-way Set-associative

Handle 0x0004, DMI type 4, 42 bytes
Processor Information
    Socket Designation: U3E1
    Type: Central Processor
    Family: Core i7
    Manufacturer: Intel(R) Corporation
    ID: D4 06 03 00 FF FB EB BF
    Signature: Type 0, Family 6, Model 61, Stepping 4
    Flags:
	FPU (Floating-point unit on-chip)
	VME (Virtual mode extension)
	DE (Debugging extension)
	PSE (Page size extension)
	TSC (Time stamp counter)
	MSR (Model specific registers)
	PAE (Physical address extension)
	MCE (Machine check exception)
	CX8 (CMPXCHG8 instruction supported)
	APIC (On-chip APIC hardware supported)
	SEP (Fast system call)
	MTRR (Memory type range registers)
	PGE (Page global enable)
	MCA (Machine check architecture)
	CMOV (Conditional move instruction supported)
	PAT (Page attribute table)
	PSE-36 (36-bit page size extension)
	CLFSH (CLFLUSH instruction supported)
	DS (Debug store)
	ACPI (ACPI supported)
	MMX (MMX technology supported)
	FXSR (FXSAVE and FXSTOR instructions supported)
	SSE (Streaming SIMD extensions)
	SSE2 (Streaming SIMD extensions 2)
	SS (Self-snoop)
	HTT (Multi-threading)
	TM (Thermal monitor supported)
	PBE (Pending break enabled)
    Version: Intel(R) Core(TM) i7-5650U CPU @ 2.20GHz
    Voltage: 1.0 V
    External Clock: 25 MHz
    Max Speed: 2200 MHz
    Current Speed: 3100 MHz
    Status: Populated, Enabled
    Upgrade: <OUT OF SPEC>
    L1 Cache Handle: 0x0001
    L2 Cache Handle: 0x0002
    L3 Cache Handle: 0x0003
    Serial Number:  
    Asset Tag:  
    Part Number:  
    Core Count: 2
    Core Enabled: 2
    Thread Count: 4
    Characteristics:
	64-bit capable
	Multi-Core
	Hardware Thread
	Execute Protection
	Enhanced Virtualization
	Power/Performance Control

Handle 0x0005, DMI type 0, 24 bytes
BIOS Information
    Vendor: Apple Inc.
    Version: MBA71.88Z.0166.B00.1502131457
    Release Date: 02/13/2015
    ROM Size: 8192 kB
    Characteristics:
	PCI is supported
	BIOS is upgradeable
	BIOS shadowing is allowed
	Boot from CD is supported
	Selectable boot is supported
	ACPI is supported
	Smart battery is supported
	Function key-initiated network boot is supported
	UEFI is supported
    BIOS Revision: 0.1

Handle 0x0006, DMI type 1, 27 bytes
System Information
    Manufacturer: Apple Inc.
    Product Name: MacBookAir7,2
    Version: 1.0
    Serial Number: C1MPF52YG944
    UUID: 25EF0280-EC82-42B0-8FB6-10ADCCC67C02
    Wake-up Type: Power Switch
    SKU Number: System SKU#
    Family: Mac

Handle 0x0007, DMI type 2, 17 bytes
Base Board Information
    Manufacturer: Apple Inc.
    Product Name: Mac-937CB26E2E02BB01
    Version: MacBookAir7,2
    Serial Number: C07511704VSG92GA1
    Asset Tag: Base Board Asset Tag#
    Features:
	Board is a hosting board
    Location In Chassis: Part Component
    Chassis Handle: 0x0008
    Type: Motherboard
    Contained Object Handles: 0

Handle 0x0008, DMI type 3, 24 bytes
Chassis Information
    Manufacturer: Apple Inc.
    Type: Laptop
    Lock: Not Present
    Version: Mac-937CB26E2E02BB01
    Serial Number: C1MPF52YG944
    Asset Tag: Chassis Board Asset Tag#
    Boot-up State: Safe
    Power Supply State: Safe
    Thermal State: Safe
    Security Status: None
    OEM Information: 0x00000000
    Height: Unspecified
    Number Of Power Cords: Unspecified
    Contained Elements: 0
    SKU Number: Not Specified

Handle 0x0009, DMI type 8, 9 bytes
Port Connector Information
    Internal Reference Designator: Not Specified
    Internal Connector Type: None
    External Reference Designator: USB0
    External Connector Type: Access Bus (USB)
    Port Type: USB

Handle 0x000A, DMI type 8, 9 bytes
Port Connector Information
    Internal Reference Designator: Not Specified
    Internal Connector Type: None
    External Reference Designator: USB1
    External Connector Type: Access Bus (USB)
    Port Type: USB

Handle 0x000B, DMI type 8, 9 bytes
Port Connector Information
    Internal Reference Designator: Not Specified
    Internal Connector Type: None
    External Reference Designator: Audio Line In
    External Connector Type: Mini Jack (headphones)
    Port Type: Audio Port

Handle 0x000C, DMI type 8, 9 bytes
Port Connector Information
    Internal Reference Designator: Not Specified
    Internal Connector Type: None
    External Reference Designator: Thunderbolt
    External Connector Type: None
    Port Type: Other

Handle 0x000D, DMI type 8, 9 bytes
Port Connector Information
    Internal Reference Designator: Microphone
    Internal Connector Type: Other
    External Reference Designator: Not Specified
    External Connector Type: None
    Port Type: None

Handle 0x000E, DMI type 8, 9 bytes
Port Connector Information
    Internal Reference Designator: Speaker
    Internal Connector Type: Other
    External Reference Designator: Not Specified
    External Connector Type: None
    Port Type: None

Handle 0x000F, DMI type 41, 11 bytes
Onboard Device
    Reference Designation: Integrated Video Controller
    Type: Video
    Status: Enabled
    Type Instance: 1
    Bus Address: 0000:00:00.0

Handle 0x0010, DMI type 41, 11 bytes
Onboard Device
    Reference Designation: Azalia Audio Codec
    Type: Sound
    Status: Enabled
    Type Instance: 1
    Bus Address: 0000:00:00.0

Handle 0x0011, DMI type 41, 11 bytes
Onboard Device
    Reference Designation: SATA
    Type: SATA Controller
    Status: Enabled
    Type Instance: 1
    Bus Address: 0000:00:00.0

Handle 0x0012, DMI type 13, 22 bytes
BIOS Language Information
    Language Description Format: Abbreviated
    Installable Languages: 1
	en
    Currently Installed Language: en

Handle 0x0013, DMI type 22, 26 bytes
Portable Battery
    Location: Not Specified
    Manufacturer: Not Specified
    Name: Not Specified
    Design Capacity: Unknown
    Design Voltage: Unknown
    SBDS Version: Not Specified
    Maximum Error: 0%
    SBDS Serial Number: 0000
    SBDS Manufacture Date: 1980-00-00
    SBDS Chemistry: Not Specified
    OEM-specific Information: 0x00000000

Handle 0x0014, DMI type 32, 11 bytes
System Boot Information
    Status: No errors detected

Handle 0x0015, DMI type 131, 6 bytes
OEM-specific Type
    Header and Data:
	83 06 15 00 06 07

Handle 0x0016, DMI type 133, 12 bytes
OEM-specific Type
    Header and Data:
	85 0C 16 00 02 00 00 00 00 00 00 00

Handle 0x0017, DMI type 128, 88 bytes
OEM-specific Type
    Header and Data:
	80 58 17 00 03 00 00 00 36 F5 03 FC 3F FF 03 FC
	02 00 03 00 00 00 00 00 00 00 99 FF FF FF AF FF
	00 00 B0 FF FF FF D4 FF 00 00 D7 FF FF FF D9 FF
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00

Handle 0x0018, DMI type 134, 20 bytes
OEM-specific Type
    Header and Data:
	86 14 18 00 32 2E 32 37 46 30 31 00 00 00 00 00
	00 00 00 00

Handle 0x0019, DMI type 16, 23 bytes
Physical Memory Array
    Location: System Board Or Motherboard
    Use: System Memory
    Error Correction Type: None
    Maximum Capacity: 8 GB
    Error Information Handle: Not Provided
    Number Of Devices: 2

Handle 0x001A, DMI type 17, 34 bytes
Memory Device
    Array Handle: 0x0019
    Error Information Handle: Not Provided
    Total Width: 64 bits
    Data Width: 64 bits
    Size: 4096 MB
    Form Factor: SODIMM
    Set: None
    Locator: DIMM0
    Bank Locator: BANK 0
    Type: DDR3
    Type Detail: Synchronous
    Speed: 1600 MHz
    Manufacturer: 0x80AD
    Serial Number: 0x00000000
    Asset Tag: Not Specified
    Part Number: 0x483943434E4E4E384A544D4C41522D4E544D
    Rank: Unknown
    Configured Clock Speed: 1600 MHz

Handle 0x001B, DMI type 130, 186 bytes
OEM-specific Type
    Header and Data:
	82 BA 1B 00 1A 00 00 00 B0 00 91 20 F1 03 04 12
	05 0A 03 11 01 08 0A 00 00 01 78 78 90 50 90 11
	50 E0 10 04 3C 3C 01 90 00 00 00 00 00 00 00 00
	00 A8 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80
	AD 01 00 00 00 00 00 00 57 FB 48 39 43 43 4E 4E
	4E 38 4A 54 4D 4C 41 52 2D 4E 54 4D 00 00 80 AD
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00

Handle 0x001C, DMI type 17, 34 bytes
Memory Device
    Array Handle: 0x0019
    Error Information Handle: Not Provided
    Total Width: 64 bits
    Data Width: 64 bits
    Size: 4096 MB
    Form Factor: SODIMM
    Set: None
    Locator: DIMM0
    Bank Locator: BANK 1
    Type: DDR3
    Type Detail: Synchronous
    Speed: 1600 MHz
    Manufacturer: 0x80AD
    Serial Number: 0x00000000
    Asset Tag: Not Specified
    Part Number: 0x483943434E4E4E384A544D4C41522D4E544D
    Rank: Unknown
    Configured Clock Speed: 1600 MHz

Handle 0x001D, DMI type 130, 186 bytes
OEM-specific Type
    Header and Data:
	82 BA 1D 00 1C 00 00 00 B0 00 91 20 F1 03 04 12
	05 0A 03 11 01 08 0A 00 00 01 78 78 90 50 90 11
	50 E0 10 04 3C 3C 01 90 00 00 00 00 00 00 00 00
	00 A8 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80
	AD 01 00 00 00 00 00 00 57 FB 48 39 43 43 4E 4E
	4E 38 4A 54 4D 4C 41 52 2D 4E 54 4D 00 00 80 AD
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	00 00 00 00 00 00 00 00 00 00

Handle 0x001E, DMI type 19, 31 bytes
Memory Array Mapped Address
    Starting Address: 0x0000000000000000k
    Ending Address: 0x00000001FFFFFFFFk
    Range Size: 8 GB
    Physical Array Handle: 0x0019
    Partition Width: 0

Handle 0xFEFF, DMI type 127, 4 bytes
End Of Table

# uname -a
Linux aero 3.10.0-229.1.2.el7.x86_64 #1 SMP Fri Mar 6 17:12:08 EST 2015 x86_64 x86_64 x86_64 GNU/Linux

# lsusb
Bus 001 Device 002: ID 0a5c:4500 Broadcom Corp. BCM2046B1 USB 2.0 Hub (part of BCM2046 Bluetooth)
Bus 001 Device 003: ID 05ac:0291 Apple, Inc. 
Bus 002 Device 002: ID 05ac:8406 Apple, Inc. 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 006: ID 05ac:828f Apple, Inc. 

# lspci
00:00.0 Host bridge: Intel Corporation Broadwell-U Host Bridge -OPI (rev 09)
00:02.0 VGA compatible controller: Intel Corporation Broadwell-U Integrated Graphics (rev 09)
00:03.0 Audio device: Intel Corporation Broadwell-U Audio Controller (rev 09)
00:14.0 USB controller: Intel Corporation Wildcat Point-LP USB xHCI Controller (rev 03)
00:16.0 Communication controller: Intel Corporation Wildcat Point-LP MEI Controller #1 (rev 03)
00:1b.0 Audio device: Intel Corporation Wildcat Point-LP High Definition Audio Controller (rev 03)
00:1c.0 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #1 (rev e3)
00:1c.1 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #2 (rev e3)
00:1c.2 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #3 (rev e3)
00:1c.4 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #5 (rev e3)
00:1c.5 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #6 (rev e3)
00:1f.0 ISA bridge: Intel Corporation Wildcat Point-LP LPC Controller (rev 03)
00:1f.3 SMBus: Intel Corporation Wildcat Point-LP SMBus Controller (rev 03)
00:1f.6 Signal processing controller: Intel Corporation Wildcat Point-LP Thermal Management Controller (rev 03)
02:00.0 Multimedia controller: Broadcom Corporation 720p FaceTime HD Camera
03:00.0 Network controller: Broadcom Corporation BCM4360 802.11ac Wireless Network Adapter (rev 03)
04:00.0 SATA controller: Samsung Electronics Co Ltd Device a801 (rev 01)

# efivar --list
605dab50-e046-4300-abb6-3dd810dd8b23-MokListRT
8be4df61-93ca-11d2-aa0d-00e098032b8c-BootCurrent
8be4df61-93ca-11d2-aa0d-00e098032b8c-ErrOutDev
8be4df61-93ca-11d2-aa0d-00e098032b8c-ConOutDev
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-gfx-saved-config-restore-status
8be4df61-93ca-11d2-aa0d-00e098032b8c-LangCodes
7c436110-ab2a-4bbb-a880-fe41995c9f82-BootCampProcessorPstates
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-SSN
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-GR_CAUSE
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-FirmwareFeatures
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-FirmwareFeaturesMask
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-HW_ICT
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-HW_MLB
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-MLB
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-HW_ROM
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-ROM
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-HW_BID
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-HardwareBootMode
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-BBIF
8be4df61-93ca-11d2-aa0d-00e098032b8c-ConOut
eb704011-1402-11d3-8e77-00a0c969723b-MTC
7c436110-ab2a-4bbb-a880-fe41995c9f82-SystemAudioVolume
36c28ab5-6566-4c50-9ebd-cbb920f83843-current-network
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-current-network
7c436110-ab2a-4bbb-a880-fe41995c9f82-SystemAudioVolumeDB
7c436110-ab2a-4bbb-a880-fe41995c9f82-boot-gamma
7c436110-ab2a-4bbb-a880-fe41995c9f82-backlight-level
8be4df61-93ca-11d2-aa0d-00e098032b8c-BootOrder
8be4df61-93ca-11d2-aa0d-00e098032b8c-Boot0001
8be4df61-93ca-11d2-aa0d-00e098032b8c-Boot0000
4d1ede05-38c7-4a6a-9cc6-4bcca8b38c14-AAPL,PathProperties0000
8d63d4fe-bd3c-4aad-881d-86fd974bc1df-last-oslogin-ident
36c28ab5-6566-4c50-9ebd-cbb920f83843-preferred-count
36c28ab5-6566-4c50-9ebd-cbb920f83843-preferred-networks
7c436110-ab2a-4bbb-a880-fe41995c9f82-fmm-computer-name
7c436110-ab2a-4bbb-a880-fe41995c9f82-LocationServicesEnabled
7c436110-ab2a-4bbb-a880-fe41995c9f82-efi-boot-device
7c436110-ab2a-4bbb-a880-fe41995c9f82-efi-boot-device-data
8be4df61-93ca-11d2-aa0d-00e098032b8c-Boot0080
af9ffd67-ec10-488a-9dfc-6cbf5ee22c2e-AcpiGlobalVariable
7c436110-ab2a-4bbb-a880-fe41995c9f82-bluetoothActiveControllerInfo
7c436110-ab2a-4bbb-a880-fe41995c9f82-bluetoothInternalControllerInfo
8be4df61-93ca-11d2-aa0d-00e098032b8c-fpf_provisioned
8be4df61-93ca-11d2-aa0d-00e098032b8c-epid_provisioned
8be4df61-93ca-11d2-aa0d-00e098032b8c-BootFFFF
8be4df61-93ca-11d2-aa0d-00e098032b8c-Lang
7c436110-ab2a-4bbb-a880-fe41995c9f82-ALS_Data
8be4df61-93ca-11d2-aa0d-00e098032b8c-MemoryConfih
8be4df61-93ca-11d2-aa0d-00e098032b8c-MemoryConfig
8be4df61-93ca-11d2-aa0d-00e098032b8c-Timeout
05299c28-3953-4a5f-b7d8-f6c6a7150b2a-SetupDefaults
4dfbbaab-1392-4fde-abb8-c41cc5ad7d5d-Setup

{% endcodeblock %}