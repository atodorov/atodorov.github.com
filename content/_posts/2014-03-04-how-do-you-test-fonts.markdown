---
layout: post
Title: How do You Test Fonts
date: 2014-03-04 21:30
comments: true
categories: ['Fedora', 'QA']
---

[Previously](/blog/2014/03/03/last-week-in-fedora-qa/) I mentioned about testing
fonts but didn't have any idea how this is done. Authors
Khaled Hosny of [Amiri Font](http://www.amirifont.org/) and Steve White of
[GNU FreeFont](http://www.gnu.org/software/freefont/) provided valuable insight
and material for further reading. I've asked them:

* What is your approach for testing ?
* What kind of problems is your test suite designed for ?

Here's what they say:

{% blockquote Khaled Hosny, Amiri Font %}
Currently my test suite consists of text strings (or lists of code
points) and expected output glyph sequences and then use HarfBuzz
(through its hb-shape command line tool) to check that the fonts always
output the expected sequence of glyphs, sometimes with the expected
positioning as well. Amiri is a complex font that have many glyph
substitution and positioning rules, so the test suite is designed to
make sure those rules are always executed correctly to catch regressions
in the font (or in HarfBuzz, which sometimes happens since the things I
do in my fonts are not always that common).

I think Lohit project do similar testing for their fonts, and HarfBuzz
itself has a similar test suite with a bunch of nice scripts (though
they are not installed when building HarfBuzz, yet[1]).

Recently I added more kinds of tests, namely checking that OTS[2]
sanitizes the fonts successfully as this is important for using them on
the web, and a test for a common mistakes I made in my feature files
that result in unexpected blank glyphs in the fonts.
{% endblockquote %}

1. <https://github.com/behdad/harfbuzz/pull/12>
2. <https://github.com/khaledhosny/ots>




{% blockquote Steve White, GNU FreeFont %}
The answer is complicated.  I'll do what I can to answer.

First, the FontForge application has a "verification" function which
can be run from a script, and which identifies numerous technical
problems.

FontForge also has a "Find Problems" function that I run by hand.

The monospaced face has special restrictions, first that all glyphs of
non-zero width must be of the same width, and second, that all glyphs
lie within the vertical bounds of the font.

Beside this, I have several other scripts that check for a few things
that FontForge doesn't (duplicate names, that glyph slots agree with
Unicode code within Unicode character blocks).

Several tests scripts have yet to be uploaded to the version control
system -- because I'm unsure of them.

There is a more complicated check of TrueType tables, which attempts
to find cases of tables that have been "shadowed" by the
script/language specification of another table.  This is helpful, but
works imperfectly.

ALL THAT SAID,

In the end, every script used in the font has to be visually checked.
This process takes me weeks, and there's nothing systematic about it,
except that I look at printout of documents in each language to see if
things have gone awry.

For a few documents in a few languages, I have images of how text
*should* look, and can compare that visually (especially important for
complex scripts.)

A few years back, somebody wrote a clever script that generated images
of text and compared them pixel-by-pixel.  This was a great idea, and
I wish I could use it more effectively, but the problem was that it
was much too sensitive.  A small change to the font (e.g. PostScript
parameters) would cause a small but global change in the rendering.
Also the rendering could vary from one version of the rendering
software to another.  So I don't use this anymore.

That's all I can think of right now.

In fact, testing has been a big problem in getting releases out.  In
the past, each release has taken at least two weeks to test, and then
another week to fix and bundle...if I was lucky.  And for the past
couple of years, I just haven't been able to justify the time
expenditure.  (Besides this, there are still a few serious problems
with the fonts--once again, a matter of time.)

Have a look at the bugs pages, to get an idea of work being done.
{% endblockquote %}

<http://savannah.gnu.org/bugs/?group=freefont>

I'm not sure if ImageMagic or PIL can help solve the rendering and compare
problem Steve is talking about. They can definitely be used for
[image comparison](/blog/2013/05/17/linux-and-python-tools-to-compare-images/)
so maybe coupled with some rendering library it's worth a quick try.


If you happen to know more about fonts, please join me in 
[improving overall test coverage in Fedora](/blog/2014/02/28/action-improving-test-coverage-in-fedora/)
by designing test suites for fonts packages.
