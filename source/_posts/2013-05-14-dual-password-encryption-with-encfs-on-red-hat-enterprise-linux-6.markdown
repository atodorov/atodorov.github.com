---
layout: post
title: "Dual Password Encryption With EncFS On Red Hat Enterprise Linux 6"
date: 2013-05-14 21:26
comments: true
categories: ['RHEL']
---

This article is a step-by-step guide to using two passwords with [EncFS](http://www.arg0.net/encfs).
The primary password is required and may be used to secure all data;
the secondary password is optional and may be stored on USB stick or
other removable media and used to secure more sensitive data. 

<img src="/images/encfs_raleigh.jpg" alt="Article in Raleigh" style="clear:both;display:block;"/>
The original article in Red Hat's Raleigh HQ!

This article has been originally written for and published by
[Red Hat Magazine](http://magazine.redhat.com/2007/06/13/dual-password-encryption-with-encfs/).
Here is a shortened version with updated commands for Red Hat Enterprise Linux 6.

Technical Information
----------------------

EncFS provides an encrypted filesystem in user-space. EncFS provides security
against offline attacks like a stolen notebook.
EncFS works on files and directories, not an entire block device.
It modifies file names and contents.
The data is stored on the underlying filesystem and meta-data is preserved.
File attributes such as ownership, modification date and permission bits are not encrypted
and are visible to anybody. EncFS is acting like a translator between the user and
the filesystem, encrypting and decrypting on the fly.


EncFS is easy to use and requires no special setup. A local user has to be in the ‘fuse’
group to use EncFS. It does not require ‘root’ privileges.
EncFS can be used with secondary passwords. This could be used to store a separate set of files on the same encrypted filesystem. 
EncFS ignores files which do not decode properly, so files created with separate passwords will 
only be visible when the filesystem is mounted with the associated password.
There is the option to read passwords from an external program or stdin (standard input). 
This option combined with custom scripting makes EncFS very flexible.
By default, all FUSE based filesystems are visible only to the user who mounted them. 
No other users (including root) can view the filesystem contents.


Installing EncFS
-----------------

Install fuse-encfs from [EPEL](https://fedoraproject.org/wiki/EPEL):

    # yum install fuse-encfs

Load the FUSE module:

    # /sbin/modprobe fuse

And, finally, add any users that will use EncFS to group ‘fuse’:

    # usermod -Gfuse jdoe

Using EncFS
-----------

Using EncFS does not differ from using any other filesystem.
The only thing you need to do is to mount it somewhere and start creating 
files and directories under the mount point.

**Warning:** Use only absolute path names with EncFS!

Create working directories:

    $ mkdir -p ~/encrypted ~/plain

* `plain/` – looks like a normal directory. All files stored here look like normal
files for the user who mounted this directory with EncFS. This acts like a virtual
directory performing encryption and decryption.
* `encrypted/` – looks garbled. The actual data is stored here and is encrypted.

Now you can mount the new EncFS volume for the first time. This assumes a default configuration:

    $ encfs /home/jdoe/encrypted /home/jdoe/plain
    Creating new encrypted volume.
    Please choose from one of the following options:
     enter "x" for expert configuration mode,
     enter "p" for pre-configured paranoia mode,
     anything else, or an empty line will select standard mode.
    ?> 
    
    Standard configuration selected.
    
    Configuration finished.  The filesystem to be created has
    the following properties:
    Filesystem cipher: "ssl/aes", version 3:0:2
    Filename encoding: "nameio/block", version 3:0:1
    Key Size: 192 bits
    Block Size: 1024 bytes
    Each file contains 8 byte header with unique IV data.
    Filenames encoded using IV chaining mode.
    File holes passed through to ciphertext.
    
    Now you will need to enter a password for your filesystem.
    You will need to remember this password, as there is absolutely
    no recovery mechanism.  However, the password can be changed
    later using encfsctl.
    
    New Encfs Password: **********
    Verify Encfs Password: **********


Create a file:

    $ echo "some content" > ~/plain/file.one

Check contents in `plain/`:

    $ ls -la ~/plain/
    total 12
    drwxrwxr-x. 2 jdoe jdoe 4096 May 14 21:31 .
    drwx------. 6 jdoe jdoe 4096 May 14 21:29 ..
    -rw-rw-r--. 1 jdoe jdoe   13 May 14 21:31 file.one
    
    $ cat ~/plain/file.one 
    some content

Check what’s in `encrypted/`:

    $ ls -la ~/encrypted/
    total 16
    drwxrwxr-x. 2 jdoe jdoe 4096 May 14 21:31 .
    drwx------. 6 jdoe jdoe 4096 May 14 21:29 ..
    -rw-rw-r--. 1 jdoe jdoe 1083 May 14 21:30 .encfs6.xml
    -rw-rw-r--. 1 jdoe jdoe   21 May 14 21:31 Wq5NZ6q-yP-fYNWYsjzFhHf9

**Warning:** `.encfs6.xml` is a special file. When performing backups or restoring data,
make sure to keep this file!

Inspect the contents of encrypted file:

    $ cat ~/encrypted/Wq5NZ6q-yP-fYNWYsjzFhHf9 
    ���r�N�M���"p��

Unmount the filesystem and mount it again with another password:

    $ fusermount -u ~/plain/
    $ encfs --anykey /home/jdoe/encrypted /home/jdoe/plain
    EncFS Password: *****

**Caution:** We are using the --anykey option to allow secondary passwords.

Check `plain/` again. The directory is empty. Previous files were not decoded with the new password.

    $ ls -la ~/plain/
    total 8
    drwxrwxr-x. 2 jdoe jdoe 4096 May 14 21:31 .
    drwx------. 6 jdoe jdoe 4096 May 14 21:29 ..

Now create another file that will be in “hidden” mode:

    $ echo "hidden contents" > ~/plain/file.two

Check again what’s in `encrypted/`. Both files are stored in the same directory:

    $ ls -la ~/encrypted/
    total 20
    drwxrwxr-x. 2 jdoe jdoe 4096 May 14 21:35 .
    drwx------. 6 jdoe jdoe 4096 May 14 21:29 ..
    -rw-rw-r--. 1 jdoe jdoe 1083 May 14 21:30 .encfs6.xml
    -rw-rw-r--. 1 jdoe jdoe   24 May 14 21:35 PfkZHs16YsKkznnTujaVsOuS
    -rw-rw-r--. 1 jdoe jdoe   21 May 14 21:31 Wq5NZ6q-yP-fYNWYsjzFhHf9

Unmount and mount again using the first password:

    $ fusermount -u ~/plain/
    $ encfs --anykey /home/jdoe/encrypted /home/jdoe/plain
    EncFS Password: **********

Inspect the contents of `plain/` again. The second file was not decoded properly and is not shown:

    $ ls -la ~/plain/
    total 12
    drwxrwxr-x. 2 jdoe jdoe 4096 May 14 21:35 .
    drwx------. 6 jdoe jdoe 4096 May 14 21:29 ..
    -rw-rw-r--. 1 jdoe jdoe   13 May 14 21:31 file.one

Summary
-------

You have learned how to use encryption to protect your data.
There is also a nice graphical application 
for using EncFS with KDE called [K-EncFS](http://kde-apps.org/content/show.php?content=54078).
I'll be happy to answer any questions or comments.
