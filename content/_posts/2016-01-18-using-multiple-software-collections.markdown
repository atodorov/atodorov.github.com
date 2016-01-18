Title: Using Multiple Software Collections
date: 2016-01-18 14:00
comments: true
Tags: fedora.planet, RHEL, tips

[Software Collections](https://www.softwarecollections.org) are never versions
of system wide packages used typically on Red Hat Enterprise Linux. They are
installed together with the system-wide versions and can be used to develop
applications without affecting the system tools.

If you need to use a software collection then enable it like so:

    scl enable rh-ruby22 /bin/bash


You can enable a second (and third, etc) software collection by executing `scl`
again:

    scl enable nodejs010 /bin/bash


After executing the above two commands I have:

    $ which ruby
    /opt/rh/rh-ruby22/root/usr/bin/ruby
    $ which node
    /opt/rh/nodejs010/root/usr/bin/node

Now I can develop an application using Ruby 2.2 and Node.js 0.10.
