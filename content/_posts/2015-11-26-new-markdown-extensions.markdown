Title: 3 New Python Markdown extensions
date: 2015-11-26 22:24
comments: true
Tags: fedora.planet, Python

I've managed to resolve several of my issues with Python-Markdown behaving not
quite as I expect. I have the pleasure to announce three new extensions which
now power this blog.

No Lazy BlockQuote Extension
----------------------------

[Markdown-No-Lazy-BlockQuote-Extension](https://github.com/atodorov/Markdown-No-Lazy-BlockQuote-Extension)
makes it possible blockquotes separated by newline to be rendered separately.
If you want to include empty lines in your blockquotes make sure to prefix
each line with `> `. The standard behavior can be seen in
[GitHub](https://github.com/atodorov/atodorov.github.com/blob/source/content/_posts/2014-03-04-how-do-you-test-fonts.markdown)
while the changed behavior is visible
[in this article](/blog/2014/03/04/how-do-you-test-fonts/). Notice how on
GitHub both quotes are rendered as one big block, while here they are two separate
blocks.

No Lazy Code Extension
----------------------

[Markdown-No-Lazy-Code-Extension](https://github.com/atodorov/Markdown-No-Lazy-Code-Extension)
allows code blocks separated by newline to be rendered separately. If you want to
include empty lines in your code blocks make sure to
[indent them as well](https://github.com/atodorov/atodorov.github.com/commit/9684875920c6c7926951ce99b6588a9a7007e6f0).
The standard behavior can be seen on
[GitHub](https://github.com/atodorov/atodorov.github.com/blob/source/content/_posts/2013-02-13-secure-vnc-installation-red-hat-enterprise-linux.markdown)
while the improved one in this
[post](/blog/2013/02/13/secure-vnc-installation-red-hat-enterprise-linux/).
Notice how GitHub renders the code in the **Warning Bugs Present** section
as one block while in reality these are two separate blocks from two different files.

Bugzilla Extension
------------------

[Markdown-Bugzilla-Extension](https://github.com/atodorov/Markdown-Bugzilla-Extension)
allows for easy references to bugs. Strings like `[bz#123]` and `[rhbz#456]` will
be converted into links.


All three extensions are available on PyPI!

Bonus: Codehilite with filenames in Markdown
---------------------------------------------

The standard Markdown codehilite extension doesn't allow to specify filename
on the `:::python` shebang line while Octopress did and I've used the syntax
on this blog in a number of articles. The fix is simple, but requires changes in
both Markdown and Pygments. See
[PR #445](https://github.com/waylan/Python-Markdown/pull/445) for the initial
version and ongoing discussion. Example of the new `:::python settings.py` syntax
can be seen
[here](/blog/2013/03/07/python-twitter-django-social-auth-hello-new-user/).
