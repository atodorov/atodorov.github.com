Title: How To Hire Software Testers, Pt. 3
Headline: How would you test a pen?
date: 2016-06-03 11:15
comments: true
Tags: QA, fedora.planet
og_image: images/fedora/pen.png
twitter_image: images/fedora/pen.png

In previous posts (links below) I have described my process of interviewing
QA candidates. Today I'm quoting an excerpt from the book
[Mission: My IT career](http://it-interviews.com/)(Bulgarian only) by Ivaylo Hristov,
one of [Komfo](http://komfo.com)'s co-founders.

![Fedora pen](/images/fedora/pen.png "Fedora pen")

He writes

    Probably the most important personal trait of a QA engineer is to
    be able to think outside given boundaries and prejudices
    (about software that is). When necessary to be non-conventional and
    apply different approaches to the problems being solved. This will help
    them find defect which nobody else will notice.
    
    Most often errors/mistakes in software development are made due to
    wrong expectations or wrong assumptions. Very often this happens because
    developers hope their software will be used in one particular way
    (as it was designed to) or that a particular set of data will be returned.
    Thus the skill to think outside the box is the most important skill
    we (as employers) are looking to find in a QA candidate. At job interviews
    you can expect to be given tasks and questions which examine those skills.


How would you test a pen?
-------------------------

This is Ivaylo's favorite question for QA candidates. He's looking for
attention to details and knowing when to stop testing. Some of the possible
answers related to core functionality are

* Does the pen write in the correct color
* Does the color fades over time
* Does the pen operate normally at various temperatures? What temperature
  intervals would you choose for testing
* Does the pen operate normally at various atmospheric pressure
* When writing, does the pen leave excessive ink
* When writing, do you get a continuous line or not
* What pressure does the user need to apply in order to write a
  continuous line
* What surfaces can the pen write on? What surfaces would you test
* Are you able to write on a piece of paper if there is something soft underneath
* What is the maximum inclination angle at which the pen is able to write
  without problems
* Does the ink dry fast
* If we spill different liquids onto a sheet of paper, on which we had written
  something, does the ink stay intact or smear
* Can you use pencil rubber to erase the ink? What else would you test
* How long can you write before we run out of ink
* How fat is the ink line

Then Ivaylo gives a few more non-obvious answers

* Verify that all labels on the pen/ink cartridge are correctly spelled
  and how durable they are (try to erase them)
* Strength test - what is the maximum height you can drop the pen from
  without breaking it
* Verify that dimensions are correct
* Test if the pen keeps writing after not being used for some time
  (how long)
* Testing individual pen components under different temperature and
  atmospheric conditions
* Verify that materials used to make the pen are safe, e.g. when you put
  the pen in your mouth

When should you stop ? According to the book there can be between 50 and 100
test cases for a single pen, maybe more. It's not a good sign if you stop at
the first 3!

If you want to know what skills are revealed via these questions please
read my other posts on the topic:

* [The login form question]({filename}2016-04-12-hiring-qa-login-form.markdown)
* [How do you test a Sudoku solver]({filename}2016-04-16-hiring-qa-sudoku.markdown)

Thanks for reading and happy testing!
