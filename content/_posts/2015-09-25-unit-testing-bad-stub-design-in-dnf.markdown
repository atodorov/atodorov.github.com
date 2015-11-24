---
layout: post
Title: Unit Testing Example - Bad Stub Design in DNF
date: 2015-09-25 11:20
comments: true
categories: ["QA", "fedora.planet"]
---

In software testing, usually unit testing, test stubs are programs that simulate
the behaviors of external dependencies that a module undergoing the test depends
on. Test stubs provide canned answers to calls made during the test.

I've discovered an improperly written stub method in one of
[DNF](http://dnf.baseurl.org/)'s tests:

{% codeblock lang:python tests/test_download.py %}
class DownloadCommandTest(unittest.TestCase):
    def setUp(self):
        def stub_fn(pkg_spec):
            if '.src.rpm' in pkg_spec:
                return Query.filter(sourcerpm=pkg_spec)
            else:
                q = Query.latest()
                return [pkg for pkg in q if pkg_spec == pkg.name]

        cli = mock.MagicMock()
        self.cmd = download.DownloadCommand(cli)
        self.cmd.cli.base.repos = dnf.repodict.RepoDict()

        self.cmd._get_query = stub_fn
        self.cmd._get_query_source = stub_fn
{% endcodeblock %}

The replaced methods look like this:

{% codeblock lang:python plugins/download.py %}
    def _get_query(self, pkg_spec):
        """Return a query to match a pkg_spec."""
        subj = dnf.subject.Subject(pkg_spec)
        q = subj.get_best_query(self.base.sack)
        q = q.available()
        q = q.latest()
        if len(q.run()) == 0:
            msg = _("No package " + pkg_spec + " available.")
            raise dnf.exceptions.PackageNotFoundError(msg)
        return q

    def _get_query_source(self, pkg_spec):
        """"Return a query to match a source rpm file name."""
        pkg_spec = pkg_spec[:-4]  # skip the .rpm
        nevra = hawkey.split_nevra(pkg_spec)
        q = self.base.sack.query()
        q = q.available()
        q = q.latest()
        q = q.filter(name=nevra.name, version=nevra.version,
                     release=nevra.release, arch=nevra.arch)
        if len(q.run()) == 0:
            msg = _("No package " + pkg_spec + " available.")
            raise dnf.exceptions.PackageNotFoundError(msg)
        return q
{% endcodeblock %}

As seen here *stub_fn* replaces the *_get_query* methods from the class under
test. At the time of writing this has probably seemed like a good idea to
speed up writing the tests.

The trouble is we should be replacing the external dependencies of *_get_query*
(other parts of DNF essentially) and not methods from *DownloadCommand*. To
understand why this is a bad idea check
[PR #113](https://github.com/rpm-software-management/dnf-plugins-core/pull/113),
which directly modifies *_get_query*. There's no way to test this patch
with the current state of the test.

So I took a few days to experiment and update the current test stubs. The
result is 
[PR #118](https://github.com/rpm-software-management/dnf-plugins-core/pull/118).
The important bits are the *SackStub* and *SubjectStub* classes which hold
information about the available RPM packages on the system. The rest are cosmetics
to fit around the way the query objects are used (q.available(), q.latest(), q.filter()).
The proposed design correctly overrides the external dependencies on
*dnf.subject.Subject* and *self.base.sack* which are initialized before our
plugin is loaded by DNF.

I must say this is the first error of this kind I've seen in my QA practice so far.
I have no idea if this was a minor oversight or something which happens more frequently
in open source projects but it's a great example nevertheless.

For those of you who'd like to get started on unit testing I can recommend the book
<a href="http://www.amazon.com/gp/product/1933988274/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1933988274&linkCode=as2&tag=atodorovorg-20">The Art of Unit Testing: With Examples in .Net</a><img src="http://www.assoc-amazon.com/e/ir?t=atodorovorg-20&l=as2&o=1&a=1933988274" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
by Roy Osherove!

**UPDATE**: Part 2 with more practical examples can be found
[here](/blog/2015/11/23/bad-stub-design-in-dnf/).
