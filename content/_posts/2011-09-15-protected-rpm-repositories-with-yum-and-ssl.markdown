---
layout: post
Title: Protected RPM repositories with yum and SSL
date: 2011-09-15 19:40
comments: true
Tags: RHEL
---

In this article I'm going to describe a simple way to set-up RPM repositories with access control using only standard tools such as yum, SSL and Apache.
I've been talking about this at one of the monthly conferences of Linux for Bulgarians!

<strong>Objective:</strong><br />
Create RPM repository with access control. Access is allowed only for some systems and forbidden for the rest. This is a similar to what Red Hat Network does. 

<strong>Solution:</strong><br />
We're going to use yum and Apache capabilities to work with SSL certificates. The client side (yum) will identify itself using SSL certificate and the server (Apache) will use this information to control the access.

<strong>Client side set-up:</strong><br />
<ol>
  <li>
Yum version 3.2.27 or newer supports SSL certificates for client authentication. This version is available in Red Hat Enterprise Linux 6. 
  </li>

  <li>
First you need to generate a private key and certificate using OpenSSL:
```
# openssl genrsa -out /var/lib/yum/client.key 1024
Generating RSA private key, 1024 bit long modulus
....++++++
.......++++++
e is 65537 (0x10001)

# openssl req -new -x509 -text -key /var/lib/yum/client.key -out /var/lib/yum/client.cert
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:BG
State or Province Name (full name) []:Sofia
Locality Name (eg, city) [Default City]:Sofia
Organization Name (eg, company) [Default Company Ltd]:Open Technologies Bulgaria
Organizational Unit Name (eg, section) []:IT
Common Name (eg, your name or your server's hostname) []:
Email Address []:no-spam@otb.bg
```
  </li>

  <li>
For better security you can change file permissions of <em>client.key</em>:
```
# chmod 600 /var/lib/yum/client.key
```
  </li>

  <li>
You need to define the protected repository in a .repo file. It needs to look something like this:
```
# cat /etc/yum.repos.d/protected.repo
[protected]
name=SSL protected repository
baseurl=https://repos.example.com/protected
enabled=1
gpgcheck=1
gpgkey=https://repos.example.com/RPM-GPG-KEY

sslverify=1
sslclientcert=/var/lib/yum/client.cert
sslclientkey=/var/lib/yum/client.key
```
  </li>

  <li>
If you use self-signed server certificate you can specify  <em>sslverify=0</em>, but this is not recommended.
  </li>
</ol>

Whenever yum tries to reach the URL of the repository it will identify itself using the specified certificate.

<strong>Server side set-up:</strong><br />
<ol>
  <li>
Install and configure the <em>mod_ssl</em> module for Apache.
  </li>

  <li>
Create a directory for the repository which will be available over HTTPS.
  </li>

  <li>
In the repository directory add <em>.htaccess</em>, which looks something like this:
```
Action rpm-protected /cgi-bin/rpm.cgi
AddHandler rpm-protected .rpm .drpm
SSLVerifyClient optional_no_ca
```
  </li>

  <li>
The <em>Action</em> and <em>AddHandler</em> directives instruct Apache to run the <em>rpm.cgi</em> CGI script every time someone tries to access files with extension .rpm and .drpm.
  </li>

  <li>
The <em>SSLVerifyClient</em> directive tells Apache that the http client may present a valid certificate but it has not to be (successfully) verifyable.
For more information on this configuration please see
<a href="http://www.modssl.org/docs/2.1/ssl_reference.html#ToC13">http://www.modssl.org/docs/2.1/ssl_reference.html#ToC13</a>.
  </li>

  <li>
The simplest form of <em>rpm.cgi</em> script may look like this:
```
#!/bin/bash

if [ "$SSL_CLIENT_M_SERIAL" == "9F938211B53B4F44" ]; then
    echo "Content-type: application/x-rpm"
    echo "Content-length: $(stat --printf='%s' $PATH_TRANSLATED)"
    echo

    cat $PATH_TRANSLATED
else
    echo "Status: 403"
    echo
fi
```
  </li>

  <li>
The script will allow access to a client which uses a certificate with serial number <em>9F938211B53B4F44</em>. Other clients will be denied access and the server will return standard 403 error code.
  </li>
</ol>

<strong>In practice:</strong><br />
The above set-up is very basic and only demonstrates the technology behind this. In a real world configuration you will need some more tools to make this really usable. 

My company [Open Technologies Bulgaria, Ltd.](http://otb.bg) has developed a custom solution for our customers based on the above example called Voyager. It features a Drupal module, a CGI script and a client side yum plugin. 

The Drupal module acts as web interface to the system and allows some basic tasks. Administrators can define software channels and subscription expiration. Customers can register and entitle their systems to particular channels. The functionality is similar to Red Hat Network but without all the extra features which we don't need.

The CGI script acts as a glue between the client side and the Drupal backend. It will read information about client credentials and act as first line of defence against non-authorized access. Then it will communicate with the Drupal database and get more information about this customer. If everything is OK then access will be allowed. 

The yum plugin has the task to communicate with the Drupal backend and dynamically update repository definitions based on available subscriptions. Then it will send a request for the RPM file back to the Apache server where the CGI script will handle it.

The client side also features a tool to generate the client certificate and register the system to the server. 

All communications are entirely over HTTPS. 

This custom solution has the advantage that it is simple and easy to maintain as well as easy to use. It integrates well with other plugins (e.g. yum-presto for delta rpm support and yum-rhnplugin) and can be used via yum or PackageKit which are the standard package management tools on Red Hat Enterprise Linux 6.
