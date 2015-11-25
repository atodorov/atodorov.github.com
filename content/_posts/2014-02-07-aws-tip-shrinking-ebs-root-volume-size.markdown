---
layout: post
Title: AWS Tip: Shrinking EBS Root Volume Size
date: 2014-02-07 00:23
comments: true
Tags: 'tips', 'Amazon', 'cloud'
---

Amazon's Elastic Block Store volumes are easy to use and expand but notoriously
hard to shrink once their size has grown. Here is my tip for shrinking EBS size
and saving some money from over-provisioned storage. I'm assuming that you want to
shrink the root volume which is on EBS. 

- Write down the block device name for the root volume (/dev/sda1) - *from AWS console:
Instances; Select instance; Look at Details tab; See Root device or Block devices*;
- Write down the availability zone of your instance - *from AWS console: Instances;
column Availability Zone*;
- Stop instance;
- Create snapshot of the root volume;
- From the snapshot, create a second volume, in the **same availability zone** as
your instance (you will have to attach it later). This will be your pristine source;
- Create new empty EBS volume (not based on a snapshot), with smaller size,
in the same availability zone - *from AWS console: Volumes; Create Volume;
Snapshot == No Snapshot*; **IMPORTANT** - size should be large enough to hold
all the files from the source file system (try `df -h` on the source first);
- Attach both volumes to instance while taking note of the block devices names
you assign for them in the AWS console;

For example: In my case `/dev/sdc1` is the source snapshot and `/dev/sdd1` is the
empty target.

- Start instance;
- Optionally check the source file system with `e2fsck -f /dev/sdc1`;
- Create a file system for the empty volume - `mkfs.ext4 /dev/sdd1`;
- Mount volumes at `/source` and `/target` respectively;
- Now sync the files: `rsync -aHAXxSP /source/ /target`. **Note the missing slash (/)
after `/target`**. If you add it you will end up with files inside `/target/source/`
which you don't want;
- Quickly verify the new directory structure with `ls -l /target`;
- Unmount `/target`;
- Optionally check the new file system for consistency `e2fsck -f /dev/sdd1`;
- **IMPORTANT** - check how `/boot/grub/grub.conf` specifies the root volume - 
by UUID, by LABEL, by device name, etc. You will have to duplicate the same for the
new smaller volume or update `/target/boot/grub/grub.conf` to match the new volume.
Check `/target/etc/fstab` as well!

In my case I had to `e2label /dev/sdd1 /` because both `grub.conf` and `fstab` were
using the device label.

- Shutdown the instance;
- Detach all volumes;
- **IMPORTANT** - attach the new smaller volume to the instance using the same block device
name from the first step (e.g. `/dev/sda1`);
- Start the instance and verify it is working correctly;
- DELETE auxiliary volumes and snapshots so they don't take space and accumulate costs!

