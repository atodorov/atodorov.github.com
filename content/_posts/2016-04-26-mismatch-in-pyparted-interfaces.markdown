Title: Mismatch in Pyparted Interfaces
Headline: revealed by newly added tests
date: 2016-04-26 10:50
comments: true
tags: QA, Python, fedora.planet

Last week my co-worker Marek Hruscak, from Red Hat, found an interesting case of
mismatch between the two interfaces provided by pyparted. In this article
I'm going to give an example, using simplified code and explain what is
happening. From pyparted's documentation we learn the following

> pyparted is a set of native Python bindings for libparted.  libparted is the
> library portion of the GNU parted project.  With pyparted, you can write
> applications that interact with disk partition tables and filesystems.
> 
> The Python bindings are implemented in two layers.  Since libparted itself
> is written in C without any real implementation of objects, a simple 1:1
> mapping of externally accessible libparted functions was written.  This
> mapping is provided in the _ped Python module.  You can use that module if
> you want to, but it's really just meant for the larger parted module.
> 
>     _ped       libparted Python bindings, direct 1:1: function mapping
>     parted     Native Python code building on _ped, complete with classes,
>                exceptions, and advanced functionality.

The two interfaces are the `_ped` and `parted` modules. As a user I expect them
to behave exactly the same but they don't. For example some partition properties
are read-only in libparted and `_ped` but not in `parted`. This is the mismatch
I'm talking about.

Consider the following tests (also available on
[GitHub](https://github.com/atodorov/pyparted/tree/not_read_only_demo))

    :::diff
    diff --git a/tests/baseclass.py b/tests/baseclass.py
    index 4f48b87..30ffc11 100644
    --- a/tests/baseclass.py
    +++ b/tests/baseclass.py
    @@ -168,6 +168,12 @@ class RequiresPartition(RequiresDisk):
             self._part = _ped.Partition(disk=self._disk, type=_ped.PARTITION_NORMAL,
             self._part = _ped.Partition(disk=self._disk, type=_ped.PARTITION_NORMAL,
                                         start=0, end=100, fs_type=_ped.file_system_type_get("ext2"))
     
    +        geom = parted.Geometry(self.device, start=100, length=100)
    +        fs = parted.FileSystem(type='ext2', geometry=geom)
    +        self.part = parted.Partition(disk=self.disk, type=parted.PARTITION_NORMAL,
    +                                    geometry=geom, fs=fs)
    +
    +
     # Base class for any test case that requires a hash table of all
     # _ped.DiskType objects available
     class RequiresDiskTypes(unittest.TestCase):
    diff --git a/tests/test__ped_partition.py b/tests/test__ped_partition.py
    index 7ef049a..26449b4 100755
    --- a/tests/test__ped_partition.py
    +++ b/tests/test__ped_partition.py
    @@ -62,8 +62,10 @@ class PartitionGetSetTestCase(RequiresPartition):
             self.assertRaises(exn, setattr, self._part, "num", 1)
             self.assertRaises(exn, setattr, self._part, "fs_type",
                 _ped.file_system_type_get("fat32"))
    -        self.assertRaises(exn, setattr, self._part, "geom",
    -                                     _ped.Geometry(self._device, 10, 20))
    +        with self.assertRaises((AttributeError, TypeError)):
    +#            setattr(self._part, "geom", _ped.Geometry(self._device, 10, 20))
    +            self._part.geom = _ped.Geometry(self._device, 10, 20)
    +
             self.assertRaises(exn, setattr, self._part, "disk", self._disk)
     
             # Check that values have the right type.
    diff --git a/tests/test_parted_partition.py b/tests/test_parted_partition.py
    index 0a406a0..8d8d0fd 100755
    --- a/tests/test_parted_partition.py
    +++ b/tests/test_parted_partition.py
    @@ -23,7 +23,7 @@
     import parted
     import unittest
     
    -from tests.baseclass import RequiresDisk
    +from tests.baseclass import RequiresDisk, RequiresPartition
     
     # One class per method, multiple tests per class.  For these simple methods,
     # that seems like good organization.  More complicated methods may require
    @@ -34,11 +34,11 @@ class PartitionNewTestCase(unittest.TestCase):
             # TODO
             self.fail("Unimplemented test case.")
     
    -@unittest.skip("Unimplemented test case.")
    -class PartitionGetSetTestCase(unittest.TestCase):
    +class PartitionGetSetTestCase(RequiresPartition):
         def runTest(self):
    -        # TODO
    -        self.fail("Unimplemented test case.")
    +        with self.assertRaises((AttributeError, TypeError)):
    +            #setattr(self.part, "geometry", parted.Geometry(self.device, start=10, length=20))
    +            self.part.geometry = parted.Geometry(self.device, start=10, length=20)
     
     @unittest.skip("Unimplemented test case.")
     class PartitionGetFlagTestCase(unittest.TestCase):

The test in `test__ped_partition.py` works without problems, I've modified it for
visual reference only. This was also the inspiration behind the test in
`test_parted_partition.py`. However the second test fails with

    ======================================================================
    FAIL: runTest (tests.test_parted_partition.PartitionGetSetTestCase)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/tmp/pyparted/tests/test_parted_partition.py", line 41, in runTest
        self.part.geometry = parted.Geometry(self.device, start=10, length=20)
    AssertionError: (<type 'exceptions.AttributeError'>, <type 'exceptions.TypeError'>) not raised
    
    ----------------------------------------------------------------------


Now it's clear that something isn't quite the same between the two interfaces.
If we look at `src/parted/partition.py` we see the following snippet

    137     fileSystem = property(lambda s: s._fileSystem, lambda s, v: setattr(s, "_fileSystem", v))
    138     geometry = property(lambda s: s._geometry, lambda s, v: setattr(s, "_geometry", v))
    139     system = property(lambda s: s.__writeOnly("system"), lambda s, v: s.__partition.set_system(v))
    140     type = property(lambda s: s.__partition.type, lambda s, v: setattr(s.__partition, "type", v))

The geometry property is indeed read-write but the system property is write-only.
`git blame` leads us to the interesting
[commit 2fc0ee2b](https://github.com/rhinstaller/pyparted/commit/2fc0ee2b), which changes
definitions for quite a few properties and removes the `_readOnly` method which raises
an exception. Even more interesting is the fact that the `Partition.geometry` property
hasn't been changed. If you look closer you will notice that the deleted definition and
the new one are exactly the same. Looks like the problem existed even before this change.

Digging down even further we find
[commit 7599aa1](https://github.com/rhinstaller/pyparted/commit/7599aa1ae505f3784ca4936b58b38b8dffb752ff)
which is the very first implementation of the `parted` module. There you can see the
`_readOnly` method and some properties like `path` and `disk` correctly marked as such
but `geometry` isn't.

Shortly after this commit the first test was added (4b9de0e) and a bit
later the second, empty test class, was added (c85a5e6). This only goes
to show that every piece of software needs appropriate QA coverage, which
pyparted was kind of lacking (and I'm trying to change that).

The reason this bug went unnoticed for so long
is the limited exposure of pyparted. To my knowledge anaconda, the Fedora installer
is its biggest (if not single) consumer and maybe it uses only the `_ped`
interface (I didn't check) or it doesn't try to do silly things like setting
a value to a read-only property.

**
The lesson from this story is to test all of your interfaces and also
make sure they are behaving in exactly the same manner!
**

Thanks for reading and happy testing!

