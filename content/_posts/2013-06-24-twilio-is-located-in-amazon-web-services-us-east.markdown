---
layout: post
Title: Twilio is Located in Amazon Web Services US East
date: 2013-06-24 23:43
comments: true
categories: ['Twilio', 'Amazon', 'cloud']
---

{% blockquote %}
Where do I store my audio files in order to minimize download and call wait time?
{% endblockquote %}

Twilio is a cloud vendor that provides telephony services. 
It can download and `<Play>` arbitrary audio files and will cache the files
for better performance.

Twilio support told me they are not disclosing the location of their servers,
so from my web application hosted in AWS US East:
{% codeblock lang:bash %}
[ivr-otb.rhcloud.com logs]\> grep TwilioProxy access_log-* | cut -f 1 -d '-' | sort | uniq 
10.125.90.172 
10.214.183.239 
10.215.187.220 
10.245.155.18 
10.255.119.159 
10.31.197.102 
{% endcodeblock %}

Now let's map these addresses to host names. From another EC2 system, also in Amazon US East:

{% codeblock lang:bash %}
[ec2-user@ip-10-29-206-86 ~]$ dig -x 10.125.90.172 -x 10.214.183.239 -x 10.215.187.220 -x 10.245.155.18 -x 10.255.119.159 -x 10.31.197.102

; <<>> DiG 9.8.2rc1-RedHat-9.8.2-0.17.rc1.29.amzn1 <<>> -x 10.125.90.172 -x 10.214.183.239 -x 10.215.187.220 -x 10.245.155.18 -x 10.255.119.159 -x 10.31.197.102
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 43245
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;172.90.125.10.in-addr.arpa.    IN      PTR

;; ANSWER SECTION:
172.90.125.10.in-addr.arpa. 113 IN      PTR     ip-10-125-90-172.ec2.internal.

;; Query time: 1 msec
;; SERVER: 172.16.0.23#53(172.16.0.23)
;; WHEN: Mon Jun 24 20:48:21 2013
;; MSG SIZE  rcvd: 87

;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 52693
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;239.183.214.10.in-addr.arpa.   IN      PTR

;; ANSWER SECTION:
239.183.214.10.in-addr.arpa. 42619 IN   PTR     domU-12-31-39-0B-B0-01.compute-1.internal.

;; Query time: 0 msec
;; SERVER: 172.16.0.23#53(172.16.0.23)
;; WHEN: Mon Jun 24 20:48:21 2013
;; MSG SIZE  rcvd: 100

;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 25255
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;220.187.215.10.in-addr.arpa.   IN      PTR

;; ANSWER SECTION:
220.187.215.10.in-addr.arpa. 43140 IN   PTR     domU-12-31-39-0C-B8-2E.compute-1.internal.

;; Query time: 0 msec
;; SERVER: 172.16.0.23#53(172.16.0.23)
;; WHEN: Mon Jun 24 20:48:21 2013
;; MSG SIZE  rcvd: 100

;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 15099
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;18.155.245.10.in-addr.arpa.    IN      PTR

;; ANSWER SECTION:
18.155.245.10.in-addr.arpa. 840 IN      PTR     ip-10-245-155-18.ec2.internal.

;; Query time: 0 msec
;; SERVER: 172.16.0.23#53(172.16.0.23)
;; WHEN: Mon Jun 24 20:48:21 2013
;; MSG SIZE  rcvd: 87

;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 28878
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;159.119.255.10.in-addr.arpa.   IN      PTR

;; ANSWER SECTION:
159.119.255.10.in-addr.arpa. 43140 IN   PTR     domU-12-31-39-01-70-51.compute-1.internal.

;; Query time: 0 msec
;; SERVER: 172.16.0.23#53(172.16.0.23)
;; WHEN: Mon Jun 24 20:48:21 2013
;; MSG SIZE  rcvd: 100

;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 28727
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;102.197.31.10.in-addr.arpa.    IN      PTR

;; ANSWER SECTION:
102.197.31.10.in-addr.arpa. 840 IN      PTR     ip-10-31-197-102.ec2.internal.

;; Query time: 0 msec
;; SERVER: 172.16.0.23#53(172.16.0.23)
;; WHEN: Mon Jun 24 20:48:21 2013
;; MSG SIZE  rcvd: 87
{% endcodeblock %}

In short:

{% codeblock %}
ip-10-125-90-172.ec2.internal.
ip-10-245-155-18.ec2.internal.
ip-10-31-197-102.ec2.internal.
domU-12-31-39-01-70-51.compute-1.internal.
domU-12-31-39-0B-B0-01.compute-1.internal.
domU-12-31-39-0C-B8-2E.compute-1.internal.
{% endcodeblock %}


The `ip-*.ec2.internal` are clearly in US East. The `domU-*.computer-1.internal` also
look like US East although I'm not 100% sure what is the difference between the two.
The later ones look like HVM guests while the former ones are para-virtualized.

For comparison here are some internal addresses from my own EC2 systems:

* ip-10-228-237-207.eu-west-1.compute.internal - EU Ireland
* ip-10-248-19-46.us-west-2.compute.internal - US West Oregon
* ip-10-160-58-141.us-west-1.compute.internal - US West N. California


After relocating my audio files to an S3 bucket in US East the average call length
dropped from 2:30 min to 2:00 min for the same IVR choices. This also minimizes
the costs since Twilio charges per minute of incoming/outgoing calls.
I think the audio quality has improved as well.


