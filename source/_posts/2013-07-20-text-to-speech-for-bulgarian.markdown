---
layout: post
title: "Text To Speech for Bulgarian"
date: 2013-07-20 14:06
comments: true
categories: 
---

I've been exploring text-to-speech synthesizers for Bulgarian in the past
few weeks. I found only three. Here is my review. 

eSpeak
------

[eSpeak](http://espeak.sourceforge.net/) is a compact open source software
speech synthesizer for English and other languages, for Linux and Windows.

I'm using espeak-1.47.11-1, from Fedora - the src.rpm rebuilt on Red Hat
Enterprise Linux 6. Earlier versions do not support Bulgarian.

There is only one available voice for Bulgarian, which seems to have reasonably
good pronunciation. There are some errors though, it's not perfect. The voice
however is horrible. It's the worst computer generated voice of all solutions
I've found so far. 

Good for initial testing since it requires virtually no setup and can be used
from the command line.

SpeechLab 2.0
-------------

SpeechLab is developed by the
[Bulgarian Association for Computational Linguistics](http://www.bacl.org/speechlab.html).
There's a sample of only one voice but I was told others can be added as well. Not sure about that.

Listening to [the sample](http://www.youtube.com/watch?feature=player_embedded&v=4s2UgwYgbkM)
I think this is the most correct synthesizer of all. The voice still sounds computerized
but better compared to eSpeak. The same voice is used by local TV channels when showing
news related to [Anonymous](https://en.wikipedia.org/wiki/Anonymous_%28group%29) and
one could probably say it will be accepted by the general public if used into
a software product.

BACL has transferred the sales rights to a company called
[Aquasyst-Eco](http://aquasyst-eco.com/speechlab_2_0_server.html) which claims to have
a desktop and a server product. The server version is supposed to work on Linux too.
There is also a [version for Android](http://slideme.org/application/speechlab-2-0).

Initially I thought to use SpeechLab but BACL and the trading vendor didn't make it
easy on me. There's virtually no documentation, all links to samples from the
official product pages are broken, they didn't reply to any of my emails
nor phone calls. 

As much as I prefer working/using locally developed products (not only software)
I will never use SpeechLab because its creators don't give a fuck about customers.
Why should I give a fuck about the product then? 


Innoetics' SpeakVolumes
-----------------------

[Innoetics](http://www.innoetics.com) is a Greek company, a spin-off of the
Institute of Language & Speech Processing (ILSP) of ‘Athena’ Research Centre.
Something like BACL I suppose but a bit more commercially oriented. 

Initially I though to use their TTS Batch product to produce audio samples
and asked for a demo. They were very quick in their response and gave me
an FTP download of the software, plus demo activation key and documentation. 
Via email they've sent me tons of info plus pricing and additional proposals.
I didn't even try this demo because it runs on Windows which I don't have.

It turned out Innoetics has built the [SpeakVolumes](http://www.speakvolumes.eu/)
web service which has two modes of operation - on-the-fly audio generation 
using a SOAP based API and offline generation via the web site.
Pricing for SpeakVolumes (per words) was much more competitive than their Windows products
for my use case.

I've created an account at SpeakVolumes and they've bumped up my initial words
credit so I can give it a try. Works like a charm. 

There is only one voice for Bulgarian called Irina
([sample](http://www.innoetics.com/media/tts_irinademo_bg.mp3)).
The voice is very soft, female voice, speaks slower compared to eSpeak
and SpeechLab and sounds very natural. It makes a few mistakes but
from a 250 words sample that I used only a couple were pronounced with
minor mistakes.


The web service generates a Base64 encoded MP3 file and returns it as
response to the client.
[See example Python script here](https://gist.github.com/atodorov/6044724).


The fact that Innoetics involved with me very quickly and provided me with
demo accounts and all sorts of information about their products and the
web API makes SpeakVolumes my choice for Text-To-Speech conversion for Bulgarian.

Ivona
-----

Andre Polykanine from the eSpeak mailing list told me about
[Ivona](http://www.ivona.com/en/). It is a Polish company and seems to 
have been acquired by Amazon now. Andre told me Ivona had planned Bulgarian
support some time ago, but now rejected it for some reason. They didn't
reply to my email though. 



Have you seen other text-to-speech synthesizers for Bulgarian? Let me know
what are they and if you have tried them out.


