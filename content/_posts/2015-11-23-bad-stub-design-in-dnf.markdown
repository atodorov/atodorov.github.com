---
layout: post
Title: Bad Stub Design in DNF, Pt.2 
date: 2015-11-23 15:55
comments: true
Tags: 'QA', 'fedora.planet'
---

Do you remember my example of a
[bad stub design in DNF](/blog/2015/09/25/unit-testing-bad-stub-design-in-dnf/) ?
At that time I didn't have a good example of why this is a bad design and what are the
consequences of it. Today I have!

From my comment on
[PR #118](https://github.com/rpm-software-management/dnf-plugins-core/pull/118)
{% blockquote %}
Note: the benefit of this patch are quite subtle.
I've played around with creating a few more tests and the benefit I see affect
only a few lines of code.

For #114 there doesn't seem to be any need to test _get_query directly,
although we call
```
       q = self.base.sack.query()
       q = q.available()
```

which will benefit from this PR b/c we're stubbing out the entire Sack object.
I will work on a test later today/tomorrow to see how it looks.

OTOH for #113 where we modify _get_query the test can look something like this:

```
    def test_get_query_with_local_rpm(self):
        try:
            (fs, rpm_path) = tempfile.mkstemp('foobar-99.99-1.x86_64.rpm')
            # b/c self.cmd.cli.base is a mock object add_remote_rpm
            # will not update the available packages while testing.
            # it is expected to hit an exception
            with self.assertRaises(dnf.exceptions.PackageNotFoundError):
                self.cmd._get_query(rpm_path)
            self.cmd.cli.base.add_remote_rpm.assert_called_with(rpm_path)
        finally:
            os.remove(rpm_path)
```

Note the comment above the with block. If we leave out `_get_query` as before
(a simple stub function) we're not going to be able to use `assert_called_with`
later.
{% endblockquote %}


Now a more practical example. See 
[commit fe13066](https://github.com/rpm-software-management/dnf-plugins-core/commit/fe130669ffc4c1d6eba8f10cda35ab4d803d5a3d)
- in case the package is not found we log the error. In case configuration is
`strict=True` then the plugin will raise another exception. With the initial version
of the stubs this change in behavior is silently ignored. If there was an error
in the newly introduced lines it would go straight into production because the
existing tests passed.

What happens is that `test_get_packages()` calls `_get_packages(['notfound'])`,
which is not the real code but a test stub and returns an empty list in this case.
The empty list is expected from the test and it will not fail!

With my new stub design the test will execute the actual `_get_packages()`
method from `download.py` and choke on the exception. The test itself needs
to be modified, which is done in
[commit 2c2b34](https://github.com/atodorov/dnf-plugins-core/commit/2c2b34237c99cbf32e23bde43027d22873f4e8b7)
and no further errors were found.


So let me summarize:
**
When using mocks, stubs and fake objects we should be replacing external
dependencies of the software under test, not internal methods from the SUT!
**
