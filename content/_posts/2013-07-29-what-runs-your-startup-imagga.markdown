---
layout: post
Title: What Runs Your Start-up - Imagga
date: 2013-07-29 12:32
comments: true
Tags: what runs, start-up, Amazon, EC2
Slug: what-runs-your-startup-imagga
---

<img src="/images/startup/imagga.png" alt="Imagga" style="float:left; margin-right:10px;" />

[Imagga](http://imagga.com/) is a cloud platform that helps businesses and 
individuals organize their images in a fast and cost-effective way. They 
develop a range of advanced proprietary image recognition and image processing
technologies, which are built into several services such as smart image
cropping, color extraction and multi-color search, visual similarity search and
auto-tagging.

During 
[Balkan Venture Forum](/blog/2013/05/23/balkan-venture-forum-sofia-post-mortem/)
in Sofia I sat down with Georgi Kadrev to talk about technology.
Surprisingly this hi-tech service is built on top of standard low-tech components
and lots of hard work.

Main Technologies
-----------------

Core functionality is developed in C and C++ with the OpenCV library. 
Imagga relies heavily on own image processing algorithms for their core
features. These were built as a combination of their own research activities
and publications from other researchers.

Image processing is executed by worker nodes configured with their own
software stack. Nodes are distributed among Amazon EC2 and other data centers.

Client libraries to access Imagga API are available in PHP, Ruby and Java.

Imagga has built several websites to showcase their technology.
[Cropp.me](http://cropp.me/), [ColorsLike.me](http://colorslike.me/),
[StockPodium](http://www.stockpodium.com) and [AutoTag.me](http://autotag.me/)
were built with PHP, JavaScript and jQuery above a standard LAMP stack.

Recently Imagga also started using GPU computing with nVidia Tesla cards.
They use C++ and Python bindings for
[CUDA](https://developer.nvidia.com/what-cuda).

Why Not Something Else?
-----------------------

> As an initially bootstrapping start-up we chose something that is basically free,
> reliable and popular - that's why started with the LAMP stack. It proved to be
> stable and convenient for our web needs and we preserved it.
> The use of C++ is a natural choice for computational intensive tasks that we
> need to perform for the purpose of our core expertise - image processing. 
> Though we initially wrote the whole core technology code from scratch, we later
> switched to OpenCV for some of the building blocks as it is very well optimized
> and continuously extended image processing library.
> 
> With the raise of affordable high-performance GPU processors and their availability
> in server instances, we decided it's time to take advantage of this highly parallel
> architecture, perfectly suitable for image processing tasks.
> 
> Georgi Kadrev

Want More Info?
---------------

If you’d like to hear more from Imagga please comment below.
I will ask them to follow this thread and reply to your questions.
