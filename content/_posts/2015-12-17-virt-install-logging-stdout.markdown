Title: Logging VM installation to stdout
date: 2015-12-17 14:34
comments: true
Tags: fedora.planet

Recently I've been using virt-install to create virtual machines inside some
automated tests and then ssh'ing to the VM guest and inspecting the results.
What's been bothering me is that while the VM is installing I can't see what's
going on. The solution is to log everything to stdout which is then collected
by my test harness and archived on the file server. To do this

    setenforce 0
    virt-install ... -x "console=ttyS0" --serial dev,path=/dev/pts/1

This puts SELinux into Permissive mode, instructs the VM guest to use a serial
console and then redirects the serial console to stdout on the host. If you have
SELinux in Enforcing mode then you get the following error:

    unable to set security context 'system_u:object_r:svirt_image_t:s0:c43,c440' on '/dev/pts/1': Permission denied

**NOTE:** if you execute this from a script and there is no controlly tty it will
fail. The next best thing you can do is log to a file with
`--serial file,path=guest.log` and collect this file for later!
