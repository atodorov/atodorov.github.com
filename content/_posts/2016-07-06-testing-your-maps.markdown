Title: Testing Data Structures in Pykickstart
Headline: or having bugs despite code coverage
date: 2016-07-06 15:10
comments: true
Tags: QA, fedora.planet

When designing automated test cases we often think either about increasing
coverage or in terms of testing more use-cases aka behavior scenarios. Both
are valid approaches to improve testing and both of them seem to focus
around execution control flow (or business logic). However program behavior
is sometimes controlled via the contents of its data structures and this is
something which is rarely tested. 

In
[this comment](https://github.com/rhinstaller/pykickstart/pull/26#discussion_r32790705)
Brian C. Lane and Vratislav Podzimek from Red Hat are talking about a data structure
which maps Fedora versions to particular implementations of kickstart commands.
For example

    :::python
    class RHEL7Handler(BaseHandler):
        version = RHEL7
    
        commandMap = {
            "auth": commands.authconfig.FC3_Authconfig,
            "authconfig": commands.authconfig.FC3_Authconfig,
            "autopart": commands.autopart.F20_AutoPart,
            "autostep": commands.autostep.FC3_AutoStep,
            "bootloader": commands.bootloader.RHEL7_Bootloader,
        }


In their particular case the Fedora 21 `logvol` implementation introduced the
`--profile` parameter but in
Fedora 22 and Fedora 23 the `logvol` command mapped to the Fedora 20 implementation and the
`--profile` parameter wasn't available. This is unexpected change in program behavior
although the `logvol.py` and `handlers/f22.py` files have
[99% and 100% code coverage](https://github.com/atodorov/pykickstart-coverage/blob/master/coverage-report.log).

This morning I did some coding and created an automated test for this problem. The test
iterates over all command maps. For each command in the map (that is data structure member)
we load the module which provides all possible implementations for that command. In the
loaded module
we search for implementations which have newer versions than what is in the map,
but not newer than the current Fedora version under test. With a little bit of pruning
the current list of offenses is

    ERROR: In `handlers/devel.py` the "fcoe" command maps to "F13_Fcoe" while in
    `pykickstart.commands.fcoe` there is newer implementation: "RHEL7_Fcoe".
    
    ERROR: In `handlers/devel.py` "FcoeData" maps to "F13_FcoeData" while in
    `pykickstart.commands.fcoe` there is newer implementation: "RHEL7_FcoeData".
    
    ERROR: In `handlers/devel.py` the "user" command maps to "F19_User" while in
    `pykickstart.commands.user` there is newer implementation: "F24_User".
    
    ERROR: In `handlers/f24.py` the "user" command maps to "F19_User" while in
    `pykickstart.commands.user` there is newer implementation: "F24_User".
    
    ERROR: In `handlers/f22.py` the "logvol" command maps to "F20_LogVol" while in
    `pykickstart.commands.logvol` there is newer implementation: "F21_LogVol".
    
    ERROR: In `handlers/f22.py` "LogVolData" maps to "F20_LogVolData" while in
    `pykickstart.commands.logvol` there is newer implementation: "F21_LogVolData".
    
    ERROR: In `handlers/f18.py` the "network" command maps to "F16_Network" while in
    `pykickstart.commands.network` there is newer implementation: "F18_Network".

The first two are possibly false negatives or related to the naming conventions used
in this module. However the rest appear to be legitimate problems. The `user` command
has introduced the `--groups` parameter in Fedora 24 (devel is Fedora 25 currently) but the
parser will fail to recognize this parameter. The `logvol` problem is recognized as well
since it was never patched. And the Fedora 18 `network` command implements a new property called
`hostname` which has probably never been available to be used.

You can follow my current work in
[PR #91](https://github.com/rhinstaller/pykickstart/pull/91) and happy testing your
data structures.
