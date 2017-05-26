Title: Learn Python &amp; Selenium Automation in 8 weeks
Headline: training for manual testers
date: 2017-05-27 00:36
comments: true
Tags: QA, fedora.planet
og_image: images/selenium_python.jpg
twitter_image: images/selenium_python.jpg

Couple of months ago I conducted a practical,
instructor lead training in Python and Selenium automation for
manual testers. You can find the materials at
[GitHub](https://github.com/atodorov/qa-automation-python-selenium-101).

The training consists of several basic modules and practical homework
assignments. The modules explain

1. The basic structure of a Python program and functions
2. Commonly used data types
3. If statements and (for) loops
4. Classes and objects
5. The Python unit testing framework and its assertions
6. High-level introduction to Selenium with Python
7. High-level introduction to the Page Objects design pattern
8. Writing automated tests for real world scenarios
   without any help from the instructor.

Every module is intended to be taken in the course of 1 week and begins with
links to preparatory materials and lots of reading. Then I help the students
understand the basics and explain with more examples, often writing code as
we go along. At the end there is the homework assignment for which I expect
a solution presented by the end of the week so I can comment and code-review it.

All assignments which require the student to implement functionality, not tests,
are paired with a test suite, which the student should use to validate their
solution.

What worked well
----------------

Despite everything I've written below I had 2 students (from a group of 8)
which showed very good progress. One of them was the absolute star, taking
active participation in every class and doing almost all homework assignments
on time, pretty much without errors. I think she'd had some previous training
or experience though.
She was in the USA, training was done remotely via Google Hangouts.

The other student was in Sofia, training was done in person. He is not on the
same level as the US student but is the best from the Bulgarian team. IMO he
lacks a little bit of motivation. He "cheated" a bit on some tasks providing
non-standard, easier solutions and made most of his assignments. After the first
Selenium session he started creating small scripts to extract results from
football sites or as helpers to be applied in the daily job.
The interesting
fact for me was that he created his programs as `unittest.TestCase` classes.
I guess because this was the way he knew how to run them!?!


There were another few students which had had some prior experience with
programming but weren't very active in class so I can't tell how their
careers will progress. If they put some more effort into it I'm sure they
can turn out to have decent programming skills.



What didn't work well
---------------------

Starting from the beginning most students failed to read the preparatory
materials. Some of the students did read a little bit, others didn't read at all.
At the times when they came prepared I had the feeling the sessions progressed
more smoothly. I also had students joining late in the process, which for the
most part didn't participate at all in the training. I'd like to avoid that in
the future if possible.

Sometimes students complained about lack of example code, although
*Dive into Python* includes tons of examples. I've resorted to sending them
the example.py files which I produced during class.

The practical part of the training was mostly myself programming on a big
TV screen in front of everyone else. Several times someone from the students
took my place. There wasn't much active participation on their part and
unfortunately they didn't want to bring personal laptops to the training
(or maybe weren't allowed)! We did have a company provided laptop though.

When practicing functions and arithmetic operations the students struggled
with basic maths like breaking down a number into its digits or vice versa,
working with Fibonacci sequences and the like. In some cases they cheated
by converting to/from strings and then iterating over them. Also some
hard-coded the first few numbers of the Fibonacci sequence and returned
it directly. Maybe an in-place
explanation of the underlying maths would have been helpful but honestly
I was surprised by this. Somebody please explain or give me an advise here!

I am completely missing examples of the `datetime` and `timedelta` classes
which tuned out to be very handy in the practical Selenium tasks and we had
to go over them on the fly.

The OOP assignments went mostly undone, not to mention one of them had
bonus tasks which are easily solved using recursion. I think we could
skip some of the OOP practice (not sure how safe that is) because I really
need classes only for constructing the tests and we don't do anything fancy
there.

Page Object design pattern is also OOP based and I think that went somewhat
well granted that we are only passing values around and performing some actions.
I didn't put constraints nor provided guidance on what the classes should
look like and which methods go where. Maybe I should have made it easier.

Anyway, given that Page Objects is being replaced by Screenplay pattern,
I think we can safely stick to the all-in-one functional based Selenium
tests. Maybe utilize helper functions for repeated tasks (like login).
Indeed this is what I was using last year with Rspec &amp; Capybara!



What students didn't understand
-------------------------------

Right until the end I had people who had troubles understanding function
signatures, function instances and calling/executing a function. Also
returning a value from a function vs. printing the (same) value on screen
or assigning to the same global variable (e.g. FIB_NUMBERS).

In the same category falls using method parameters vs. using global variables
(which happened to have the same value), using the parameters as arguments to
another function inside the body of the current function, using class attributes
(e.g. `self.name`) to store and pass values around vs. local variables in methods
vs. method parameters which have the same names.


I think there was some confusion about lists, dictionaries and tuples but
we did practice mostly with list structures so I don't have enough information.


I have the impression that object oriented programming (classes and instances,
we didn't go into inheritance) are generally confusing to beginners with zero
programming experience. The classical way to explain them is by using some
abstractions like animal -> dog -> a particular dog breed -> a particular pet.
OOP was explained to me in a similar way back in school so these kinds of
abstractions are very natural for me. I have no idea if my explanation sucks or students are having hard time
wrapping their heads around the abstraction. I'd love to hear some feedback
from other instructors on this one.


I think there is some misunderstanding between a class (a definition of behavior)
and an instance/object of this class (something which exists into memory). This
may also explain the difficulty remembering or figuring out what `self` points to
and why do we need to use it inside method bodies.


For `unittest.TestCase` we didn't do lots of practice which is my fault.
The homework assignments request the students to go back to solutions
of previous modules and implement more tests for them. Next time I should
provide a module (possibly with non-obvious bugs) and request to write
a comprehensive test suite for it.

Because of the missing practice there was some confusion/misunderstanding
about the `setUpClass/tearDownClass` and the `setUp/tearDown` methods.
Also add to the mix that the first are `@classmethod` while the later
are not. "To be safe" students always defined both as class methods!

I have since corrected the training materials but we didn't have
good examples (nor practiced) explaining the difference between
`setUpClass` (executed once aka before suite) and `setUp`
(possibly executed multiple times aka before test method).


On the Selenium side I think it is mostly practice which students lack,
not understanding. The entire Selenium framework (any web test framework
for that matter) boils down to

- Load a page
- Find element(s)
- Click or hover (that one was tricky) element
- Get element's attribute value or text
- Wait for the proper page to load (or worst case AJAX calls)

IMO finding the correct element on the page is on-par with waiting
(which also relies on locating elements) and took 80% of the time we spent
working with Selenium.



Thanks for reading and don't forget to comment and give me your feedback!


*Image source: https://www.udemy.com/selenium-webdriver-with-python/*
