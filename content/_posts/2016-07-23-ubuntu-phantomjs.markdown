Title: PhantomJS 2.1.1 in Ubuntu different from upstream
Headline: when building from source build all sources
date: 2016-07-23 11:30
comments: true
Tags: QA, fedora.planet

For some time now I've been hitting
[PhantomJS #12506](https://github.com/ariya/phantomjs/issues/12506) with the
latest 2.1.1 version. The problem is supposedly fixed in 2.1.0 but this is not
always the case. If you use a .deb package from the latest Ubuntu then the problem
still exists, see
[Ubuntu #1605628](https://bugs.launchpad.net/ubuntu/+source/phantomjs/+bug/1605628).

It turns out the root cause of this, and probably other problems, is the way
PhantomJS packages are built. Ubuntu builds the package against their stock
Qt5WebKit libraries which leads to

    $ ldd usr/lib/phantomjs/phantomjs | grep -i qt
        libQt5WebKitWidgets.so.5 => /lib64/libQt5WebKitWidgets.so.5 (0x00007f5173ebf000)
        libQt5PrintSupport.so.5 => /lib64/libQt5PrintSupport.so.5 (0x00007f5173e4d000)
        libQt5Widgets.so.5 => /lib64/libQt5Widgets.so.5 (0x00007f51737b6000)
        libQt5WebKit.so.5 => /lib64/libQt5WebKit.so.5 (0x00007f5171342000)
        libQt5Gui.so.5 => /lib64/libQt5Gui.so.5 (0x00007f5170df8000)
        libQt5Network.so.5 => /lib64/libQt5Network.so.5 (0x00007f5170c9a000)
        libQt5Core.so.5 => /lib64/libQt5Core.so.5 (0x00007f517080d000)
        libQt5Sensors.so.5 => /lib64/libQt5Sensors.so.5 (0x00007f516b218000)
        libQt5Positioning.so.5 => /lib64/libQt5Positioning.so.5 (0x00007f516b1d7000)
        libQt5OpenGL.so.5 => /lib64/libQt5OpenGL.so.5 (0x00007f516b17c000)
        libQt5Sql.so.5 => /lib64/libQt5Sql.so.5 (0x00007f516b136000)
        libQt5Quick.so.5 => /lib64/libQt5Quick.so.5 (0x00007f5169dad000)
        libQt5Qml.so.5 => /lib64/libQt5Qml.so.5 (0x00007f5169999000)
        libQt5WebChannel.so.5 => /lib64/libQt5WebChannel.so.5 (0x00007f5169978000)

While building from the upstream sources gives

    $ ldd /tmp/bin/phantomjs | grep -i qt

If you take a closer look at PhantomJS's sources you will notice there are
3 git submodules in their repository - `3rdparty`, `qtbase` and `qtwebkit`.
Then in their `build.py` you can clearly see that this local fork of `QtWebKit`
is built first, then the `phantomjs` binary is built against it.

The problem is that these custom forks include additional patches to make
WebKit suitable for Phantom's needs. And these patches are not available
in the stock WebKit library that Ubuntu uses.

> Yes, that's correct. We need additional functionality that
> vanilla QtWebKit doesn't have. That's why we use custom version.
>
> Vitaly Slobodin, PhantomJS

At the moment of this writing Vitaly's qtwebkit fork is 28 commits ahead and
39 commits behind qt:dev. I'm surprised Ubuntu's PhantomJS even works.

The solution IMO is to bundle the additional sources into the src.deb package
and use the same building procedure as upstream.
