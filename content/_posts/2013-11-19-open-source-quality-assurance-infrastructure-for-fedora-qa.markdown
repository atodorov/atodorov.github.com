---
layout: post
Title: Open Source Quality Assurance Infrastructure for Fedora QA
date: 2013-11-19 14:12
comments: true
categories: ['Fedora', 'QA']
---

!["Beaker test lab"](/images/fedora/beaker.png "Beaker test lab")

In the last few weeks I've been working together with 
[Tim Flink](https://fedoraproject.org/wiki/User:Tflink) and
[Kamil Paral](https://fedoraproject.org/wiki/User:Kparal) from the Fedora QA
team on bringing some installation testing expertise to Fedora and establishing
an [open source test lab](http://beaker.fedoraproject.org/bkr/)
to perform automated testing in. The infrastructure is
already in relatively usable condition so I've decided to share this information
with the community. 

Beaker is Running Our Test Lab
------------------------------

[Beaker](http://beaker-project.org/) is the software suite that powers the test
lab infrastructure. It is quite complex, with many components and sometimes not
very straight-forward to set up. Tim has been working on that with me giving it
a try and reporting issues as they have been discovered and fixed. 

In the process of working on this I've managed to create
[couple of patches](http://gerrit.beaker-project.org/#/q/owner:%22Alexander+Todorov%22,n,z)
against Beaker and friends. They are still pending release in a future version
because of more urgent bug fixes which need to released first.

SNAKE is The Kickstart Template Server
--------------------------------------

[SNAKE](https://fedorahosted.org/snake/) is a client/server Python framework used
to support Anaconda installations. It supports plain text ks.cfg files, IIRC those
were static templates, no variable substitution.

The other possibility is Python templates based on Pykickstart:

{% codeblock lang:python %}
from pykickstart.constants import KS_SCRIPT_POST
from pykickstart.parser import Script
from installdefaults import InstallKs

def ks(**context):
    '''Anaconda autopart'''

    ks=InstallKs()
    ks.packages.add(['@base'])

    ks.clearpart(initAll=True)
    ks.autopart(autopart=True)

    script = '''
cp /tmp/ks.cfg /mnt/sysimage/root/ks.cfg || \
cp /run/install/ks.cfg /mnt/sysimage/root/ks.cfg
'''
    post = Script(script, type=KS_SCRIPT_POST, inChroot=False)
    ks.scripts.append(post)

    return ks
{% endcodeblock %}

At the moment SNAKE is essentially abandoned but feature complete.
I'm thinking about adopting the project just in case we need to make some fixes.
Will let you know more about this when it happens. 

Open Source Test Suite
----------------------

I have been working on opening up several test cases for what we (QE) call
a tier #1 installation test suite. They can be found in
[git](http://taskbot.cloud.fedoraproject.org/cgit/fedora-beaker-tests/).
The tests are base on [beakerlib](https://fedorahosted.org/beakerlib/) and
the legacy RHTS framework which is now part of Beaker.

This effort has been coordinated with Kamil as part of a pilot
project he's responsible for. I've been executing the same test suite against
earlier Fedora 20 snapshots but using an internal environment. Now everything
is going out in the open.

Executing The Tests
-------------------

Well you can't do that - YET! There are command line client tools for Fedora
but Beaker and SNAKE are not well suited for use outside a restricted network
like LAN or VPN. There are issues with authentication most notably for SNAKE.

At the moment I have to ssh through two different systems to get proper access.
However this is been worked on. I've read about a rewrite which will allow Beaker
to utilize a custom authentication framework like FAS for example. Hopefully that
will be implemented soon enough.

I will also like to see the test systems have direct access to the Internet for
various reasons but this is not without its risks either. This is still to be
decided.

If you are interested anyway see the `kick-tests.sh` file in the test suite for
examples and command line options.

Test Results
------------

The first successfully completed
[test jobs](http://beaker.fedoraproject.org/bkr/jobs/) are jobs 50 to 58.
There's a failure in one of the test cases, namely SELinux related 
[RHBZ #1027148](https://bugzilla.redhat.com/show_bug.cgi?id=1027148).

From what I can tell the lab is now working as expected and we can start doing
some testing against Fedora development snapshots.

Ping me or join #fedora-qa on irc.freenode.net if you'd like to join Fedora QA!
