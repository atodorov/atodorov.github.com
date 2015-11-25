---
layout: post
Title: Tip: Running DNF Plugins from git
date: 2015-11-23 15:50
comments: true
Tags: QA, fedora.planet, tips
---

This is mostly for self reference because it is not currently documented
in the code. To use dnf plugins from a local git checkout modify your
`/etc/dnf/dnf.conf` and add the following line under the `[main]` section:

    pluginpath=/path/to/dnf-plugins-core/plugins

