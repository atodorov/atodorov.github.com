---
layout: post
title: "2 Barcode Related Bugs in MyFitnessPal"
date: 2015-01-07 14:44
comments: true
categories: ['QA']
---

![Barcode that fails to scan](/images/barcode/fail.jpg "Barcode that fails to scan")

**Did you know that the popular *MyFitnessPal* application can't scan barcodes
printed on curved surfaces?** The above barcode fails to scan because it is
printed on a metal can full of roasted almonds :). In contrast the
*Barcode Scanner* from *ZXing Team* understands it just fine. My bet is
*MyFitnessPal* uses less advanced barcode scanning library. Judging from
the visual clues in the app the issue is between 6 and 0 where white space is wider.

![Barcode that scans fine](/images/barcode/pass.jpg "Barcode that scans fine")

Despite being a bit blurry this second barcode is printed on a flat surface and
is understood by both *MyFitnessPal* and "ZXing Barcode Scanner".

**NOTE** I get the same results regardless if I try to scan the actual barcode
printed on packaging, a picture from a mobile device screen or these two images
from the laptop screen.


**MyFitnessPal also has problems with duplicate barcodes!** Barcodes are not unique
and many producers use the same code for multiple products. I've seen this in the
case of two different varieties of salami from the same manufacturer on the good end
and two different products produced across the world (eggs and popcorn) on the
extreme end.

Once the user scans their barcodes and establish that the existing information is
not correct they can *Create a Food* and update the calories database. This is then
synced back to MyFitnesPal servers and overrides any existing information. When the same
barcode is scanned for the second time only the new DB entry is visible.

How to reproduce:

* Scan an existing barcode and enter it to MFP database if not already there;
* Scan the same barcode one more time and pretend the information is not correct;
* Click the *Create a Food* button and fill-in the fields. For example use a
different food name to distinguish between the two database entries. Save!
* From another device with different account (to verify information in DB)
scan the same barcode again. 

Actual results:
The last entered information is shown.


Expected results:
User is shown both DB records and can select between them.





