---
layout: post
Title: Anaconda &amp; coverage.py - Pt.3 - coverage-diff
date: 2015-10-27 11:12
comments: true
Tags: 'QA', 'fedora.planet'
---

In my [previous post](/blog/2015/10/15/anaconda-coverage.py-details/)
I've talked about testing anaconda and friends and raised some questions.
Today I'm going to give an example of how to answer one of them:
"How different is the code execution path between different tests?"

coverate-tools
--------------

I'm going to use [coverage-tools](https://github.com/atodorov/coverage-tools)
in my explanations below so a little introduction is required. All the tools
are executable Python scripts which build on top of existing coverage.py API.
The difference is mainly in flexibility of parameters and output formatting.
I've tried to keep as close as possible to the existing behavior of coverage.py.

*coverage-annotate* - when given a .coverage data file prints the source code
annotated with line numbers and execution markers.

{% codeblock lang:python %}
!!! missing/usr/lib64/python2.7/site-packages/pyanaconda/anaconda_argparse.py
>>> covered/usr/lib64/python2.7/site-packages/pyanaconda/anaconda_argparse.py
... skip ...
    37 > import logging
    38 > log = logging.getLogger("anaconda")
    39   
    40   # Help text formatting constants
    41   
    42 > LEFT_PADDING = 8  # the help text will start after 8 spaces
    43 > RIGHT_PADDING = 8  # there will be 8 spaces left on the right
    44 > DEFAULT_HELP_WIDTH = 80
    45   
    46 > def get_help_width():
    47 >     """
    48 >     Try to detect the terminal window width size and use it to
    49 >     compute optimal help text width. If it can't be detected
    50 >     a default values is returned.
    51   
    52 >     :returns: optimal help text width in number of characters
    53 >     :rtype: int
    54 >     """
    55       # don't do terminal size detection on s390, it is not supported
    56       # by its arcane TTY system and only results in cryptic error messages
    57       # ending on the standard output
    58       # (we do the s390 detection here directly to avoid
    59       #  the delay caused by importing the Blivet module
    60       #  just for this single call)
    61 >     is_s390 = os.uname()[4].startswith('s390')
    62 >     if is_s390:
    63 !         return DEFAULT_HELP_WIDTH
    64   
... skip ...
{% endcodeblock %}

In the example above all lines starting with **>** were executed by the interpreter.
All top-level import statements were executed as you would expect. Then the method
*get_help_width()* was executed (called from somewhere). Because this was on x86_64
machine line 63 was not executed. It is marked with **!**. The comments and empty
lines are of no interest.


*coverage-diff* - produces git like diff reports on the text output of annotate.

{% codeblock lang:diff %}
--- a/usr/lib64/python2.7/site-packages/pyanaconda/ui/gui/spokes/source.py
+++ b/usr/lib64/python2.7/site-packages/pyanaconda/ui/gui/spokes/source.py
@@ -634,7 +634,7 @@
    634           # Wait to make sure the other threads are done before sending ready, otherwise
    635           # the spoke may not get be sensitive by _handleCompleteness in the hub.
    636 >         while not self.ready:
-   637 !             time.sleep(1)
+   637 >             time.sleep(1)
    638 >         hubQ.send_ready(self.__class__.__name__, False)
    639   
    640 >     def refresh(self):\
{% endcodeblock %}

In this example line 637 was not executed in the first test run, while it was executed
in the second test run. Reading the comments above it is clear the difference between
the two test runs is just timing and synchronization.

Kickstart vs. Kickstart
-----------------------

How different is the code execution path between different tests? Looking at
[Fedora 23 test results](https://fedoraproject.org/wiki/Test_Results:Fedora_23_Final_RC3_Installation)
we see several tests which differ only slightly in their setup - installation
via HTTP, FTP or NFS; installation to SATA, SCSI, SAS drives; installation using
RAID for the root file system; These are good candidates for further analysis.

Note: my results below are not from Fedora 23 but the conclusions still apply!
The tests were executed on bare metal and virtual machines, trying to use the
same hardware or same systems configurations where possible!

Example: HTTP vs. FTP
{% codeblock lang:diff %}
--- a/usr/lib64/python2.7/site-packages/pyanaconda/packaging/__init__.py
+++ b/usr/lib64/python2.7/site-packages/pyanaconda/packaging/__init__.py
@@ -891,7 +891,7 @@
    891   
    892               # Run any listeners for the new state
    893 >             for func in self._event_listeners[event_id]:
-   894 !                 func()
+   894 >                 func()
    895   
    896 >     def _runThread(self, storage, ksdata, payload, fallback, checkmount):
    897           # This is the thread entry
--- a/usr/lib64/python2.7/site-packages/pyanaconda/ui/gui/spokes/lib/resize.py
+++ b/usr/lib64/python2.7/site-packages/pyanaconda/ui/gui/spokes/lib/resize.py
@@ -102,10 +102,10 @@
    102           # Otherwise, fall back on increasingly vague information.
    103 >         if not part.isleaf:
    104 >             return self.storage.devicetree.getChildren(part)[0].name
-   105 >         if getattr(part.format, "label", None):
+   105 !         if getattr(part.format, "label", None):
    106 !             return part.format.label
-   107 >         elif getattr(part.format, "name", None):
-   108 >             return part.format.name
+   107 !         elif getattr(part.format, "name", None):
+   108 !             return part.format.name
    109 !         else:
    110 !             return ""
    111   
@@ -315,10 +315,10 @@
    315 >     def on_key_pressed(self, window, event, *args):
    316           # Handle any keyboard events.  Right now this is just delete for
    317           # removing a partition, but it could include more later.
-   318 >         if not event or event and event.type != Gdk.EventType.KEY_RELEASE:
+   318 !         if not event or event and event.type != Gdk.EventType.KEY_RELEASE:
    319 !             return
    320   
-   321 >         if event.keyval == Gdk.KEY_Delete and self._deleteButton.get_sensitive():
+   321 !         if event.keyval == Gdk.KEY_Delete and self._deleteButton.get_sensitive():
    322 !             self._deleteButton.emit("clicked")
    323   
    324 >     def _sumReclaimableSpace(self, model, path, itr, *args):
--- a/usr/lib64/python2.7/site-packages/pyanaconda/ui/gui/spokes/source.py
+++ b/usr/lib64/python2.7/site-packages/pyanaconda/ui/gui/spokes/source.py
@@ -634,7 +634,7 @@
    634           # Wait to make sure the other threads are done before sending ready, otherwise
    635           # the spoke may not get be sensitive by _handleCompleteness in the hub.
    636 >         while not self.ready:
-   637 !             time.sleep(1)
+   637 >             time.sleep(1)
    638 >         hubQ.send_ready(self.__class__.__name__, False)
    639   
    640 >     def refresh(self):
{% endcodeblock %}

The difference in `source.py` is from timing/synchronization and can safely be ignored.
I'm not exactly sure about `__init__.py` but doesn't look much of a big deal.
We're left with `resize.py`. The differences in *on_key_pressed()* are because
I've probably used the keyboard instead the mouse (these are indeed manual installs).
The other difference is in how the partition labels are displayed. One of the installs
was probably using fresh disks while the other not.


Example: SATA vs. SCSI - no difference

Example: SATA vs. SAS (mpt2sas driver)

{% codeblock lang:diff %}
--- a/usr/lib64/python2.7/site-packages/pyanaconda/bootloader.py
+++ b/usr/lib64/python2.7/site-packages/pyanaconda/bootloader.py
@@ -109,10 +109,10 @@
    109 >     try:
    110 >         opts.parity = arg[idx+0]
    111 >         opts.word   = arg[idx+1]
-   112 !         opts.flow   = arg[idx+2]
-   113 !     except IndexError:
-   114 >         pass
-   115 >     return opts
+   112 >         opts.flow   = arg[idx+2]
+   113 >     except IndexError:
+   114 !         pass
+   115 !     return opts
    116   
    117 ! def _is_on_iscsi(device):
    118 !     """Tells whether a given device is on an iSCSI disk or not."""
@@ -1075,13 +1075,13 @@
   1075 >             command = ["serial"]
   1076 >             s = parse_serial_opt(self.console_options)
   1077 >             if unit and unit != '0':
-  1078 !                 command.append("--unit=%s" % unit)
+  1078 >                 command.append("--unit=%s" % unit)
   1079 >             if s.speed and s.speed != '9600':
   1080 >                 command.append("--speed=%s" % s.speed)
   1081 >             if s.parity:
-  1082 !                 if s.parity == 'o':
+  1082 >                 if s.parity == 'o':
   1083 !                     command.append("--parity=odd")
-  1084 !                 elif s.parity == 'e':
+  1084 >                 elif s.parity == 'e':
   1085 !                     command.append("--parity=even")
   1086 >             if s.word and s.word != '8':
   1087 !                 command.append("--word=%s" % s.word)
{% endcodeblock %}

As you can see the difference is minimal, mostly related to the underlying
hardware. As far as I can tell this has to do with how the bootloader is
installed on disk but I'm no expert on this particular piece of code.
I've seen the same difference in other comparisons so it probably has to do
more with hardware than with what kind of disk/driver is used.

Example: RAID 0 vs. RAID 1 - manual install

{% codeblock lang:diff %}
--- a/usr/lib64/python2.7/site-packages/pyanaconda/ui/gui/spokes/datetime_spoke.py
+++ b/usr/lib64/python2.7/site-packages/pyanaconda/ui/gui/spokes/datetime_spoke.py
@@ -490,9 +490,9 @@
    490   
    491 >         time_init_thread = threadMgr.get(constants.THREAD_TIME_INIT)
    492 >         if time_init_thread is not None:
-   493 >             hubQ.send_message(self.__class__.__name__,
-   494 >                              _("Restoring hardware time..."))
-   495 >             threadMgr.wait(constants.THREAD_TIME_INIT)
+   493 !             hubQ.send_message(self.__class__.__name__,
+   494 !                              _("Restoring hardware time..."))
+   495 !             threadMgr.wait(constants.THREAD_TIME_INIT)
    496   
    497 >         hubQ.send_ready(self.__class__.__name__, False)
    498   
{% endcodeblock %}

As far as I can tell the difference is related to hardware clock settings,
probably due to different defaults in BIOS on the various hardware.
Additional tests with RAID 5 and RAID 6 reveals the same exact difference.
RAID 0 vs. RAID 10 shows no difference at all. Indeed as far as I know anaconda
delegates the creation of RAID arrays to mdadm once the desired configuration
is known so these results are to be expected.


Conclusion
----------

As you can see sometimes there are tests which appear to be very important
but in reality they cover a corner case of the base test. For example if any
of the RAID levels works we can be pretty confident 
<strike>all of them work</strike> *they won't break in anaconda*
(thanks Adam Williamson)!

What you do with this information is up to you. Sometimes QA is able to
execute all the tests and life is good. Sometimes we have to compromise,
skip some testing and accept the risks of doing so. Sometimes you can
execute all tests for every build, sometimes only once per milestone.
Whatever the case having the information to back up your decision is vital!


In my next post on this topic I'm going to talk more about functional tests
vs. unit tests. Both anaconda and blivet have both kinds of tests and I'm
interested to know if tests from the two categories focus on the same
functionality how are they different. If we have a unit test for feature X,
does it warrant to spend the resources doing functional testing for X as well?
