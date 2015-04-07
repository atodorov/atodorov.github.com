---
layout: post
title: "How to Configure iSCSI Target on Red Hat Enterprise Linux 7"
date: 2015-04-07 15:52
comments: true
categories: ['RHEL', 'Fedora']
---

Linux-IO (LIO) Target is an open-source implementation of the SCSI target that
has become the standard one included in the Linux kernel and the one present in
Red Hat Enterprise Linux 7. The popular *scsi-target-utils* package is replaced
by the newer *targetcli* which makes configuring a software iSCSI target quite
different.

In earlier versions one had to edit the `/etc/tgtd/targets.conf` file and
`service tgtd restart`. Here is an example configuration:

    <target iqn.2008-09.com.example:server.target1>
        backing-store /dev/vg_iscsi/lv_lun1
        backing-store /dev/vg_iscsi/lv_lun2

        incominguser user2 secretpass23
        outgoinguser userA secretpassA
    </target>

*targetcli* can be used either as an interactive shell or as stand alone commands.
Here is an example shell session which creates a file-based disk image. Comments are
provided inline:

{% codeblock %}

# yum install -y targetcli
# systemctl enable target

# targetcli 

# first create a disk image with the name of disk1. All files are sparsely created.

/> backstores/fileio create disk1 /var/lib/libvirt/images/disk1.img 10G
Created fileio disk1 with size 10737418240

# create an iSCSI target. NB: this only defines the target

/> iscsi/ create iqn.2015-04.com.example:target1
Created target iqn.2015-04.com.example:target1.
Created TPG 1.
Global pref auto_add_default_portal=true
Created default portal listening on all IPs (0.0.0.0), port 3260.

# TPGs (Target Portal Groups) allow the iSCSI to support multiple complete
# configurations within one target. This is useful for complex quality-of-service
# configurations. targetcli will automatically create one TPG when the target
# is created, and almost all setups only need one.

# switch to TPG definition for our target

/> cd iscsi/iqn.2015-04.com.example:target1/tpg1

# list the contents

/iscsi/iqn.20...:target1/tpg1> ls 
o- tpg1 ..................................................................................................... [no-gen-acls, no-auth]
  o- acls ................................................................................................................ [ACLs: 0]
  o- luns ................................................................................................................ [LUNs: 0]
  o- portals .......................................................................................................... [Portals: 1]
    o- 0.0.0.0:3260 ........................................................................................................... [OK]

# create a portal aka IP:port pairs which expose the target on the network

/iscsi/iqn.20...:target1/tpg1> portals/ create
Using default IP port 3260
Binding to INADDR_ANY (0.0.0.0)
This NetworkPortal already exists in configFS.

# create logical units (LUNs) aka disks inside our target
# in other words bind the target to its on-disk storage

/iscsi/iqn.20...:target1/tpg1> luns/ create /backstores/fileio/disk1
Created LUN 0.

# disable authentication

/iscsi/iqn.20...:target1/tpg1> set attribute authentication=0
Parameter authentication is now '0'.

# enable read/write mode

/iscsi/iqn.20...:target1/tpg1> set attribute demo_mode_write_protect=0
Parameter demo_mode_write_protect is now '0'.

# Enable generate_node_acls mode. This can be thought of as 
# "ignore ACLs mode" -- both  authentication and LUN mapping
# will then use the TPG settings.

/iscsi/iqn.20...:target1/tpg1> set attribute generate_node_acls=1
Parameter generate_node_acls is now '1'.

/iscsi/iqn.20...:target1/tpg1> ls
o- tpg1 ........................................................................................................ [gen-acls, no-auth]
  o- acls ................................................................................................................ [ACLs: 0]
  o- luns ................................................................................................................ [LUNs: 1]
  | o- lun0 ..................................................................... [fileio/disk1 (/var/lib/libvirt/images/disk1.img)]
  o- portals .......................................................................................................... [Portals: 1]
    o- 0.0.0.0:3260 ........................................................................................................... [OK]

# exit or Ctrl+D will save the configuration under /etc/target/saveconfig.json

/iscsi/iqn.20...:target1/tpg1> exit
Global pref auto_save_on_exit=true
Last 10 configs saved in /etc/target/backup.
Configuration saved to /etc/target/saveconfig.json

# after creating a second target the layout looks like this

/> ls
o- / ......................................................................................................................... [...]
  o- backstores .............................................................................................................. [...]
  | o- block .................................................................................................. [Storage Objects: 0]
  | o- fileio ................................................................................................. [Storage Objects: 2]
  | | o- disk1 .................................................. [/var/lib/libvirt/images/disk1.img (10.0GiB) write-back activated]
  | | o- disk2 .................................................. [/var/lib/libvirt/images/disk2.img (10.0GiB) write-back activated]
  | o- pscsi .................................................................................................. [Storage Objects: 0]
  | o- ramdisk ................................................................................................ [Storage Objects: 0]
  o- iscsi ............................................................................................................ [Targets: 2]
  | o- iqn.2015-04.com.example:target1 ................................................................................... [TPGs: 1]
  | | o- tpg1 .................................................................................................. [gen-acls, no-auth]
  | |   o- acls .......................................................................................................... [ACLs: 0]
  | |   o- luns .......................................................................................................... [LUNs: 1]
  | |   | o- lun0 ............................................................... [fileio/disk1 (/var/lib/libvirt/images/disk1.img)]
  | |   o- portals .................................................................................................... [Portals: 1]
  | |     o- 0.0.0.0:3260 ..................................................................................................... [OK]
  | o- iqn.2015-04.com.example:target2 ................................................................................... [TPGs: 1]
  |   o- tpg1 .................................................................................................. [gen-acls, no-auth]
  |     o- acls .......................................................................................................... [ACLs: 0]
  |     o- luns .......................................................................................................... [LUNs: 1]
  |     | o- lun0 ............................................................... [fileio/disk2 (/var/lib/libvirt/images/disk2.img)]
  |     o- portals .................................................................................................... [Portals: 1]
  |       o- 0.0.0.0:3260 ..................................................................................................... [OK]
  o- loopback ......................................................................................................... [Targets: 0]


# enable CHAP and Reverse CHAP (mutual) for both discovery and login authentication

# discovery authentication is enabled under the global iscsi node

/> cd /iscsi
/iscsi> set discovery_auth enable=1
/iscsi> set discovery_auth userid=IncomingUser
/iscsi> set discovery_auth password=SomePassword1
/iscsi> set discovery_auth mutual_userid=OutgoingUser
/iscsi> set discovery_auth mutual_password=AnotherPassword2

# login authentication is enabled either under the TPG node or under ACLs

/iscsi> cd iqn.2015-04.com.example:target1/tpg1
/iscsi/iqn.20...:target1/tpg1> set attribute authentication=1
/iscsi/iqn.20...:target1/tpg1> set auth userid=IncomingUser2
/iscsi/iqn.20...:target1/tpg1> set auth password=SomePassword3
/iscsi/iqn.20...:target1/tpg1> set auth mutual_userid=OutgoingUser2
/iscsi/iqn.20...:target1/tpg1> set auth mutual_password=AnotherPassword4
/iscsi/iqn.20...:target1/tpg1> exit

{% endcodeblock %}

Hints:

* activating targetcli service at boot is mandatory, otherwise your configuration won’t be read after a reboot
* if you type `cd` *targetcli* will display an interactive node tree
* after configuration is saved you don't need to restart anything
* the old *scsi-target-utils* doesn't support discovery authentication
* *targetcli* allows kernel memory to be shared as a block SCSI device via the
ramdisk backstore. It also supports "nullio" mode, which discards all writes, and returns all-zeroes for reads.
* I'm having troubles configuring portals to listen both on any IPv4 addresses and any IPv6 addresses
the system has. I've still not figured that out entirely.

For more information please read Chapter 25 from Red Hat's
[Storage Administration Guide](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Storage_Administration_Guide/ch25.html)
