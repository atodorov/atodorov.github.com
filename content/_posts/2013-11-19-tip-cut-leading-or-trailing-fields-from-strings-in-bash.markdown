---
layout: post
Title: Tip: Cut Leading or Trailing Fields From Strings in Bash
date: 2013-11-19 00:16
comments: true
categories: ['tips', 'Fedora']
---

Today I was looking for a command sequence to cut a string in two by predefined
delimiter (e.g. like `cut` does). I wanted to get the last field only and all
fields but the last as separate variables.

The proposed solutions I've found suggested using `awk` but I don't like it.
Here's a simple solution using `cut` and `rev` which can extract arbitrary
field counts from the end of the string. 

    $ echo 'buildvm-08.phx2.fedoraproject.org' | rev | cut -f1 -d. | rev
    org
    $ echo 'buildvm-08.phx2.fedoraproject.org' | rev | cut -f-2 -d. | rev
    fedoraproject.org
    $ echo 'buildvm-08.phx2.fedoraproject.org' | rev | cut -f-3 -d. | rev
    phx2.fedoraproject.org
    $ echo 'buildvm-08.phx2.fedoraproject.org' | rev | cut -f2- -d. | rev
    buildvm-08.phx2.fedoraproject
    $ echo 'buildvm-08.phx2.fedoraproject.org' | rev | cut -f3- -d. | rev
    buildvm-08.phx2
    $ echo 'buildvm-08.phx2.fedoraproject.org' | rev | cut -f4- -d. | rev
    buildvm-08

The magic here is done by `rev` which reverses the order of characters in every
line. It comes with the *util-linux-ng* package.

**Note to Self:** *util-linux-ng* appears to contain more useful commands which
I wasn't aware of. Need to RTFM a little bit.
