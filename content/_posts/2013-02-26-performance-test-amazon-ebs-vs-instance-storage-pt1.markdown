---
layout: post
Title: Performance Test: Amazon EBS vs. Instance Storage, Pt.1
date: 2013-02-26 23:02
comments: true
Tags: 'performance testing', 'QA', 'Amazon', 'EC2', 'cloud'
---

I'm exploring the possibility to speed-up my cloud database so I've run some
basic tests against storage options available to Amazon EC2 instances.
The instance was [m1.large](http://aws.amazon.com/ec2/instance-types/)
with High I/O performance and two additional disks with the same size:

* /dev/xvdb - type EBS
* /dev/xvdc - type instance storage

Both are Xen para-virtual disks. The difference is that EBS is persistent
across reboots while instance storage is ephemeral.


hdparm
------

For a quick test I used `hdparm`. The manual says:

    -T  Perform timings of cache reads for benchmark and comparison purposes.
        This displays the speed of reading directly from the Linux buffer cache
        without disk access. This measurement is essentially an indication of
        the throughput of the processor, cache, and memory of the system under test.

    -t  Perform timings of device reads for benchmark and comparison purposes.
        This displays the speed of reading through the buffer cache to the disk
        without any prior caching of data. This measurement is an indication of how
        fast the drive can sustain sequential data reads under Linux, without any
        filesystem overhead.

The results of 3 runs of hdparm are shown below:

    # hdparm -tT /dev/xvdb /dev/xvdc
    
    /dev/xvdb:
     Timing cached reads:   11984 MB in  1.98 seconds = 6038.36 MB/sec
     Timing buffered disk reads:  158 MB in  3.01 seconds =  52.52 MB/sec
    
    /dev/xvdc:
     Timing cached reads:   11988 MB in  1.98 seconds = 6040.01 MB/sec
     Timing buffered disk reads:  1810 MB in  3.00 seconds = 603.12 MB/sec


    # hdparm -tT /dev/xvdb /dev/xvdc
    
    /dev/xvdb:
     Timing cached reads:   11892 MB in  1.98 seconds = 5991.51 MB/sec
     Timing buffered disk reads:  172 MB in  3.00 seconds =  57.33 MB/sec
    
    /dev/xvdc:
     Timing cached reads:   12056 MB in  1.98 seconds = 6075.29 MB/sec
     Timing buffered disk reads:  1972 MB in  3.00 seconds = 657.11 MB/sec


    # hdparm -tT /dev/xvdb /dev/xvdc
    
    /dev/xvdb:
     Timing cached reads:   11994 MB in  1.98 seconds = 6042.39 MB/sec
     Timing buffered disk reads:  254 MB in  3.02 seconds =  84.14 MB/sec
    
    /dev/xvdc:
     Timing cached reads:   11890 MB in  1.99 seconds = 5989.70 MB/sec
     Timing buffered disk reads:  1962 MB in  3.00 seconds = 653.65 MB/sec


**Result:**
Sequential reads from instance storage are 10x faster compared to EBS on average.


IOzone
------

I'm running MySQL and sequential data reads are probably over idealistic scenario.
So I found another benchmark suite, called [IOzone](http://iozone.org).
I used the 3-414 version built from the official SRPM.

IOzone performs multiple tests. I'm interested in read/re-read, random-read/write,
read-backwards and stride-read.

For this round of testing I've tested with ext4 filesystem with and without journal
on both types of disks. I also experimented running Iozone inside a ramfs mounted
directory. However I didn't have the time to run the test suite multiple times.

Then I used
[iozone-results-comparator](http://code.google.com/p/iozone-results-comparator/) to
visualize the results. (I had to do a minor fix to the code to run inside virtualenv
and install all missing dependencies).

Raw IOzone output, data visualization and the modified tools are available in the
[aws_disk_benchmark_w_iozone.tar.bz2](http://s3.amazonaws.com/atodorov/blog/aws_disk_benchmark_w_iozone.tar.bz2)
file (size 51M).

**Graphics**

EBS without journal(Baseline) vs. Instance Storage without journal(Set1)
![EBS vs. Instance Storage](/images/aws_iozone/ebs_woj_vs_is_woj.png "EBS vs. Instance Storage")

Instance Storage without journal(Baseline) vs. Ramfs(Set1)
![IS vs. Ramfs](/images/aws_iozone/ebs_woj_vs_is_woj.png "IS vs. Ramfs")

**Results**

* ext4 journal has no effect on reads, causes slow down when writing to disk. This
is expected;
* Instance storage is faster compared to EBS but not much.
If I understand the results correctly, read performance is similar in some cases;
* Ramfs is definitely the fastest but read performance compared to instance storage
is not two-fold (or more) as I expected;

**Conclusion**

Instance storage appears to be faster (and this is expected) but I'm still not sure if
my application will gain any speed improvement or how much if migrated to read from
instance storage (or ramfs) instead of EBS. I will be performing more real-world
test next time, by comparing execution time for some of my largest SQL queries.

If you have other ideas how to adequately measure I/O performance in the AWS cloud,
please use the comments below.
