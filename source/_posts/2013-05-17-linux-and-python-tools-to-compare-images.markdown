---
layout: post
title: "Linux and Python Tools To Compare Images"
date: 2013-05-17 21:13
comments: true
categories: ['Python', 'QA']
---

How to compare two images in Python? A tricky question with quite a few answers.
Since my needs are simple, my solution is simpler!

<img src="/images/difio_compare.png" alt="Difio Google +1 changes" style="clear:both;display:block"/>
[dif.io](http://www.dif.io) homepage before and after it got a G+1.

ImageMagic is magic
-------------------

If you haven't heard of [ImageMagic](http://www.imagemagick.org/) then you've been
living in a cave on a deserted island! The suite contains the `compare` command
which mathematically and visually annotates the difference between two images.

The third image above was produced with:

    $ compare difio_10.png difio_11.png difio_diff.png

Differences are displayed in red (default) and the original image is seen in the
background. As shown, the Google +1 button and count has changed between the two
images. `compare` is a nice tool for manual inspection and debugging.
It works well in this case because the images are lossless PNGs and are regions of
screen shots where most objects are the same.


<img src="/images/chestnut_compare.jpg" alt="JPEG quality reduction" style="clear:both;display:block"/>
Chestnuts I had in Rome. 100% to 99% quality reduction.

As seen on the second image set only 1% of JPEG quality change leads to many small
differences in the image, which are invisible to the naked eye.



Python Imaging Library aka PIL
-------------------------------

[PIL](http://www.pythonware.com/products/pil/) is another powerful tool for
image manipulation. I googled around and found some answers to my original
questions
[here](http://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way).
The proposed solution is to calculate
[RMS](https://en.wikipedia.org/wiki/Root_mean_square) of the two images
and compare that with some threshold to establish the level of certainty that
two images are identical.

Simple solution
----------------

I've been working on a script lately which needs to know what is displayed on
the screen and recognize some of the objects. Calculating image similarity is
quite complex but comparing if two images are **exactly** identical is not.
Given my environment and the fact
that I'm comparing screen shots where only few areas changed
(see first image above for example) led to the following solution: 

* Take a screen shot;
* Crop a particular area of the image which needs to be examined;
* Compare to a baseline image of the same area created manually;
* Don't use RMS, use the image histogram only to speed up calculation.


I've prepared the baseline images with GIMP and tested couple of scenarios
using `compare`. Here's how it looks in code:

{% codeblock lang:python %}
from PIL import Image
from dogtail.utils import screenshot

baseline_histogram = Image.open('/home/atodorov/baseline.png').histogram()

img = Image.open(screenshot())
region = img.crop((860, 300, 950, 320))
print region.histogram() == baseline_histogram
{% endcodeblock %}


Results
-------

The presented solution was easy to program, works fast and reliably for my use case.
In fact after several iterations I've added a second baseline image to account for some
unidentified noise which appears randomly in the first region. As far as I can tell
the two checks combined are 100% accurate. 


Field of application
---------------------

I'm working on QA automation where this comes handy. However you may try some
lame CAPTCHA recognition by comparing regions to a pre-defined baseline. Let me know
if you come up with a cool idea or actually used this in code. 

I'd love to hear
about interesting projects which didn't get too complicated because of image
recognition.

