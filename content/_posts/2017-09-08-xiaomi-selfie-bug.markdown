Title: Xiaomi's selfie bug
Headline: front camera mirroring images
date: 2017-09-08 09:50
comments: true
Tags: fedora.planet, QA
og_image: images/unicorn_mirrored.jpeg
twitter_image: images/unicorn_mirrored.jpeg

Recently I've been exploring the user interface of a Xiaomi Redmi Note 4X
phone and noticed a peculiar bug, adding to my collection of
[obscure phone bugs]({filename}2013-03-19-bug-in-nokia-software-shows-wrong-caller-id.markdown).
Sometimes when taking selfies the images
will not be saved in the correct orientation. Instead they will be saved as
if looking in the mirror and this is a bug!

!["Samsung S5 front screen"](/images/samsung_s5_front_screen.jpg "Samsung S5 front screen")

While taking the selfie the display correctly acts as a mirror, see my personal
Samsung S5 (black) and the Xiaomi device (white).

!["Xiaomi front screen"](/images/xiaomi_front_screen.jpg "Xiaomi front screen")

However when the image is saved and then viewed through the gallery application
there is a difference. The image below is taken with the Xiaomi device and there
have been no effects added to it except scaling and cropping. As you can see
the letters on the cereal box are mirrored!

!["Xiaomi mirrored image"](/images/xiaomi_adi_mirrored.jpeg "Xiaomi mirrored image")

The symptoms of the bug are not quite clear as of yet. I've managed to reproduce at
around 50% rate so far. I've tried taking pictures during the day in direct sunlight
and in the shade, also in the evening under bad artificial lighting.
Taking photo of a child's face and then child plus varying number of adults.
Then photo of only 1 or more adults, heck I even made a picture of myself. I though that
lighting or the number of faces and their age have something to do with this bug
but so far I'm not getting consistent results. Sometimes the images turn out OK
and other times they don't regardless of what I take a picture of.

I also took a picture of the same cereal box, under the same conditions as above but
not capturing the child's face and the image came out not mirrored. The only clue
that seems to hold true so far is that you need to have people's faces in the picture
for this bug to reproduce but that isn't an edge case when taking selfies, right?

I've also compared the results with my Samsung S5 (Android version 6.0.1) and BlackBerry Z10 devices
and both work as expected: while taking the picture the display acts as a mirror
but when viewing the saved image it appears in normal orientation. On S5 there is
also a clearly visible "Processing" progress bar while the picture is being saved!

For reference the system information is below:

    :::
    Model number: Redmi Note 4X
    Android version: 6.0 MRA58K
    Android security patch level: 2017-03-01
    Kernel version: 3.18.22+


I'd love if somebody
from Xiaomi's engineering department looks into this and sends me a root cause analysis
of the problem.

Thanks for reading and happy testing! Oh and btw this is my breakfast, not hers!
