---
layout: post
Title: Moving /tmp from EBS to Instance Storage
date: 2014-02-10 13:48
comments: true
Tags: cloud, Amazon
---

I've seen a fair amount of stories about moving away from Amazon's EBS volumes
to ephemeral instance storage. I've decided to give it a try starting with `/tmp`
directory where [Difio](http://www.dif.io) operates.

It should be noted that although instance storage may be available for some instance
types it may not be attached by default. Use this command to check:
{% codeblock lang:bash %}
$ curl http://169.254.169.254/latest/meta-data/block-device-mapping/
ami
root
swap
{% endcodeblock %}

In the above example there is no instance storage present. 

You can attach one either when launching the EC2 instance or when creating a customized AMI
(instance storage devices are pre-defined in the AMI). When creating an AMI you can attach more ephemeral devices
but they will not available when instance is launched. The maximum number of available
instance storage devices can be found in the
[docs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#StorageOnInstanceTypes).
That is to say if you have an AMI which defines 2 ephemeral devices and launch a
standard m1.small instance there will be only one ephemeral device present.

Also note that for M3 instances, you must specify instance store volumes in the
block device mapping for the instance. When you launch an M3 instance, Amazon ignores
any instance store volumes specified in the block device mapping for the AMI.


As far as I can see the AWS Console doesn't indicate if instance storage is attached
or not. For instance with 1 ephemeral volume:

{% codeblock lang:bash %}
$ curl http://169.254.169.254/latest/meta-data/block-device-mapping/
ami
ephemeral0
root
swap

$ curl http://169.254.169.254/latest/meta-data/block-device-mapping/ephemeral0
sdb
{% endcodeblock %}


Ephemeral devices can be mounted in `/media/ephemeralX/`, but not all volumes.
I've found that usually only `ephemeral0` is mounted automatically.

{% codeblock lang:bash %}
$ curl http://169.254.169.254/latest/meta-data/block-device-mapping/
ami
ephemeral0
ephemeral1
root

$ ls -l /media/
drwxr-xr-x 3 root root 4096 21 ное  2009 ephemeral0
{% endcodeblock %}



For Difio I have an init.d script which executes when the system
boots. To enable `/tmp` on ephemeral storage I just added the following snippet:
{% codeblock lang:bash %}
echo $"Mounting /tmp on ephemeral storage:"
for ef in `curl http://169.254.169.254/latest/meta-data/block-device-mapping/ 2>/dev/null | grep ephemeral`; do
    disk=`curl http://169.254.169.254/latest/meta-data/block-device-mapping/$ef 2>/dev/null`
    echo $"Unmounting /dev/$disk"
    umount /dev/$disk

    echo $"mkfs /dev/$disk"
    mkfs.ext4 -q /dev/$disk

    echo $"Mounting /dev/$disk"
    mount -t ext4 /dev/$disk /tmp && chmod 1777 /tmp && success || failure
done
{% endcodeblock %}

**NB:** success and failure are from `/etc/rc.d/init.d/functions`.
If you are using LVM or RAID you need to reconstruct your block devices
accordingly!


If everything goes right I should be able to reduce my AWS costs by saving on
provisioned storage and I/O requests. I'll keep you posted on this after a month or two.
