---
layout: post
Title: How Do You Test Thai Scalable Fonts
date: 2014-03-17 22:51
comments: true
Tags: 'Fedora', 'QA'
---

Recently I wrote about [testing fonts](/blog/2014/03/04/how-do-you-test-fonts/).
I finally managed to get an answer from the authors of *thai-scalable-fonts*.

{% blockquote Theppitak Karoonboonyanan, Fonts-TLWG %}

> * What is your approach for testing Fonts-TLWG?

It's not automated test. What it does is generate PDF with sample
texts at several sizes (the waterfall), pangrams, and glyph table.
It needs human eyes to investigate.

> * What kind of problems is your test suite designed for ?

- Shaping
- Glyph coverage
- Metrics

We also make use of fontforge features to make spotting errors
easier, such as
- Show extremas
- Show almost vertical/horizontal lines/curves
{% endblockquote %}
