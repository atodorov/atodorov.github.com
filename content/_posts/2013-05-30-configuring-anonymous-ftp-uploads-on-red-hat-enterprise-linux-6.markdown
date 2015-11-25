---
layout: post
Title: Configuring Anonymous FTP Uploads On Red Hat Enterprise Linux 6
date: 2013-05-30 13:07
comments: true
Tags: RHEL, tips
---

Install related packages and make configuration changes:

    yum -y install vsftp policycoreutils-python
    sed -i "s/#anon_upload_enable=YES/anon_upload_enable=YES/" /etc/vsftpd/vsftpd.conf

Configure writable directory for uploads:

    mkdir /var/ftp/pub/upload
    chgrp ftp /var/ftp/pub/upload
    chmod 730 /var/ftp/pub/upload

Configure SELinux - this is **[MISSING](https://bugzilla.redhat.com/show_bug.cgi?id=968935)**
from Red Hat's official docs:

    setsebool -P allow_ftpd_anon_write=1
    semanage fcontext -a -t public_content_rw_t '/var/ftp/pub/upload(/.*)'
    chcon -t public_content_rw_t /var/ftp/pub/upload


Start the service:

    chkconfig vsftpd on
    service vsftpd start
