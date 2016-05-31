Title: Capybara's find().click doesn't always fire onClick
Headline: and using statistical approach to testing
date: 2016-05-31 14:01
comments: true
Tags: QA, Ruby
twitter_image: images/capybara-20clipart-hamster3.png
og_image: images/capybara-20clipart-hamster3.png

Recently I've observed a strange behavior in one of the test suites I'm
working with - a test which submits a web form appeared to fail at a rate
between 10% and 30%. This immediately made me think there is some kind of
race-condition but it turned out that Capybara's `find().click` method
doesn't always fire the onClick event in the browser!

The test suite uses Capybara, Poltergeist and PhantomJS. The element we
click on is an image, coupled to a hidden check-box underneath. When the image
is clicked onClick is fired and the check-box is updated accordingly. In the
failed cases the underlying check-box wasn't updated!
Searching the web reveals a similar problem described by
[Alex Okolish](http://aokolish.me/blog/2012/01/22/testing-hover-events-with-capybara/)
so we've tried his solution:

    :::ruby
    div.find('.replacement', visible: true).trigger(:click)

How to Test
-----------

The failure behavior being somewhat flaky I've opted for running the
test multiple times and see what happens when it fails. Initially I've
executed the test in batches of 10 and 20 repetitions to get a feeling
of how often does it fail before proceeding with debugging. Debugging
was done by logging variables and state on the console and repeating
multiple times. Once a possible solution was
proposed we've run the tests in batches of 100 repetitions and counted
how often they failed.

At the end, when Alex's solution was discovered we've repeated the
testing around 1000 times just to make sure it works reliably.
So far this has been working without issues!

I've spent around a week working on this together with a co-worker
and we didn't really want to spend more time trying to figure out
what was going wrong with our tools. Once we saw that `trigger` does
the job we didn't continue debugging Capybara or PhantomJS.

