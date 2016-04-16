Title: How To Hire Software Testers, Pt. 2
Headline: testing Sudoku solver
date: 2016-04-16 10:34
comments: true
Tags: QA, fedora.planet
og_image: images/sudoku.png
twitter_image: images/sudoku.png

In my
[previous post]({filename}2016-04-12-hiring-qa-login-form.markdown) I have
described the process I follow when interviewing candidates for a QA position.
The first question is designed to expose the applicant's way of thinking.
My second question is designed to examine their technical understanding
and to a lesser extent their way of thinking.

![Sudoku](/images/sudoku.png "Sudoku")


How do You Test a Sudoku Solving Function
-----------------------------------------

You have implementation of a sudoku solver function with the following pseudocode:

```
func Sudoku(Array[2]) {
    ...
    return Array[2]
}
```

- The function solves a sudoku puzzle;
- Input parameter is a two-dimensional array with the known numbers (from 1 to 9) in the Sudoku grid;
- The output is a two-dimensional array with the numbers from the solved puzzle.

You have 10 minutes to write down a list of all test cases you can think of!

Behind The Scenes
-----------------

One set of possible tests is to examine the input and figure out if the
function has been passed valid data.
In the real-world programs interact with each other, they are not alone.
Sometimes it happens that a valid output from one program isn't a
valid input for the next one. Also we have malicious users who will try to
break the program.

If a person manages to test for this case then
I know they have a bit more clue about how software is used in the real-world.
This also touches a bit on white-box testing, where the tester has full info
about the software under test. In this example the implementation is
intentionally left blank.


OTOH I've seen answers where the applicant blindly assumes that the input
is 1-9, because the spec says so, and excludes the entire input testing from
their scope. I classify this answer as immediate failure, because a tester should
never assume anything and test to verify their initial conditions are indeed
as stated in the documentation.


Another set of possible tests is to verify the correct work of the function.
That is to verify the proposed Sudoku solution is indeed following the rules
of the game. This is what we usually refer to black-box testing. The tester
doesn't know how the SUT works internally, they only know the input data and
the expected output. 

If a person fails to describe at least one such test case
they have essentially failed the question. What is the point of a SUT which
doesn't crash (suppose that all previous tests passed) but doesn't
produce the desired correct result ?


Then there are test cases related to the environment in which this Sudoku
solver function operates. This is where I examine the creativity of the person,
their familiarity with other platforms and to some extent their thinking out of
the box. Is the Sudoku solver iterative or recursive ? What if we're on an
embedded system and recursion is too heavy for it ? How much power does the
function require, how fast it works, etc.

A person that provides at least one answer in this category has bonus points
over the others who didn't. IMO it is very important for a tester to have
experience with various platforms and environments because this helps them
see edge cases which others will not be able to see. I also consider a strong
plus if the person shows they can operate outside their comfort zone.


If we have time I may ask the applicant to write the tests using a programming
language they know. This is to verify their coding and automation skills.

OTOH having the tests as code will show me how much the person knows about testing
vs. coding. I've seen solutions where people write a for loop, looping over all
numbers from 1 to 100 and testing if they are a valid input to `Sudoku()`.
Obviously this is pointless and they failed the test.


Last but not least, the question asks for testing a particular Sudoku solver
implementation. I expect the answers to be designed around the given function.
However I've seen answers designed around a
[Sudoku solver website](http://sudoku-solutions.com/) or described as
intermediate states in an interactive Sudoku game (e.g. wrong answers shown in red).
I consider these invalid because the question is to test a particular
given function, not anything Sudoku related. If you do this in real-life that
means you are not testing the SUT directly but maybe touching it indirectly
(at best). This is not what a QA job is about.



What Are The Correct Answers
-----------------------------

Here are some of the possible tests.

* Test with single dimensional input array - we expect an error;
* Test with 3 dimensional input array - we expect an error;
* Then proceed testing with 2 dimensional array;
* Test with number less than 1 (usually 0) - expect error;
* Test with number greater than 9 (usually 10) - expect error;
* Test how the function handles non-numerical data - chars & symbols
(essentially the same thing for our function);
* Test with strings which actually represent a number, e.g. "1";
* Test with floating point numbers, e.g. 1.0, 2.0, 3.0 - may or may not
work depending on how the code is written;
* If floating point numbers are accepted, then test with a different locale.
Is "1.0" the same as "1,0";
* Test with `null`, `nil`, `None` (whatever the language supports) -
this should be a valid value for unknown numbers and not cause a crash;
* Test if the function validates that the provided input follows the
Sudoku rules by passing it duplicate numbers in one row, column or
square. It should produce an error;
* Test if the input data contains the minimum number of givens, 17
for a general Sudoku, so that a solution can be found. Otherwise the function
may go into an
[endless loop]({filename}2015-01-05-endless-loop-bug-candy-crush-saga-level-80.markdown);
* Verify the proposed solution conforms to Sudoku rules;
* Test with a fully solved puzzle as input - output should be exactly the same;
* If on mobile, measure battery consumption for 1 minute of operation. I've
seen a game which uses 1% battery power for 1 minute of game play;
* Test for buffer overflows;
* Test for speed of execution (performance);
* Test performance on single and multiple (core) CPUs - depending on the
language and how the function is written this may produce a difference or not;

I'm sure I'm missing something so please use the comments below to tell me your suggestions.

Thanks for reading and happy testing!
