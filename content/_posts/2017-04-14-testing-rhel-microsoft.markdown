Title: Testing Red Hat Enterprise Linux the Microsoft way
Headline: practical pairwise experiment
date: 2017-04-14 09:18
comments: true
Tags: QA, fedora.planet
og_image: images/microsoft-redhat-puzzle.jpg
twitter_image: images/microsoft-redhat-puzzle.jpg

![Microsoft and Red Hat logos](/images/microsoft-redhat-puzzle.jpg "Microsoft and Red Hat logos")

Pairwise (a.k.a. all-pairs) testing is an effective test case generation
technique that is based on the observation that most faults are caused by
interactions of at most two factors! Pairwise-generated test suites cover
all combinations of two therefore are much smaller than exhaustive ones yet
still very effective in finding defects. This technique has been pioneered by
Microsoft in testing their products. For an example please see
[their GitHub repo](https://github.com//microsoft/pict)!

I heard about pairwise testing by
[Niels Sander Christensen](https://www.linkedin.com/in/niels-sander-christensen-a2639b1/)
last year at
[QA Challenge Accepted 2.0](http://qachallengeaccepted.com/2016.html#agenda2016) and
I immediately knew where it would fit into my test matrix.

This article describes an experiment made during Red Hat Enterprise Linux 6.9
installation testing campaign. The experiment covers generating a
test plan (referred to Pairwise Test Plan) based on the pairwise test strategy and
some heuristics. The goal was to reduce the number of test cases which needed to be
executed and still maintain good test coverage (in terms of breadth of testing) and
also maintain low risk for the product.


Product background
==================

For RHEL 6.9 there are 9 different product variants each comprising of particular
package set and CPU architecture:

* Server i386
* Server x86_64
* Server ppc64 (IBM Power)
* Server s390x (IBM mainframe)
* Workstation i386
* Workstation x86_64
* Client i386
* Client x86_64
* ComputeNode x86_64

Traditional testing activities are classified as Tier #1, Tier #2 and Tier #3

* Tier #1 - basic form of installation testing. Executed for all arch/variants on all builds,
  including nightly builds. This group includes the most common installation methods and configurations.
  If Tier #1 fails the product is considered unfit for customers and further testing blocking the release!
* Tier #2 and #3 - includes additional installation configurations and/or functionality which is deemed important.
  These are still fairly common scenarios but not the most frequently used ones.
  If some of the Tier#2 and #3 test cases fail they will not block the release.


This experiment focuses only on Tier #2 and #3 test cases because they generate the
largest test matrix! This experiment is related only to installation testing of RHEL.
This broadly means *"Can the customer install RHEL via the Anaconda installer and boot
into the installed system"*.
I do not test functionality of the system after reboot!

**I have theorized that from the point of view of installation testing RHEL is mostly a
platform independent product!**

Individual product variants rarely exhibit differences in their functional behavior
because they are compiled from the same code base! If a feature is present it should work
the same on all variants. The main differences between variants are:

* What software has been packaged as part of the variant (e.g. base package set and add-on repos);
* Whether or not a particular feature is officially supported, e.g. iBFT on Client variants.
  Support is usually provided via including the respective packages in the variant package set
  and declaring SLA for it.

These differences may lead to problems with resolving dependencies and missing packages
but historically haven't shown significant tendency to cause functional failures
e.g. using NFS as installation source working on Server but not on Client.

The main component being tested, Anaconda - the installer, is also mostly platform independent.
In a previous experiment I had collected code coverage data from Anaconda while
performing installation with the same kickstart (or same manual options) on various architectures.
The coverage report supports the claim that Anaconda is platform independent!
See
[Anaconda & coverage.py - Pt.3 - coverage-diff, section Kickstart vs. Kickstart]({filename}2015-10-27-anaconda-coverage.py-coverage-diff.markdown)!


Testing approach
================

The traditional pairwise approach focuses on features whose functionality is
controlled via parameters. For example: RAID level, encryption cipher, etc.
**I have taken this definition one level up and applied it to the entire product!
Now functionality is also controlled by variant and CPU architecture!**
This allows me to reduce the number of total test cases in the test matrix but still
execute all of them at least once!

The initial implementation used a simple script, built with
[the Ruby pairwise gem](https://github.com/josephwilk/pairwise), that:

* Copies verbatim all test cases which are applicable for a single product variant,
    for example s390x Server or ppc64 Server! There's nothing we can do to reduce these
    from combinatorial point of view!

* Then we have the group of test cases with input parameters. For example:

        storage / iBFT / No authentication / Network init script
        storage / iBFT / CHAP authentication / Network Manager
        storage / iBFT / Reverse CHAP authentication / Network Manager

    In this example the test is `storage / iBFT` and the parameters are

    * Authentication type
        * None
        * CHAP
        * Reverse CHAP
    * Network management type
        * SysV init
        * NetworkManager

    For test cases in this group I also consider the CPU architecture and OS variant
    as part of the input parameters and combine them using pairwise. Usually this results
    in around 50% reduction of test efforts compared to testing against all product variants!

* Last we have the group of test cases which don't depend on any input parameters,
    for example `partitioning / swap on LVM`. They are grouped together (wrt their applicable variants)
    and each test case is executed only once against a randomly chosen product variant!
    This is my own heuristic based on the fact that the product is platform
    independent!

    **NOTE:** You may think that for these test cases the product variant is their input parameter.
    If we consider this to be the case then we'll not get any reduction because of
    how pairwise generation works (the 2 parameters with the largest number of possible values determine
    the maximum size of the test matrix). In this case the 9 product variants is the largest set of values!

For this experiment
[pairwise_spec.rb](https://gist.github.com/atodorov/8f44022e209f749c7121f91281aa641e)
only produced the list of test scenarios (test cases) to be executed! It doesn't
schedule test execution and it doesn't update the
[test case management system]({filename}2017-04-04-nitrate-methods-and-tools.markdown)
with actual results. It just tells you what to do! Obviously this script
will need to integrate with other systems and processes as defined by the organization!

Example results:

    RHEL 6.9 Tier #2 and #3 testing
      Test case w/o parameters can't be reduced via pairwise
        x86_64 Server - partitioning / swap on LVM
        x86_64 Workstation - partitioning / swap on LVM
        x86_64 Client - partitioning / swap on LVM
        x86_64 ComputeNode - partitioning / swap on LVM
        i386 Server - partitioning / swap on LVM
        i386 Workstation - partitioning / swap on LVM
        i386 Client - partitioning / swap on LVM
        ppc64 Server - partitioning / swap on LVM
        s390x Server - partitioning / swap on LVM
      Test case(s) with parameters can be reduced by pairwise
        x86_64 Server - rescue mode / LVM / plain
        x86_64 ComputeNode - rescue mode / RAID / encrypted
        x86_64 Client - rescue mode / RAID / plain
        x86_64 Workstation - rescue mode / LVM / encrypted
        x86_64 Server - rescue mode / RAID / encrypted
        x86_64 Workstation - rescue mode / RAID / plain
        x86_64 Client - rescue mode / LVM / encrypted
        x86_64 ComputeNode - rescue mode / LVM / plain
        i386 Server - rescue mode / LVM / plain
        i386 Client - rescue mode / RAID / encrypted
        i386 Workstation - rescue mode / RAID / plain
        i386 Workstation - rescue mode / LVM / encrypted
        i386 Server - rescue mode / RAID / encrypted
        i386 Workstation - rescue mode / RAID / encrypted
        i386 Client - rescue mode / LVM / plain
        ppc64 Server - rescue mode / LVM / plain
        s390x Server - rescue mode / RAID / encrypted
        s390x Server - rescue mode / RAID / plain
        s390x Server - rescue mode / LVM / encrypted
        ppc64 Server - rescue mode / RAID / encrypted
    
    Finished in 0.00602 seconds (files took 0.10734 seconds to load)
    29 examples, 0 failures

In this example there are 9 (variants) * 2 (partitioning type) * 2 (encryption type) == 32
total combinations! As you can see pairwise reduced them to 20! Also notice that
if you don't take CPU arch and variant into account you are left with
2 (partitioning type) * 2 (encryption type) == 4 combinations for each product variant
and they can't be reduced on their own!


Acceptance criteria
===================

I did evaluate all bugs which were found by executing the test cases from the
pairwise test plan and compared them to the list of all bugs found by the team.
This will tell me how good my pairwise test plan was compared to the regular one.
"good" meaning:

* How many bugs would I find if I don't execute the full test matrix
* How many critical bugs would I miss if I don't execute the full test matrix

Results:

* Pairwise found **14 new bugs**;
* **23 bugs were first found by regular test plan**
    * some by test cases not included in this experiment;
    * pairwise totally **missed 4 bugs**!

Pairwise test plan **missed 3 critical regressions** due to:

* Poor planning of pairwise test activity. There was a regression in
  one of the latest builds and that particular test was simply not executed!
* Human factor aka me not being careful enough and not following the process diligently.
  I waived a test due to infrastructure issues while there was a bug which stayed undiscovered!
  I should have tried harder to retest this scenario after fixing my infrastructure!
* Architecture and networking specific regression which wasn't tested on multiple levels and
  is very narrow corner case.
  Can be mitigated with more testing upstream, more automation and better understanding of the hidden test
  requirements (e.g. IPv4 vs IPv6) for all of which pairwise can help (analysis and more available resources).

All of the missed regressions could have been missed by regular test plan as well, however the risk of missing
them in pairwise is higher b/c of the reduced test matrix and the fact that
you may not execute exactly the same test scenario for quite a long time.
OTOH the risk can be mitigated with more automation b/c we now have more free resources.

IMO pairwise test plan did a good job and didn't introduce "dramatic" changes in risk level for the product!


Summary
=======

* 65 % reduction in test matrix;
* Only 1/3rd of team engineers needed;
    * keep arch experts around though;
* 2/3rd of team engineers could be free for automation and to create even more test cases;
* Test run execution completion rate is comparable to regular test plan
    * average execution completion for pairwise test plan was 76%!
    * average execution completion for regular test plan was 85%!
* New bugs found:
    * 30% by Pairwise Test Plan
    * 30% by Tier #1 test cases (good job here)
    * 30% by exploratory testing
* Risk of missing regressions or critical bugs exists (I did miss 3) but can be mitigated;
* Clearly exposes the need of constant review, analysis and improvement of existing test cases;
* Exposes hidden parameters in test scenarios and some hidden relationships;
* Patterns and other optimization techniques observed


Patterns observed:

* Many new test case combinations found, which I had to describe into
  [Nitrate]({filename}2017-04-04-nitrate-methods-and-tools.markdown); The longer you use
  pairwise the less new combinations are discovered (aka undocumented scenarios).
  The first 3 initial test runs discovered the most of the missing combinations!
* Found quite a few test cases with hidden parameters, for example `swap / recommended`
  which calculates the recommended size of swap partition based on 4 different
  ranges in which the actual RAM size fits! These ranges became parameters
  to the test case;
* Can combine (2, 3, etc) independent test cases together and consider them as parameters
  so we can apply pairwise against the combination. This will create new scenarios, broaden
  the test matrix but not result in significant increase in execution time. I didn't try this
  because it was not the focus of the experiment;
* Found some redundant/duplicate test cases - test plans need to be constantly analyzed and
  maintained you know;
* Automated scheduling and tools integration is critical. This needs to be working perfectly
  in order to capitalize on the newly freed resources;
* Testing on s390x was sub-optimal (mostly my own inexperience with the platform) so for
  specialized environments we still want to keep the experts around;
* 1 engineer (me) was able to largely keep up with schedule with the rest of the team!
    * experiment was conducted during the course of several months
    * I have tried to adhere to all milestones and deadlines and mostly succeeded

I have also discovered ideas for new test execution optimization techniques
which need to be evaluated and measured further:

* Use a common set-up step for multiple test cases across variants, e.g.
    * install a RAID system then;
    * perform 3 rescue mode tests (same test case, different variants)
* Pipeline test cases so that the result of one case is the setup for the next, e.g.
    * install a RAID system and test for correctness of the installation;
    * perform rescue mode test;
    * damage one of the RAID partitions while still in rescue mode;
    * test installation with damaged disks - it should not crash!

These techniques can be used stand-alone or in combination with
other optimization techniques and tooling available to the team. They are
specific to my particular kind of testing so beware of your surroundings
before you try them out!


Thanks for reading and happy testing!

*Cover image copyright: cio-today.com*
