---
layout: post
Title: USB multi-seat on Red Hat Enterprise Linux 6
date: 2011-03-14 20:10
comments: true
Tags: 'RHEL'
---
Multiseat configurations are well known in the Linux community and have been used for a number of years now. In the last few years USB docking stations emerged on the market and are becoming popular among multiseat enthusiasts. 

My company [Open Technologies Bulgaria, Ltd.](http://otb.bg) offers full support of USB multiseat for Red Hat Enterprise Linux 6 as a downstream vendor. We use the name SUMU (simple usb multi user) to refer to the entire multiseat bundle and in this article I'm going to describe the current state of technologies surrounding multiseat, how that works on RHEL 6 and some practical observations.

COMPONENTS
----------

To build a multiseat system you need a number of individual components:

<img src="/images/plugable_docking_station.png" alt="UD-160-A" style="float: right;"/>

<ul>
  <li>
    USB docking station like Plugable's <a href="http://plugable.com/products/UD-160-A">UD-160-A</a> or a combination of <a href="http://plugable.com/products/">USB video card</a> and stand alone USB hub. It is also possible to use USB docking stations from other vendors but I'm not aware of anyone who did it.
  </li>

  <li>
<em>udlfb</em> - a kernel driver for USB graphics adapters which use DisplayLink based chips. As of January 2011 udlfb.c is part of the mainline kernel tree and is on track for 2.6.38. On RHEL6 this can easily be built as a stand alone module. There are no issues with this package.

We also use a custom patch that will draw the string "fbX" onto the green screen. This is useful for easier identification of the display. The patch can be found <a href="http://otb-sources.googlecode.com/svn/trunk/sumu/udlfb-kmod/fbX-numbering.patch">here</a>.
  </li>

  <li>
<em>Xorg</em> - this is the standard graphics server on Linux. In RHEL 6 we have xorg-x11-server-Xorg-1.7.7-26 which works perfectly in a multiseat environment.
  </li>

  <li>
<em>xorg-x11-drv-fbdev</em> with extensions - Xorg driver based on the <em>fbdev</em> driver. The extensions add support for the X DAMAGE protocol. This is a temporary solution until Xorg adds support for the damage protocol. Our package is called <em>xorg-x11-drv-fbdev-displaylink</em> to avoid conflict with the stock package provided by the distribution and it installs the files in <em>/usr/local</em>. You can also change the compiler flags and produce a binary under a different name (say <em>displaylink_drv.so</em> instead of <em>fbdev_drv.so</em>).
  </li>

  <li>
<em>GDM</em> with multiseat support - GDM will manage multiple local displays and has the ability to add/remove displays dynamically. This functionality is present in versions up to 2.20 and since RHEL6 includes gdm-2.30.4-21.el6 this is a tough choice. There are several possibilities:
<ol>
  <li>
Use older <em>GDM</em>, preferably from a previous RHEL release. This gives you a tested piece of software and as long as the previous release is maintained you have (at least some) opportunity of fixing bugs in this code base. However this conflicts with current <em>GDM</em> in the distro which is also integrated with <em>ConsoleKit</em>, <em>Plymouth</em> and <em>PulseAudio</em>.
  </li>

  <li>
Use <em>GDM</em> and <em>ConsoleKit</em> that are available in RHEL6 and apply the multiseat patches available at
https://bugs.freedesktop.org/show_bug.cgi?id=19333 and http://bugzilla.gnome.org/show_bug.cgi?id=536355.

Those patches are quite big (around 3000 lines each) and are not yet fully integrated upstream. They also conflict with custom patches that Red Hat is shipping into these packages. Your patched packages will also conflict with the stock distro packages and you will not receive any support for that. Since <em>ConsoleKit</em> seems like fairly important application I'd not recommend modifying it.
  </li>

  <li>
Use another display manager that can handle multiple displays. https://help.ubuntu.com/community/MultiseatX suggests to use <em>KDM</em> instead of <em>GDM</em>. As far as I can tell the configuration is only static and this can break any time due to the fact that USB device discovery is unpredictable and unreliable. It also lacks an alternative for <em>gdmdynamic</em> according to http://lists.kde.org/?l=kde-devel&m=129898381127854&w=2 which makes it a no-go for plug-and-play multiseat support.

There are other less popular display managers but I haven't spend much time in research.
  </li>

  <li>
Just for the record it is also possible that one writes a custom display manager for multiseat operations. This sounds like an overkill and there are many factors which need to be taken into account. If you have enough resources and knowledge to write a display manager you'd better give upstream a hand instead of reinventing the wheel. 
  </li>
</ol>

We've decided to use <em>GDM 2.16</em> from RHEL5 due to the above factors. In practice it turns out that there aren't many issues with this version.
  </li>

  <li>
<em>A GDM theme</em> - since the GDM version we're using requires a theme which is missing in RHEL6 this is also provided as a separate package. A GDM theme is an XML file plus some images.
  </li>

  <li>
<em>udev rules, scripts and config files</em> - this is the glue between all the other components. Their primary job is to group the display-mouse-keyboard pairs for a given seat and start the display with the appropriate configuration settings. We also have support for <em>PulseAudio</em>.
  </li>
</ul>

RHEL6 SPECIFICS
---------------

For detailed description of multiseat configuration take a look at http://plugable.com/2009/11/16/setting-up-usb-multiseat-with-displaylink-on-linux-gdm-up-to-2-20/ or at our <a href="http://otb-sources.googlecode.com/svn/trunk/sumu/">source code</a>. I'm going to describe only the differences in RHEL6.

<em>GDM</em>, <em>udlfb</em> and <em>xorg-x11-drv-fbdev-displaylink</em> need to be compiled and installed on the system. 

To build an older <em>GDM</em> on RHEL6 you will need to adjust some of the patches in the src.rpm package to apply cleanly and tweak the .spec file to your needs. This also includes using the appropriate version of <em>ltmain.sh</em> from the distro.

The udev rules and scripts are slightly different due to the different device paths in RHEL6:
``` bash
SYSFS{idVendor}=="17e9", SYSFS{bConfigurationValue}=="2", RUN="/bin/echo 1 > /sys%p/bConfigurationValue"

ACTION=="add",    KERNEL=="fb*", SUBSYSTEM=="graphics", SUBSYSTEMS=="usb", PROGRAM="/usr/bin/sumu-hub-id /sys/%p/device/../", SYMLINK+="usbseat/%c/display",  RUN+="/etc/udev/scripts/start-seat %c"
ACTION=="remove", KERNEL=="fb*", SUBSYSTEM=="graphics", RUN+="/etc/udev/scripts/stop-seat %k"

KERNEL=="control*", SUBSYSTEM=="sound", BUS=="usb", PROGRAM="/usr/bin/sumu-hub-id /sys/%p/device/../../../../", SYMLINK+="usbseat/%c/sound"
KERNEL=="event*", SUBSYSTEM=="input", BUS=="usb", SYSFS{bInterfaceClass}=="03", SYSFS{bInterfaceProtocol}=="01", PROGRAM="/usr/bin/sumu-hub-id /sys/%p/device/../../../../", SYMLINK+="usbseat/%c/keyboard", RUN+="/etc/udev/scripts/start-seat %c"
KERNEL=="event*", SUBSYSTEM=="input", BUS=="usb", SYSFS{bInterfaceClass}=="03", SYSFS{bInterfaceProtocol}=="02", PROGRAM="/usr/bin/sumu-hub-id /sys/%p/device/../../../../", SYMLINK+="usbseat/%c/mouse",    RUN+="/etc/udev/scripts/start-seat %c"
```

We also use only <em>/dev/event*</em> devices for both mouse and keyboard.

The <em>sumu-hub-id</em> script returns the string busX-devY indicating the location of the device:
``` bash
#!/bin/bash
if [ -d "$1" ]; then
    echo "bus$(cat $1/busnum)-dev$(cat $1/devnum)"
    exit 0
else
    exit 1
fi
```

USB device numbering is unique per bus and there isn't a global device identifier as far as I know. On systems with 2 or more USB buses this can lead to mismatch between devices/seats.

For seat/display numbering we use the number of the framebuffer device associated with the seat. This is unique, numbers start from 1 (<em>fb0</em> is the text console) and are sequential unlike USB device numbers. This also ensures easy match between <em>$DISPLAY</em> and <em>/dev/fbX</em> for debugging purposes.

Our <em>xorg.conf.sed</em> template uses evdev as the input driver. This driver is the default in RHEL6:
```
Section "InputDevice"
    Identifier "keyboard"
    Driver      "evdev"
    Option      "CoreKeyboard"
    Option      "Device"        "/dev/usbseat/%SEAT_PATH%/keyboard"
    Option      "XkbModel"      "evdev"
EndSection

Section "InputDevice"
    Identifier "mouse"
    Driver      "evdev"
    Option      "CorePointer"
    Option      "Protocol" "auto"
    Option      "Device"   "/dev/usbseat/%SEAT_PATH%/mouse"
    Option      "Buttons" "5"
    Option      "ZAxisMapping" "4 5"
EndSection
```

We also use a custom <em>gdm.conf</em> file to avoid conflicts with stock packages. Only the important settings are shown:
```
[daemon]
AlwaysRestartServer=false
DynamicXServers=true
FlexibleXServers=0
VTAllocation=false

[servers]
0=inactive
```

AlwaysRestartServer=false is necessary to avoid a bug in <em>Xorg</em>. See below for issues description.

Audio is supported by setting $PULSE_SINK/$PULSE_SOURCE environment variables using a script in <em>/etc/profile.d</em> which executes after login.

SCALABILITY AND PERFORMANCE
---------------------------

<strong>Maximum seats</strong>:<br />
The USB standard specifies a maximum of 127 USB devices connected to a single host controller. This means around 30 seats per USB controller depending on the number of devices connected to a USB hub. In practice you will have hard time finding a system which has that many port available. I've used Fujitsu's <a href="http://ts.fujitsu.com/products/standard_servers/tower/primergy_tx100s1.html">TX100 S1</a> and <a href="http://ts.fujitsu.com/products/standard_servers/tower/primergy_tx100s2.html">TX100 S2</a> which can be expanded to 15 or 16 USB ports using all external and internal ports and additional PCI-USB extension card.

While larger configuration are possible by using more PCI cards or intermediate hubs those are limited by the USB 2.0 transfer speed (more devices on a single hub, slower graphics) and a <a href="https://bugzilla.kernel.org/show_bug.cgi?id=28682">bug</a> in the Linux kernel.


<strong>Space and cable length</strong>:<br />
USB 2.0 limits the cable length to 5 meters. On the market I've found good quality cables running 4.5 meters. This means that your multiseat system needs to be confined is small physical space due to these limitations. In practice using medium sized multiseat system in a 30 square meters space is doable and fits into these limits. This is roughly the size of a class-room in a school.

You can of course use daisy chaining (up to 5 hubs) and active USB extension cords (11 meters) or USB over CAT5 cables (up to 45 meters) but all of these interfere with USB signal strength and can lead to unpredictable behavior. For example I've see errors opening USB devices when power is not sufficient or too high. Modern computer systems have built in hardware protection and shut off USB ports or randomly reboot when the current on the wire is too strong. I've seen this on a number of occasions and the fix was to completely power off and unplug the system then power it on again.

Also don't forget that USB video consumes a great deal of the limited USB 2.0 bandwidth. Depending on the workload of the system (e.g. office applications vs. multimedia) you could experience slow graphical response if using extension cords and daisy chaining.

<strong>Performance</strong>:<br />
For regular desktop use (i.e. nothing in particular) I'd recommend using 32bit operating system. On 64bit systems objects take a lot more memory and you'll need 3-4 times more for the same workload as on 32bit. For example 16 users running Eclipse, gnome-terminal and Firefox will need less that 8GB of memory on 32bit and more than 16GB on 64bit. Python and Java are particularly known to use much more memory on 64bit.

Regular desktop usage is not CPU intensive and a modern Xeon CPU has no issues with it. One exception is Flash which always causes your CPU to choke. On multiseat that becomes even a bigger problem. If possible disable/remove Flash from the system.

Multiseat doesn't make any difference when browsing, sending e-mail, etc. You shouldn't experience issues with networking unless your workload doesn't require hi-speed connection or your bandwidth is too low. If this is the case you'd better use the USB NICs available in the docking stations and bond them together, add external PCI NICs or upgrade your networking infrastructure.

Disk performance is critical in multiseat especially because it affects the look and feel of the system and is visible by the end users. It is usually good practice to place /home on a separate partition and even on a separate disk. Also consider disabling unnecessary caching in user space applications such as Firefox and Nautilus (thumbnails and cache). 

On a system with 2 x 7,2K RPM disks in BIOS RAID1 configuration and a standard RHEL6 installation (i.e. no optimizations configured) where /, swap and /home are on the same RAID array we have 15 users using GNOME, gedit, Firefox, gnome-terminal and gcc. The performance is comparable to stand alone desktop with occasional spikes which cause GNOME to freeze for a second or two. It is expected that disabling unnecessary caching will make things better.

Depending on the workload (reads vs. writes) you should consider different RAID levels, file system types and settings and changing disk parameters. A good place to start is the "Storage Administration Guide" and "I/O Tuning Guide" at http://docs.redhat.com.


KNOWN ISSUES
------------

<ul>
 <li>
<a href="https://bugzilla.kernel.org/show_bug.cgi?id=28682">Bug 28682 - input drivers support limited device numbers (EVDEV_MINORS is 32)</a> - this bug will block you from adding more than 32 input devices of the same type. For multiseat that means 32 devices which are handled by the event driver which includes mice, keyboards, joystick and special platform events such as the Reboot/Poweroff buttons. This limits the available seats to around 15.
 </li>

 <li>
<a href="https://bugzilla.redhat.com/show_bug.cgi?id=679122">Bug 679122 - gnome-volume-control: Sound at 100% and no sound output</a> - upon first login the user will not hear any sound regardless of the fact that the volume control application shows volume is at 100%.
 </li>

 <li>
<a href="https://bugzilla.redhat.com/show_bug.cgi?id=682562">Bug 682562 - gnome-volume-control doesn't respect PULSE_SINK/PULSE_SOURCE</a> - the volume control application will not behave correctly and may confuse users.
 </li>

 <li>
Xorg will cause 100% CPU usage after logout - this is due to several factors. The <a href="http://plugable.com/2009/11/16/setting-up-usb-multiseat-with-displaylink-on-linux-gdm-up-to-2-20/">initial multiseat configuration</a> had a problem with input duplication. This was fixed by removing "-sharevts -novtswitch" from the X start line and substituting a specific VT - "vt07". 

This works fine unless one of the users logs out of their GNOME session. After that GDM will kill and restart it's process and new Xorg process will be spawned. The restarted instance will loop endlessly executing the following code:

``` c
ioctl(5, TCFLSH, 0x2)                   = -1 EIO (Input/output error)
setitimer(ITIMER_REAL, {it_interval={0, 20000}, it_value={0, 20000}}, NULL) = 0
clock_gettime(CLOCK_MONOTONIC, {247, 684817842}) = 0
clock_gettime(CLOCK_MONOTONIC, {247, 684921278}) = 0
setitimer(ITIMER_REAL, {it_interval={0, 0}, it_value={0, 0}}, NULL) = 0
select(256, [1 3 5 13 14 15 16], NULL, NULL, {409, 254000}) = 1 (in [5], left {409, 253990})
ioctl(5, TCFLSH, 0x2)                   = -1 EIO (Input/output error)
```

If you search on the Internet you will find plenty of bug reports related to this code block. The problem is in <em>Xorg</em> which doesn't properly handle the situation where it can't take control over the terminal. The solution is to not restart <em>Xorg</em> after user session ends. This is done by setting AlwaysRestartServer=false in <em>gdm.conf</em>.
 </li>

 <li>
No integration with <em>SELinux</em> and <em>ConsoleKit</em> - while configuring <em>SELinux</em> in Permissive mode is easy workaround there's no easy workaround for <em>ConsoleKit</em>. 

Newer <em>GDM</em> versions register the user session with <em>ConsoleKit</em> and integrate that into the desktop. Missing integration means that some things will fail. For example <em>NetworkManager</em> will not allow the user to connect to a VPN connection because it thinks this user is not logged in:

```
** (nm-applet:1168): WARNING **: &lt;WARN&gt;  activate_vpn_cb(): VPN Connection activation failed:
(org.freedesktop.NetworkManager.PermissionDenied) No user settings service available
```
</li>

 <li>
No ACLs for external USB flash drives - this is missing upstream and is supposed to land in <em>ConsoleKit</em>. When a user plugs their USB flash drive on a multiseat system GNOME will try to mount it automatically. If there are multiple users logged in this will either fail or all of them will be able to access the flash drive. 
 </li>
</ul>

PICTURES AND VIDEO
------------------

Pictures from one of our deployments can be found on Facebook (no login required):
<http://www.facebook.com/album.php?aid=54571&id=180150925328433>.
A demonstration video from the same deployment can be found at <http://www.youtube.com/watch?v=7GYbCDGTz-4>

If you are interested in commercial support please contact me!

FUTURE
------

In the open source world everything is changing and multiseat is no exception. While <em>GDM</em> and <em>ConsoleKit</em> patches are not yet integrated upstream there's a new project called <a href="http://www.freedesktop.org/wiki/Software/systemd">systemd</a> which aims at replacing the SysV init scripts system. It already has several configuration files for multiseat and I expect it will influence multiseat deployments in the future. Systemd will be available in Fedora 15.
