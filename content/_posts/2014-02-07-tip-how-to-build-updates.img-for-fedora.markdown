---
layout: post
Title: Tip: How to Build updates.img for Fedora
date: 2014-02-07 11:01
comments: true
Tags: tips, Fedora
---

Anaconda the Fedora, CentOS and Red Hat Enterprise Linux installer has the
capability to incorporate
[updates at runtime](https://fedoraproject.org/wiki/Anaconda/Updates).
These updates are generally distributed as an `updates.img` file. Here is how
to easily build one from a working installation tree.

Instead of using the git sources to build an updates.img I prefer using the SRPM
from the tree which I am installing. <strike>This way the resulting updates image will be
more consistent with the anaconda version already available in the tree. And in theory
everything you need to build it should already be available as well.</strike>
**UPDATE 2014-02-08:** You can also build the `updates.img` from the git source tree
which is shown at the bottom of this article. 

The following steps work for me on a Fedora 20 system. 

* Download the source RPM for anaconda from the tree and extract the sources to a working
directory. Then;

        :::bash
        cd anaconda-20.25.16-1
        git init
        git add .
        git commit -m "initial import"
        git tag anaconda-20.25.16-1

* The above steps will create a local git repository and tag the initial contents before
modification. The tag is required later by the script which creates the updates image;

* After making your changes commit them and from the top anaconda directory execute:

        :::bash
        ./scripts/makeupdates -t anaconda-20.25.16-1

You can also add RPM contents to the updates.img but you need to download the packages first:

    :::bash
    yumdownloader python-coverage python-setuptools
    
    ./scripts/makeupdates -t anaconda-20.25.16-1 -a ~/python-coverage-3.7-1.fc20.x86_64.rpm -a ~/python-setuptools-1.4.2-1.fc20.noarch.rpm 
    BUILDDIR /home/atodorov/anaconda-20.25.16-1
    Including anaconda
    2 RPMs added manually:
    python-setuptools-1.4.2-1.fc20.noarch.rpm
    python-coverage-3.7-1.fc20.x86_64.rpm
    cd /home/atodorov/anaconda-20.25.16-1/updates && rpm2cpio /home/atodorov/python-setuptools-1.4.2-1.fc20.noarch.rpm | cpio -dium
    3534 blocks
    cd /home/atodorov/anaconda-20.25.16-1/updates && rpm2cpio /home/atodorov/python-coverage-3.7-1.fc20.x86_64.rpm | cpio -dium
    1214 blocks
    <stdin> to <stdout> 4831 blocks
    
    updates.img ready

In the above example I have only modified the top level anaconda file (`/usr/sbin/anaconda`
inside the installation environment) experimenting with
[python-coverage](http://nedbatchelder.com/code/coverage/) integration.

You are done! Make the `updates.img` available to Anaconda and start using it!

**UPDATE 2014-02-08:** If you prefer working with the anaconda source tree here's
how to do it:

    :::bash
    git clone git://git.fedorahosted.org/git/anaconda.git
    cd anaconda/
    git checkout anaconda-20.25.16-1 -b my_feature-branch
    
    ... make changes ...
    
    git commit -a -m "Fixed something"
    
    ./scripts/makeupdates -t anaconda-20.25.16-1

