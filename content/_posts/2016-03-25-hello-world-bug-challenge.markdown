Title: Hello World QA Challenge
date: 2016-03-25 11:08
comments: true
Tags: fedora.planet, QA

Recently I've been asked on Quora
"Do simple programs like hello world have any bugs" ? In particular if the
computer hardware and OS are healthy, will there be any bugs in a simple
hello-world program?

I'm challenging you to tell me what
kinds of bugs have you seen which would easily apply to a very simple program!
Below are some I was able to think about.


Localization
------------

Once we add a requirement to our system to work in environment which supports
multiple languages and input methods, not supporting them immediately becomes a bug,
although the SUT still functions correctly. For example, if using a French locale
I would expect the program to print "Bonjour le monde". Same for German, Spanish,
Italian, etc. It even becomes trickier with languages using non-latin script like
Bulgarian and Japanese for example. Depending on your environment you may not be
able to display non-latin script at all.
See also
[How do you test fonts]({filename}2014-03-17-how-do-you-test-thai-scalable-fonts.markdown)!

Packaging and distribution
--------------------------

This is an entire class of problems not directly related to the SUT but to the way
it is packaged and distributed to its target customers. For a Linux system it makes
sense to have an RPM or DEB packages. Dependency resolution and proper installation
and upgrade for these packages need to be tested and ensured.

A famous example of a high impact packaging bug is
[Django #19858](https://code.djangoproject.com/ticket/19858). During an urgent
security release it was discovered that the source package was shipping byte-compiled
`*.pyc` files made with a newer version of Python (2.7). Even worse there were
byte-compiled files without the corresponding source files.

Being a security release everyone
rushed to upgrade immediately. Everyone who had Python 2.6 saw their website
produce `ImportError: Bad magic number` and crash immediately after the upgrade!

**NOTE:** byte-compiled files between different versions of Python are
incompatible!

Another one is
[django-facebook #262](https://github.com/tschellenbach/Django-facebook/issues/262)
in which version 4.3.0 suddenly grew from 200KiB to 23MiB in size, shipping a ton
of extra JPEG images.

Portability
-----------

There are so many different portability issues which may affect an otherwise
working program. You only need to add a requirement to build/execute on another
OS or CPU architecture - for example aarch64 (64-bit ARM).
This resulted in hundreds of bugs
reported by Dennis Gilmore, for example
[RHBZ #926850](https://bugzilla.redhat.com/show_bug.cgi?id=926850) which is also related to
packaging and the build chain.

Then we have possibility for big endian vs. little endian issues especially if
we run on Power 8 CPU which supports both modes.

Another one could be 16bit vs. 32bit vs 64bit memory addressing. For example
on platforms like IBM mainframe (s390) they reserved the most significant bit
to easily support applications expecting 24-bit addressing, as well as to
sidestep a problem with extending two instructions to handle 32-bit unsigned
addresses, which made the address space 31-bits!

Performance
------------

Not all processors are created equal! Both Intel (x86_64), ARM and PowerPC
have different instruction sets and numbers of registers. Depending on what
sort of calculations you perform one of the architectures may be more suitable
than the other.


Typos
-----

It not uncommon to mistype even common words like
"hello" and "world" and I've rarely seen QAs and developers running spell
checkers on all of their source strings. We do this for documentation and
occasionally for man pages but for the actual program output or widget labels -
almost never.


Challenge
---------

I find the original question very interesting and a good metal exercise for
IT professionals. I will be going through Bugzilla
to find examples which illustrate the above points and even more possible problems
with a program as simple as hello world and will update this blog accordingly!

Tell me what kinds of bugs have you seen which would easily apply to a very simple program!
It's best if you can post links to public bugs and/or detailed explanation.
Thanks!
