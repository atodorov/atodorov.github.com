Title: Testing the 8-bit computer Puldin
Headline: a piece of Bulgarian IT history
date: 2016-07-12 14:10
comments: true
Tags: QA, fedora.planet, events
og_image: images/puldin_creators.jpg
twitter_image: images/puldin_creators.jpg

![Puldin creators](/images/puldin_creators.jpg "Puldin creators")

Last weekend I visited [TuxCon](http://tuxcon.mobi) in Plovdiv and
was very happy to meet and talk to some of the creators of the Puldin
computer! On the picture above are (left to right) Dimitar Georgiev
- wrote the text editor, Ivo Nenov - BIOS, DOS and core OS developer,
Nedyalko Todorov - director of the vendor company and Orlin Shopov -
BIOS, DOS, compiler and core OS developer.


Puldin is 100% pure Bulgarian development, while the “Pravetz” brand
was copy of Apple ][ (Pravetz 8A, 8C, 8M), Oric (Pravets 8D) and IBM-PC
(Pravetz 16). The Puldin computers were build from scratch both hardware
and software and were produced in Plovdiv in the late 80s and early 90s.
50000 pieces were made, at least 35000 of them have been exported to Russia
and paid for. A typical configuration in a Russian class room consisted of
several Puldin computers and a single Pravetz 16. According to Russian sources
the last usage of these computers was in 2003 serving as Linux terminals
and being maintained without any support from the vendor
(b/c it ceased to exist).

![Puldin 601](/images/puldin601.jpg "Puldin 601")

One of the main objectives of Puldin was full compatibility with IBM-PC.
At the time IBM had been releasing extensive documentation about how their
software and hardware works which has been used by Puldin's creators as
their software specs. Despite IBM-PC using faster CPU the Puldin 601 had
a comparable performance due to aggressive software and compiler optimizations.

Testing wise the guys used to compare Puldin's functionality with that of IBM-PC.
It was a hard requirement to have full compatibility on the file storage layer,
that means floppy disks written on Puldin had to be readable on IBM-PC and vice
versa. Same goes for programs compiled on Puldin - they had to execute on IBM-PC.

Everything of course had been tested manually and on top of that all the software
had to be burned to ROM before you can do anything with it. As you can imagine the
testing process had been quite slow and painful compared to today's standards.
I've asked the guys if they'd happened to find a bug in IBM-PC which wasn't present
in their code but they couldn't remember.

What was interesting for me on the hardware side was the fact that you can plug
the computer directly to a cheap TV set and that it's been one of the first computers
which could operate on 12V DC, powered directly from a car battery.

![Pravetz 16](/images/pravetz16.jpg "Pravetz 16")

There was also a fully functional Pravetz 16 with an additional VGA port to
connect it to the LCD monitor as well as a SD card reader wired to function as a
floppy disk reader (the small black dot behind the joystick).


For those who missed it (and understand Bulgarian) I have a
[video recording on YouTube](https://www.youtube.com/watch?v=uFGnrqa2RSY&list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db&index=1).
For more info about the history and the hardware please check-out
[Olimex post on Puldin](https://olimex.wordpress.com/2015/01/12/retro-computer-puldin-the-only-bulgarian-8-bit-computer-developed-from-scratch/)
(in English). For more info on Puldin and Pravetz please visit
[pyldin.info](http://pyldin.info) (in Russian) and
[pravetz8.com](http://pravetz8.com) (in Bulgarian)
using Google translate if need be.
