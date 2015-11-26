---
layout: post
Title: Tip: Extending Btrfs Filesystem for Fedora Virtual Machine
date: 2013-10-13 14:53
comments: true
Tags: tips, Fedora
---

I was testing Fedora 20 inside a KVM guest this week when the disk
space run out. The system was configured to use Btrfs filesystem and this is how
to extend it.

First you have to extend the underlying guest storage. On the host I'm using LVM
so this is a no brainer:

    # pvs
      PV                                                    VG              Fmt  Attr PSize   PFree  
      /dev/mapper/luks-f3f6cea1-baba-4aaf-bca8-33a0ec540369 vg_redbull_mini lvm2 a--  289,11g 134,11g
    
    # lvs
      LV            VG              Attr      LSize   Pool Origin Data%  Move Log Cpy%Sync Convert
      vm_fedora     vg_redbull_mini -wi-ao---  15,00g                                             
    
    # lvextend -L +5G /dev/mapper/vg_redbull_mini-vm_fedora 
      Extending logical volume vm_fedora to 20,00 GiB
      Logical volume vm_fedora successfully resized
    
    # lvs
      LV            VG              Attr      LSize   Pool Origin Data%  Move Log Cpy%Sync Convert
      vm_fedora     vg_redbull_mini -wi-ao---  20,00g                                             
    
    # pvs
      PV                                                    VG              Fmt  Attr PSize   PFree  
      /dev/mapper/luks-f3f6cea1-baba-4aaf-bca8-33a0ec540369 vg_redbull_mini lvm2 a--  289,11g 129,11g


On the VM we have a default Btrfs layout:

    # blkid
    /dev/vda1: UUID="410ee563-e701-42ff-9d5f-5805dd103e35" TYPE="ext4" PARTUUID="0000330f-01" 
    /dev/vda2: UUID="f4addad4-a0fc-482e-ad5a-240864b76f09" TYPE="swap" PARTUUID="0000330f-02" 
    /dev/vda3: LABEL="fedora" UUID="f0b589ce-061c-4ac3-826e-7f3f8c8a6d30" UUID_SUB="11aa8414-3ce1-4fe7-a506-9a4f91ba5c30" TYPE="btrfs" PARTUUID="0000330f-03" 
    
    # df -h
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/vda3        13G   11G  1.4G  89% /
    devtmpfs        996M     0  996M   0% /dev
    tmpfs          1002M   80K 1002M   1% /dev/shm
    tmpfs          1002M  668K 1002M   1% /run
    tmpfs          1002M     0 1002M   0% /sys/fs/cgroup
    tmpfs          1002M   16K 1002M   1% /tmp
    /dev/vda3        13G   11G  1.4G  89% /home
    /dev/vda1       477M   72M  376M  17% /boot


Now power-off (not reboot) and power-on the VM guest so that it sees the new size
of the underlying storage. See the fdisk header (line 9 below), vda is now 20GiB!

Before extending the filesystem you have to extend the underlying disk partition! This is the
trickiest part. Using fdisk or parted you have to delete the partition and add it again.
Make sure to use the **SAME** starting sector for the new partition (line 33)!

    #!bash
    # fdisk /dev/vda
    
    Welcome to fdisk (util-linux 2.24-rc1).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.
    
    
    Command (m for help): p
    Disk /dev/vda: 20 GiB, 21474836480 bytes, 41943040 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x0000330f
    
    Device    Boot     Start       End   Blocks  Id System
    /dev/vda1 *         2048   1026047   512000  83 Linux
    /dev/vda2        1026048   5253119  2113536  82 Linux swap / Solaris
    /dev/vda3        5253120  31457279 13102080  83 Linux
    
    Command (m for help): d
    Partition number (1-3, default 3): 3
    
    Partition 3 is deleted
    
    Command (m for help): n
    
    Partition type:
       p   primary (2 primary, 0 extended, 2 free)
       e   extended
    Select (default p): p
    Partition number (3,4, default 3): 3
    First sector (5253120-41943039, default 5253120): 
    Last sector, +sectors or +size{K,M,G,T,P} (5253120-41943039, default 41943039): 
    
    Created a new partition 3 of type 'Linux' and of size 17,5 GiB.
    
    Command (m for help): p
    Disk /dev/vda: 20 GiB, 21474836480 bytes, 41943040 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk label type: dos
    Disk identifier: 0x0000330f
    
    Device    Boot     Start       End   Blocks  Id System
    /dev/vda1 *         2048   1026047   512000  83 Linux
    /dev/vda2        1026048   5253119  2113536  82 Linux swap / Solaris
    /dev/vda3        5253120  41943039 18344960  83 Linux
    
    Command (m for help): w
    
    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Re-reading the partition table failed.: Device or resource busy
    
    The kernel still uses the old table. The new table will be used at the next reboot or after you run partprobe(8) or kpartx(8).
    
    # partprobe
    Error: Partition(s) 3 on /dev/vda have been written, but we have been unable to inform the kernel of the change, probably because it/they are in use.  As a result, the old partition(s) will remain in use.  You should reboot now before making further changes.
    
    # reboot


See lines 36 and 49 above. The new partition has a greater size.
After reboot just resize the filesystem and verify the new space has been added

    # btrfs filesystem resize max /
    Resize '/' of 'max'
    
    # df -h
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/vda3        18G   11G  6.4G  63% /
    devtmpfs        996M     0  996M   0% /dev
    tmpfs          1002M   80K 1002M   1% /dev/shm
    tmpfs          1002M  660K 1002M   1% /run
    tmpfs          1002M     0 1002M   0% /sys/fs/cgroup
    tmpfs          1002M   16K 1002M   1% /tmp
    /dev/vda3        18G   11G  6.4G  63% /home
    /dev/vda1       477M   72M  376M  17% /boot


This is it, more disk space available for the virtual machine. Let me know how it works
for you.
