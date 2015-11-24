---
layout: post
Title: Combining PDF Files On The Command Line
date: 2012-07-12 11:06
comments: true
categories: ['tips', 'RHEL']
---

**VERSION**

Red Hat Enterprise Linux 6

**PROBLEM**

You have to create a single PDF file by combining multiple files -
for example individually scanned pages.

**ASSUMPTIONS**

You know how to start a shell and havigate to the directory containing the files.

**SOLUTION**

If individual PDF files are named, for example, `doc_01.pdf`, `doc_02.pdf`, `doc_03.pdf`,
`doc_04.pdf`, then you can combine them with the `gs` command:


        $ gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=mydocument.pdf doc_*.pdf

The resulting PDF file will contain all pages from the individual files.

**MORE INFO**

The `gs` command is part of the [ghostscript](http://www.ghostscript.com/) rpm package.
You can find more about it using `man gs`, the documentation file `/usr/share/doc/ghostscript-*/index.html`
or <http://www.ghostscript.com>.
