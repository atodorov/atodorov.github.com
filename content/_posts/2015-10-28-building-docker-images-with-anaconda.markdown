---
layout: post
Title: Building Docker Images with Anaconda
date: 2015-10-28 16:10
comments: true
Tags: fedora.planet
---

Anaconda, the Fedora and Red Hat Enterprise Linux installer, has gained some
features to facilitate building Docker images. These are only available
in kickstart. To build a Docker image for HTTPD, using packages provided in the
distro use the following ks.cfg file:

    install
    lang en_US.UTF-8
    keyboard us
    network --onboot yes --device eth0 --bootproto dhcp

    rootpw  --lock
    firewall --disabled
    timezone Europe/Sofia

    clearpart --all --initlabel
    part / --fstype=ext4 --size=1 --grow

    bootloader --disabled

    %packages --nocore --instLangs=en_US --excludedocs
    httpd
    -kernel
    yum-langpacks # workaround for rhbz#1271766
    %end

The above kickstart file will:

* install HTTPD and its dependencies
* disable kernel installation by excluding it from the package list
* disable installation of the boot loader using `--disabled`. The resulting image
will not be bootable
* disable firewall
* locks the root account so it can't login from the console
* prevent installing @core using `--nocore`
* limit the installation of localization files using `--instLangs`
* limit the installation of documentation using `--excludedocs`

**Note:** the previous `--nobase` option is deprected and doesn't have any effect.


After the VM installation is complete grab the contents of the root directory:

    # virt-tar-out -a /var/lib/libvirt/images/disk.qcow2 / myimage.tar


Import the tarball into Docker and inspect the result:

    # docker import myimage.tar local_images:ver1.0
    8a2324e6d0e940a998b990262335894a17d261450c33f57dc153d3d1987e4fc1
    
    # docker images
    REPOSITORY                                             TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
    local_images                                           ver1.0              8a2324e6d0e9        13 seconds ago      320.6 MB
    registry.access.redhat.com/rhel                        latest              82ad5fa11820        6 weeks ago         158.3 MB
    registry.access.redhat.com/rhscl_beta/httpd-24-rhel7   latest              55a8a150cf2d        9 weeks ago         201.1 MB

Run commands into a new container: 

    # docker run --name=bash_myimage -it 8a2324e6d0e9 /bin/bash
    bash-4.2# cat /etc/redhat-release 
    Red Hat Enterprise Linux Server release 7.2 Beta (Maipo)
    bash-4.2# rpm -q httpd
    httpd-2.4.6-40.el7.x86_64
    bash-4.2# exit

    # docker ps -a
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
    64f7ca6d5844        8a2324e6d0e9        "/bin/bash"         24 seconds ago      Exited (0) 19 seconds ago                       bash_myimage


As you can see the resulting image is bigger than stock images provided by Red Hat.
At this moment I don't know if this is the minimum package set which satisfies
dependencies or anaconda adds a bit more on its own. The full package list is
given below. There are some packages like  device-mapper, dracut, e2fsprogs,
iptables, kexec-tools, SELinux related, systemd and tzdata which look out
of place. My guess is some of them are pulled in from the various kickstart
commands and not really necessary. I will follow up with devel and see if
the content can be stripped down even more.

For more information check out these docs:

* [Get Started with Docker Formatted Container Images on Red Hat Systems](https://access.redhat.com/articles/881893)
* [Chapter 7. Get Started with Docker Formatted Container Images](https://access.redhat.com/documentation/en/red-hat-enterprise-linux-atomic-host/version-7/red-hat-enterprise-linux-atomic-host-7-getting-started-with-containers/chapter-7-get-started-with-docker-formatted-container-images)

Full package list:

    acl-2.2.51-12.el7.x86_64
    apr-1.4.8-3.el7.x86_64
    apr-util-1.5.2-6.el7.x86_64
    audit-libs-2.4.1-5.el7.x86_64
    basesystem-10.0-7.el7.noarch
    bash-4.2.46-19.el7.x86_64
    bind-libs-lite-9.9.4-29.el7.x86_64
    bind-license-9.9.4-29.el7.noarch
    binutils-2.23.52.0.1-54.el7.x86_64
    bzip2-libs-1.0.6-13.el7.x86_64
    ca-certificates-2015.2.4-71.el7.noarch
    chkconfig-1.3.61-5.el7.x86_64
    chrony-2.1.1-1.el7.x86_64
    coreutils-8.22-15.el7.x86_64
    cpio-2.11-24.el7.x86_64
    cracklib-2.9.0-11.el7.x86_64
    cracklib-dicts-2.9.0-11.el7.x86_64
    cryptsetup-libs-1.6.7-1.el7.x86_64
    curl-7.29.0-25.el7.x86_64
    cyrus-sasl-lib-2.1.26-19.2.el7.x86_64
    dbus-1.6.12-13.el7.x86_64
    dbus-glib-0.100-7.el7.x86_64
    dbus-libs-1.6.12-13.el7.x86_64
    dbus-python-1.1.1-9.el7.x86_64
    device-mapper-1.02.107-5.el7.x86_64
    device-mapper-libs-1.02.107-5.el7.x86_64
    dhclient-4.2.5-42.el7.x86_64
    dhcp-common-4.2.5-42.el7.x86_64
    dhcp-libs-4.2.5-42.el7.x86_64
    diffutils-3.3-4.el7.x86_64
    dracut-033-358.el7.x86_64
    dracut-network-033-358.el7.x86_64
    e2fsprogs-1.42.9-7.el7.x86_64
    e2fsprogs-libs-1.42.9-7.el7.x86_64
    ebtables-2.0.10-13.el7.x86_64
    elfutils-libelf-0.163-3.el7.x86_64
    elfutils-libs-0.163-3.el7.x86_64
    ethtool-3.15-2.el7.x86_64
    expat-2.1.0-8.el7.x86_64
    file-libs-5.11-31.el7.x86_64
    filesystem-3.2-20.el7.x86_64
    findutils-4.5.11-5.el7.x86_64
    firewalld-0.3.9-14.el7.noarch
    gawk-4.0.2-4.el7.x86_64
    gdbm-1.10-8.el7.x86_64
    glib2-2.42.2-5.el7.x86_64
    glibc-2.17-105.el7.x86_64
    glibc-common-2.17-105.el7.x86_64
    gmp-6.0.0-11.el7.x86_64
    gnupg2-2.0.22-3.el7.x86_64
    gobject-introspection-1.42.0-1.el7.x86_64
    gpgme-1.3.2-5.el7.x86_64
    grep-2.20-2.el7.x86_64
    gzip-1.5-8.el7.x86_64
    hardlink-1.0-19.el7.x86_64
    hostname-3.13-3.el7.x86_64
    httpd-2.4.6-40.el7.x86_64
    httpd-tools-2.4.6-40.el7.x86_64
    info-5.1-4.el7.x86_64
    initscripts-9.49.30-1.el7.x86_64
    iproute-3.10.0-54.el7.x86_64
    iptables-1.4.21-16.el7.x86_64
    iputils-20121221-7.el7.x86_64
    kexec-tools-2.0.7-37.el7.x86_64
    keyutils-libs-1.5.8-3.el7.x86_64
    kmod-20-5.el7.x86_64
    kmod-libs-20-5.el7.x86_64
    kpartx-0.4.9-85.el7.x86_64
    krb5-libs-1.13.2-10.el7.x86_64
    langtable-0.0.31-3.el7.noarch
    langtable-data-0.0.31-3.el7.noarch
    langtable-python-0.0.31-3.el7.noarch
    libacl-2.2.51-12.el7.x86_64
    libassuan-2.1.0-3.el7.x86_64
    libattr-2.4.46-12.el7.x86_64
    libblkid-2.23.2-26.el7.x86_64
    libcap-2.22-8.el7.x86_64
    libcap-ng-0.7.5-4.el7.x86_64
    libcom_err-1.42.9-7.el7.x86_64
    libcurl-7.29.0-25.el7.x86_64
    libdb-5.3.21-19.el7.x86_64
    libdb-utils-5.3.21-19.el7.x86_64
    libedit-3.0-12.20121213cvs.el7.x86_64
    libffi-3.0.13-16.el7.x86_64
    libgcc-4.8.5-4.el7.x86_64
    libgcrypt-1.5.3-12.el7_1.1.x86_64
    libgpg-error-1.12-3.el7.x86_64
    libidn-1.28-4.el7.x86_64
    libmnl-1.0.3-7.el7.x86_64
    libmount-2.23.2-26.el7.x86_64
    libnetfilter_conntrack-1.0.4-2.el7.x86_64
    libnfnetlink-1.0.1-4.el7.x86_64
    libpwquality-1.2.3-4.el7.x86_64
    libselinux-2.2.2-6.el7.x86_64
    libselinux-python-2.2.2-6.el7.x86_64
    libsemanage-2.1.10-18.el7.x86_64
    libsepol-2.1.9-3.el7.x86_64
    libss-1.42.9-7.el7.x86_64
    libssh2-1.4.3-10.el7.x86_64
    libstdc++-4.8.5-4.el7.x86_64
    libtasn1-3.8-2.el7.x86_64
    libuser-0.60-7.el7_1.x86_64
    libutempter-1.1.6-4.el7.x86_64
    libuuid-2.23.2-26.el7.x86_64
    libverto-0.2.5-4.el7.x86_64
    libxml2-2.9.1-5.el7_1.2.x86_64
    lua-5.1.4-14.el7.x86_64
    lzo-2.06-8.el7.x86_64
    mailcap-2.1.41-2.el7.noarch
    ncurses-5.9-13.20130511.el7.x86_64
    ncurses-base-5.9-13.20130511.el7.noarch
    ncurses-libs-5.9-13.20130511.el7.x86_64
    nspr-4.10.8-1.el7_1.x86_64
    nss-3.19.1-17.el7.x86_64
    nss-softokn-3.16.2.3-13.el7_1.x86_64
    nss-softokn-freebl-3.16.2.3-13.el7_1.x86_64
    nss-sysinit-3.19.1-17.el7.x86_64
    nss-tools-3.19.1-17.el7.x86_64
    nss-util-3.19.1-3.el7_1.x86_64
    openldap-2.4.40-8.el7.x86_64
    openssl-libs-1.0.1e-42.el7_1.9.x86_64
    p11-kit-0.20.7-3.el7.x86_64
    p11-kit-trust-0.20.7-3.el7.x86_64
    pam-1.1.8-12.el7_1.1.x86_64
    pcre-8.32-15.el7.x86_64
    pinentry-0.8.1-14.el7.x86_64
    pkgconfig-0.27.1-4.el7.x86_64
    popt-1.13-16.el7.x86_64
    procps-ng-3.3.10-3.el7.x86_64
    pth-2.0.7-23.el7.x86_64
    pygobject3-base-3.14.0-3.el7.x86_64
    pygpgme-0.3-9.el7.x86_64
    pyliblzma-0.5.3-11.el7.x86_64
    python-2.7.5-34.el7.x86_64
    python-decorator-3.4.0-3.el7.noarch
    python-iniparse-0.4-9.el7.noarch
    python-libs-2.7.5-34.el7.x86_64
    python-pycurl-7.19.0-17.el7.x86_64
    python-slip-0.4.0-2.el7.noarch
    python-slip-dbus-0.4.0-2.el7.noarch
    python-urlgrabber-3.10-7.el7.noarch
    pyxattr-0.5.1-5.el7.x86_64
    qrencode-libs-3.4.1-3.el7.x86_64
    readline-6.2-9.el7.x86_64
    redhat-logos-70.0.3-4.el7.noarch
    redhat-release-server-7.2-7.el7.x86_64
    rpm-4.11.3-17.el7.x86_64
    rpm-build-libs-4.11.3-17.el7.x86_64
    rpm-libs-4.11.3-17.el7.x86_64
    rpm-python-4.11.3-17.el7.x86_64
    sed-4.2.2-5.el7.x86_64
    setup-2.8.71-6.el7.noarch
    shadow-utils-4.1.5.1-18.el7.x86_64
    shared-mime-info-1.1-9.el7.x86_64
    snappy-1.1.0-3.el7.x86_64
    sqlite-3.7.17-8.el7.x86_64
    systemd-219-19.el7.x86_64
    systemd-libs-219-19.el7.x86_64
    sysvinit-tools-2.88-14.dsf.el7.x86_64
    tzdata-2015g-1.el7.noarch
    ustr-1.0.4-16.el7.x86_64
    util-linux-2.23.2-26.el7.x86_64
    xz-5.1.2-12alpha.el7.x86_64
    xz-libs-5.1.2-12alpha.el7.x86_64
    yum-3.4.3-132.el7.noarch
    yum-langpacks-0.4.2-4.el7.noarch
    yum-metadata-parser-1.1.4-10.el7.x86_64
    zlib-1.2.7-15.el7.x86_64
