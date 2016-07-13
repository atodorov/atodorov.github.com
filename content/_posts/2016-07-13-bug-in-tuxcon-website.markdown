Title: Bug in TuxCon Website
Headline: due to wrong initialization values
date: 2016-07-13 14:10
comments: true
Tags: QA
og_image: images/bugs/tuxcon_bug.png
twitter_image: images/bugs/tuxcon_bug.png

![TuxCon bug](/images/bugs/tuxcon_bug.png "TuxCon bug")

Here comes July 9th 2016 and the start of [TuxCon](http://tuxcon.mobi) ...
with a bug on their website! The image above is taken during the first
talk of the conference. Obviously the count down timer is completely off.

In
[init.js:100](https://github.com/TuxCon/tuxcon-website/blob/master/js/init.js#L100)
there is this piece of code

    :::javascript
    var finalDate = '2016/07/09';
    
    $('div#counter').countdown(finalDate)
    .on('update.countdown', function(event) {
        $(this).html(event.strftime('<span>%D <em>days</em></span>' +
                                    '<span>%H <em>hours</em></span>' +
                                    '<span>%M <em>minutes</em></span>' +
                                    '<span>%S <em>seconds</em></span>'));
    });

It counts backwards and updates the HTML until `finalDate` is reached. Then
the HTML is no longer updated and the default values are shown, which in
this case are non zero. A simple
[patch](https://github.com/TuxCon/tuxcon-website/pull/1) fixes the problem.

Initialize your variables properly and happy testing!
