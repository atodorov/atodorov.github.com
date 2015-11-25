---
layout: post
Title: Reducing AWS Cloud Costs - Real Money Example
date: 2014-03-07 17:14
comments: true
Tags: 'Amazon', 'cloud'
---

[Last month](http://aws.amazon.com/ebs/pricing/effective-february-2014/) Amazon
reduced by 50% prices for EBS storage. This, combined with 
[shrinking EBS root volume size](/blog/2014/02/07/aws-tip-shrinking-ebs-root-volume-size/) and
[moving /tmp to instance storage](/blog/2014/02/10/moving-tmp-from-ebs-to-instance-storage/)
allowed me to reduce EBS related costs behind [Difio](http://www.dif.io) by around 50%.
Following are the real figures from my AWS Bill.

EBS costs for Difio were gradually rising up with every new node added to the cluster and
increased package processing (resulting in more I/O):

* November 2013 - $7.38
* December 2013 - $10.55
* January 2014 - $11.97

{% codeblock January 2014 %}
EBS
$0.095 per GB-Month of snapshot data stored     9.052 GB-Mo     $0.86
$0.10  per GB-month of provisioned storage      101.656 GB-Mo  $10.17
$0.10  per 1 million I/O requests               9,405,243 IOs   $0.94
                                                        Total: $11.97
{% endcodeblock %}

In February there was one new system added to process additional requests
(cluster nodes run as spot instances) and an increased number of temporary
instances (although I haven't counted them) while I was restructuring AMI
internals to accommodate the [open source](https://github.com/difio/difio)
version of Difio. My assumption (based on historical data) is this would
have driven the costs up in the region of $15 per month only for EBS.

After implementing the stated minimal improvements and having Amazon reduced the prices by
half the bill looks like this:

{% codeblock February 2014 %}
EBS
$0.095 per GB-Month of snapshot data stored     8.668 GB-Mo     $0.82
$0.05  per GB-month of provisioned storage      58.012 GB-Mo    $2.90
$0.05  per 1 million I/O requests               5,704,482 IOs   $0.29
                                                        Total:  $4.01
{% endcodeblock %}


Explanation
-----------

*Snapshot data stored* is the volume of snapshots (AMIs, backups, etc) which
I have. This is fairly constant.

*Provisioned storage* is the volume of EBS storage provisioned for running
instances (e.g. root file system, data partitions, etc.). This was reduced
mainly because of shrinking the root volumes. (Previously I've used larger
root volumes for a bigger /tmp).


*I/O requests* is the number of I/O requests associated with your EBS volumes.
As far as I understand Amazon doesn't charge for I/O related to ephemeral storage.
Moving /tmp from EBS to instance storage is the reason this was reduced roughly by half.


Where To Next
-------------

I've reduced the root volumes back to the 8GB defaults but this has still room for
improvement b/c the AMI is quite minimal. This will bring the largest improvements.
Another thing is the still relatively high I/O rate that touches EBS volumes.
I haven't investigated where this comes from though.

