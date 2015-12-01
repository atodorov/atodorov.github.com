---
layout: post
Title: Installing Red Hat Enterprise Linux 7 on MacBook Air 2015
date: 2015-04-26 20:33
comments: true
Tags: fedora.planet, RHEL, Mac
---

Recently I've upgraded to a new 
<a href="http://www.amazon.com/gp/product/B00UGECEUY/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00UGECEUY&linkCode=as2&tag=atodorovorg-20&linkId=3YENGI5TIYKEC5GM">MacBook Air</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B00UGECEUY" width="1" height="1" border="0"  style="border:none !important; margin:0px !important;" />
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
<a href="http://www.amazon.com/gp/product/B002PONXAI/ref=as_li_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B002PONXAI&linkCode=as2&tag=atodorovorg-20&linkId=N4KGQKYSBSDWMMM6">USB docking station from Plugable</a><img src="http://ir-na.amazon-adsystem.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=B002PONXAI" width="1" height="1" border="0"  style="border:none !important; margin:0px !important;" />
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
* *UPDATE 2015-05-05:* Presenting via external projector works with a USB to VGA adapter.
[See here](/blog/2015/05/05/using-usb-to-vga-adapter-on-macbook-air-with-linux/);

**Things that don't work yet**

* *UPDATE 2015-04-30:* I'd like to remap the Cmd key to the Menu key found in PC keyboards;
* Camera doesn't work, reverse engineering a [driver](https://github.com/patjak/bcwc_pcie)
 is in progress;
* I'm missing the [ThinkLight](http://www.thinkwiki.org/wiki/ThinkLight) from my X220,
however the integrated Broadcom FaceTime HD camera doesn't seem to have a LED flash
which can be repurposed for this task;
* I need a CPU temperature monitor and maybe CPU fan speed needs adjustments;


**UPDATE 2015-04-28:**
Check the list above for links to wifi and backlight drivers and how to disable the boot chime.

**UPDATE 2015-04-29:**
You can find precompiled RPMS in my
[Macbook Air RHEL 7 repository](/blog/2015/04/29/rhel-7-repository-for-macbook-air/).

**UPDATE 2015-04-30:**
Added more links and split the list into stuff which already works and stuff that doesn't.

**UPDATE 2015-05-04:**
Added info about Thunderbolt to Ethernet adapter.

**UPDATE 2015-05-05:**
Added info about USB to VGA adapter.


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

**lshw added on 2015-12-01**

    # lshw
    
    aero
        description: Laptop
        product: MacBookAir7,2 (System SKU#)
        vendor: Apple Inc.
        version: 1.0
        serial: C1MPF52YG944
        width: 64 bits
        capabilities: smbios-2.7 dmi-2.7 vsyscall32
        configuration: boot=normal chassis=laptop family=Mac sku=System SKU# uuid=8002EF25-82EC-B042-8FB6-10ADCCC67C02
      *-core
           description: Motherboard
           product: Mac-937CB26E2E02BB01
           vendor: Apple Inc.
           physical id: 0
           version: MacBookAir7,2
           serial: C07511704VSG92GA1
           slot: Part Component
         *-cache:0
              description: L1 cache
              physical id: 0
              slot: L1 Cache
              size: 32KiB
              capacity: 32KiB
              capabilities: synchronous internal write-back data
         *-cache:1
              description: L1 cache
              physical id: 1
              slot: L1 Cache
              size: 32KiB
              capacity: 32KiB
              capabilities: synchronous internal write-back instruction
         *-cache:2
              description: L2 cache
              physical id: 2
              slot: L2 Cache
              size: 256KiB
              capacity: 256KiB
              capabilities: synchronous internal write-back unified
         *-cache:3
              description: L3 cache
              physical id: 3
              slot: L3 Cache
              size: 4MiB
              capacity: 4MiB
              capabilities: synchronous internal write-back unified
         *-cpu
              description: CPU
              product: Core i7
              vendor: Intel Corp.
              physical id: 4
              bus info: cpu@0
              version: Intel(R) Core(TM) i7-5650U CPU @ 2.20GHz
              slot: U3E1
              size: 3100MHz
              capacity: 3200MHz
              width: 64 bits
              clock: 25MHz
              capabilities: x86-64 fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch ida arat epb pln pts dtherm tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap xsaveopt cpufreq
              configuration: cores=2 enabledcores=2 threads=4
         *-firmware
              description: BIOS
              vendor: Apple Inc.
              physical id: 5
              version: MBA71.88Z.0166.B00.1502131457
              date: 02/13/2015
              size: 1MiB
              capacity: 8128KiB
              capabilities: pci upgrade shadowing cdboot bootselect acpi smartbattery netboot uefi
         *-memory
              description: System Memory
              physical id: 19
              slot: System board or motherboard
              size: 8GiB
            *-bank:0
                 description: SODIMM DDR3 Synchronous 1600 MHz (0,6 ns)
                 product: H9CCNNN8JTMLAR-NTM
                 vendor: Hynix Semiconductor (Hyundai Electronics)
                 physical id: 0
                 serial: 0x00000000
                 slot: DIMM0
                 size: 4GiB
                 width: 64 bits
                 clock: 1600MHz (0.6ns)
            *-bank:1
                 description: SODIMM DDR3 Synchronous 1600 MHz (0,6 ns)
                 product: H9CCNNN8JTMLAR-NTM
                 vendor: Hynix Semiconductor (Hyundai Electronics)
                 physical id: 1
                 serial: 0x00000000
                 slot: DIMM0
                 size: 4GiB
                 width: 64 bits
                 clock: 1600MHz (0.6ns)
         *-pci
              description: Host bridge
              product: Broadwell-U Host Bridge -OPI
              vendor: Intel Corporation
              physical id: 100
              bus info: pci@0000:00:00.0
              version: 09
              width: 32 bits
              clock: 33MHz
              configuration: driver=bdw_uncore
              resources: irq:0
            *-display
                 description: VGA compatible controller
                 product: Broadwell-U Integrated Graphics
                 vendor: Intel Corporation
                 physical id: 2
                 bus info: pci@0000:00:02.0
                 version: 09
                 width: 64 bits
                 clock: 33MHz
                 capabilities: msi pm vga_controller bus_master cap_list rom
                 configuration: driver=i915 latency=0
                 resources: irq:56 memory:c0000000-c0ffffff memory:b0000000-bfffffff ioport:3000(size=64)
            *-multimedia:0
                 description: Audio device
                 product: Broadwell-U Audio Controller
                 vendor: Intel Corporation
                 physical id: 3
                 bus info: pci@0000:00:03.0
                 version: 09
                 width: 64 bits
                 clock: 33MHz
                 capabilities: pm msi pciexpress bus_master cap_list
                 configuration: driver=snd_hda_intel latency=0
                 resources: irq:57 memory:c1610000-c1613fff
            *-usb
                 description: USB controller
                 product: Wildcat Point-LP USB xHCI Controller
                 vendor: Intel Corporation
                 physical id: 14
                 bus info: pci@0000:00:14.0
                 version: 03
                 width: 64 bits
                 clock: 33MHz
                 capabilities: pm msi xhci bus_master cap_list
                 configuration: driver=xhci_hcd latency=0
                 resources: irq:47 memory:c1600000-c160ffff
               *-usbhost:0
                    product: xHCI Host Controller
                    vendor: Linux 3.10.0-327.el7.x86_64 xhci-hcd
                    physical id: 0
                    bus info: usb@2
                    logical name: usb2
                    version: 3.10
                    capabilities: usb-3.00
                    configuration: driver=hub slots=4 speed=5000Mbit/s
                  *-usb
                       description: Mass storage device
                       product: Card Reader
                       vendor: Apple
                       physical id: 3
                       bus info: usb@2:3
                       logical name: scsi0
                       version: 8.20
                       serial: 000000000820
                       capabilities: usb-3.00 scsi emulated scsi-host
                       configuration: driver=usb-storage maxpower=896mA speed=5000Mbit/s
                     *-disk
                          description: SCSI Disk
                          product: SD Card Reader
                          vendor: APPLE
                          physical id: 0.0.0
                          bus info: scsi@0:0.0.0
                          logical name: /dev/sdb
                          version: 3.00
                          serial: 000000000820
                          capabilities: removable
                          configuration: ansiversion=6 logicalsectorsize=512 sectorsize=512
                        *-medium
                             physical id: 0
                             logical name: /dev/sdb
               *-usbhost:1
                    product: xHCI Host Controller
                    vendor: Linux 3.10.0-327.el7.x86_64 xhci-hcd
                    physical id: 1
                    bus info: usb@1
                    logical name: usb1
                    version: 3.10
                    capabilities: usb-2.00
                    configuration: driver=hub slots=11 speed=480Mbit/s
                  *-usb:0
                       description: USB hub
                       product: USB2.0 Hub
                       vendor: Genesys Logic, Inc.
                       physical id: 2
                       bus info: usb@1:2
                       version: 9.01
                       capabilities: usb-2.00
                       configuration: driver=hub maxpower=100mA slots=4 speed=480Mbit/s
                     *-usb:0
                          description: Mouse
                          product: USB Optical Mouse
                          vendor: Logitech
                          physical id: 2
                          bus info: usb@1:2.2
                          version: 63.00
                          capabilities: usb-2.00
                          configuration: driver=usbhid maxpower=100mA speed=1Mbit/s
                     *-usb:1
                          description: Keyboard
                          product: USB Keyboard
                          vendor: Logitech
                          physical id: 3
                          bus info: usb@1:2.3
                          version: 66.00
                          capabilities: usb-1.10
                          configuration: driver=usbhid maxpower=90mA speed=1Mbit/s
                  *-usb:1
                       description: USB hub
                       product: BRCM20702 Hub
                       vendor: Apple Inc.
                       physical id: 3
                       bus info: usb@1:3
                       version: 1.00
                       capabilities: usb-2.00
                       configuration: driver=hub maxpower=94mA slots=3 speed=12Mbit/s
                     *-usb
                          description: Bluetooth wireless interface
                          product: Bluetooth USB Host Controller
                          vendor: Apple Inc.
                          physical id: 3
                          bus info: usb@1:3.3
                          version: 1.01
                          capabilities: usb-2.00 bluetooth
                          configuration: driver=btusb speed=12Mbit/s
                  *-usb:2
                       description: Human interface device
                       product: Apple Internal Keyboard / Trackpad
                       vendor: Apple Inc.
                       physical id: 5
                       bus info: usb@1:5
                       version: 1.71
                       serial: D3H5074FL6ZF94RAQ3D
                       capabilities: usb-2.00
                       configuration: driver=bcm5974 maxpower=500mA speed=12Mbit/s
            *-communication
                 description: Communication controller
                 product: Wildcat Point-LP MEI Controller #1
                 vendor: Intel Corporation
                 physical id: 16
                 bus info: pci@0000:00:16.0
                 version: 03
                 width: 64 bits
                 clock: 33MHz
                 capabilities: pm msi bus_master cap_list
                 configuration: driver=mei_me latency=0
                 resources: irq:58 memory:c161b100-c161b11f
            *-multimedia:1
                 description: Audio device
                 product: Wildcat Point-LP High Definition Audio Controller
                 vendor: Intel Corporation
                 physical id: 1b
                 bus info: pci@0000:00:1b.0
                 version: 03
                 width: 64 bits
                 clock: 33MHz
                 capabilities: pm msi bus_master cap_list
                 configuration: driver=snd_hda_intel latency=64
                 resources: irq:59 memory:c1614000-c1617fff
            *-pci:0
                 description: PCI bridge
                 product: Wildcat Point-LP PCI Express Root Port #1
                 vendor: Intel Corporation
                 physical id: 1c
                 bus info: pci@0000:00:1c.0
                 version: e3
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
                 configuration: driver=pcieport
                 resources: irq:42
            *-pci:1
                 description: PCI bridge
                 product: Wildcat Point-LP PCI Express Root Port #2
                 vendor: Intel Corporation
                 physical id: 1c.1
                 bus info: pci@0000:00:1c.1
                 version: e3
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
                 configuration: driver=pcieport
                 resources: irq:43 memory:c1400000-c15fffff ioport:a0000000(size=268435456)
               *-multimedia UNCLAIMED
                    description: Multimedia controller
                    product: 720p FaceTime HD Camera
                    vendor: Broadcom Corporation
                    physical id: 0
                    bus info: pci@0000:02:00.0
                    version: 00
                    width: 64 bits
                    clock: 33MHz
                    capabilities: pm msi pciexpress bus_master cap_list
                    configuration: latency=0
                    resources: memory:c1500000-c150ffff memory:a0000000-afffffff memory:c1400000-c14fffff
            *-pci:2
                 description: PCI bridge
                 product: Wildcat Point-LP PCI Express Root Port #3
                 vendor: Intel Corporation
                 physical id: 1c.2
                 bus info: pci@0000:00:1c.2
                 version: e3
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
                 configuration: driver=pcieport
                 resources: irq:44 memory:c1000000-c12fffff
               *-network
                    description: Wireless interface
                    product: BCM4360 802.11ac Wireless Network Adapter
                    vendor: Broadcom Corporation
                    physical id: 0
                    bus info: pci@0000:03:00.0
                    logical name: wlp3s0
                    version: 03
                    serial: 34:36:3b:86:04:e2
                    width: 64 bits
                    clock: 33MHz
                    capabilities: pm msi pciexpress bus_master cap_list ethernet physical wireless
                    configuration: broadcast=yes driver=wl0 driverversion=6.30.223.248 (r487574) ip=192.168.0.106 latency=0 multicast=yes wireless=IEEE 802.11abg
                    resources: irq:18 memory:c1200000-c1207fff memory:c1000000-c11fffff
            *-pci:3
                 description: PCI bridge
                 product: Wildcat Point-LP PCI Express Root Port #5
                 vendor: Intel Corporation
                 physical id: 1c.4
                 bus info: pci@0000:00:1c.4
                 version: e3
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
                 configuration: driver=pcieport
                 resources: irq:45 ioport:4000(size=12288) memory:c1700000-cd7fffff ioport:cd800000(size=201326592)
            *-pci:4
                 description: PCI bridge
                 product: Wildcat Point-LP PCI Express Root Port #6
                 vendor: Intel Corporation
                 physical id: 1c.5
                 bus info: pci@0000:00:1c.5
                 version: e3
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
                 configuration: driver=pcieport
                 resources: irq:46 memory:c1300000-c13fffff
               *-storage
                    description: SATA controller
                    product: Samsung Electronics Co Ltd
                    vendor: Samsung Electronics Co Ltd
                    physical id: 0
                    bus info: pci@0000:04:00.0
                    version: 01
                    width: 32 bits
                    clock: 33MHz
                    capabilities: storage pm msi pciexpress ahci_1.0 bus_master cap_list
                    configuration: driver=ahci latency=0
                    resources: irq:48 memory:c1300000-c1301fff
            *-isa
                 description: ISA bridge
                 product: Wildcat Point-LP LPC Controller
                 vendor: Intel Corporation
                 physical id: 1f
                 bus info: pci@0000:00:1f.0
                 version: 03
                 width: 32 bits
                 clock: 33MHz
                 capabilities: isa bus_master cap_list
                 configuration: driver=lpc_ich latency=0
                 resources: irq:0
            *-serial UNCLAIMED
                 description: SMBus
                 product: Wildcat Point-LP SMBus Controller
                 vendor: Intel Corporation
                 physical id: 1f.3
                 bus info: pci@0000:00:1f.3
                 version: 03
                 width: 64 bits
                 clock: 33MHz
                 configuration: latency=0
                 resources: memory:c161b000-c161b0ff ioport:efa0(size=32)
            *-generic UNCLAIMED
                 description: Signal processing controller
                 product: Wildcat Point-LP Thermal Management Controller
                 vendor: Intel Corporation
                 physical id: 1f.6
                 bus info: pci@0000:00:1f.6
                 version: 03
                 width: 64 bits
                 clock: 33MHz
                 capabilities: pm msi bus_master cap_list
                 configuration: latency=0
                 resources: memory:c1618000-c1618fff
         *-scsi
              physical id: 6
              logical name: scsi1
              capabilities: emulated
            *-disk
                 description: ATA Disk
                 product: APPLE SSD SM0256
                 physical id: 0.0.0
                 bus info: scsi@1:0.0.0
                 logical name: /dev/sda
                 version: JA0Q
                 serial: S1W2NYAG331512
                 size: 233GiB (251GB)
                 capabilities: gpt-1.00 partitioned partitioned:gpt
                 configuration: ansiversion=5 guid=4025fdbc-1c2d-45f7-864a-f87804b249da logicalsectorsize=512 sectorsize=4096
               *-volume:0
                    description: Windows FAT volume
                    vendor: mkfs.fat
                    physical id: 1
                    bus info: scsi@1:0.0.0,1
                    logical name: /dev/sda1
                    logical name: /boot/efi
                    version: FAT16
                    serial: 7eac-bc8f
                    size: 199MiB
                    capacity: 199MiB
                    capabilities: boot fat initialized
                    configuration: FATs=2 filesystem=fat mount.fstype=vfat mount.options=rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,shortname=winnt,errors=remount-ro name=EFI System Partition state=mounted
               *-volume:1
                    description: data partition
                    vendor: Windows
                    physical id: 2
                    bus info: scsi@1:0.0.0,2
                    logical name: /dev/sda2
                    logical name: /boot
                    serial: 9477ed42-e463-49a1-9bbe-991cc1bff83e
                    capacity: 499MiB
                    configuration: mount.fstype=xfs mount.options=rw,seclabel,relatime,attr2,inode64,noquota state=mounted
               *-volume:2
                    description: data partition
                    vendor: Windows
                    physical id: 3
                    bus info: scsi@1:0.0.0,3
                    logical name: /dev/sda3
                    serial: 04b082aa-fb17-4f2a-8bc9-32bce650c819
                    size: 147GiB
                    capacity: 147GiB
                    width: 512 bits
                    capabilities: encrypted luks initialized
                    configuration: bits=512 cipher=aes filesystem=luks hash=sha1 mode=xts-plain64 version=1
      *-battery
           physical id: 1
      *-network DISABLED
           description: Ethernet interface
           physical id: 2
           logical name: virbr0-nic
           serial: 52:54:00:e6:cc:48
           size: 10Mbit/s
           capabilities: ethernet physical
           configuration: autonegotiation=off broadcast=yes driver=tun driverversion=1.6 duplex=full link=no multicast=yes port=twisted pair speed=10Mbit/s
