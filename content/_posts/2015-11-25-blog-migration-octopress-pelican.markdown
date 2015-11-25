---
layout: post
Title: Blog Migration: from Octopress to Pelican
date: 2015-11-25 17:24
comments: true
Tags: fedora.planet, Django
---

Finally I have migrated this blog from [Octopress](http://octopress.org) to
[Pelican](https://github.com/getpelican/pelican). I am using the
[clean-blog](https://github.com/gilsondev/pelican-clean-blog/) theme with
[modifications](https://github.com/gilsondev/pelican-clean-blog/pull/3).

See the
[pelican_migration](https://github.com/atodorov/atodorov.github.com/commits/pelican_migration)
branch for technical details. Here's the summary:

* I removed pretty much everything that Octopress uses, only left the content files;
* I've added my own CSS overrides;
* I had several Octopress pages, these were merged and converted into blog posts;
* In Octopress all titles had quotes, which were removed using sed;
* Octopress categories were converted to Pelican tags and removed quotes around them,
again using sed;
* Manually updated Octopress's `{% codeblock %}` and `{% blockquote %}` tags to
match Pelican syntax. This is the biggest content change;
* I was trying to keep as much as the original URLs as possible. `ARTICLE_URL`,
`ARTICLE_SAVE_AS`, `TAG_URL`, `TAG_SAVE_AS`, `FEED_ALL_ATOM` and `TAG_FEED_ATOM`
are the relevant settings. For 50+ posts I had to manually specify the `Slug:`
variable so that they match existing Octopress URLs. Verifying the resulting names
was as simple as diffing the file listings from both Octopress and Pelican.
**NOTE:** The *fedora.planet* tag changed its URL because there's no way
to assign slugs for tags in Pelican. The new URL is missing the dot! Luckily
I make use of this only in one place which was manually updated!

I've also found a few bugs and missing functionality:

* There's no `rake new_post` counterpart in Pelican;
* As far as I can tell the preview server doesn't regenerate files automatically;
* Pelican will merge code blocks and quotes which follow one after another
but are separated with a newline in Markdown. This makes it visually impossible
to distinguish code from two files, or quotes from two people, which are published
without any other comments in between;
* The syntax doesn't allow to specify filename or a quote title when publishing
code blocks and quotes. Octopress did that easily. I will be happy with something
like `:::python settings.py`.
* There's no way to specify slugs for tag URLs in order to keep compatibility
with existing URLs.

I will be filling Issues and pull requests for both Pelican and the clear-blog theme
in the next few days so stay tuned!
