Title: How To Hire Software Testers, Pt. 1
Headline: the Login Form question
date: 2016-04-12 12:34
comments: true
Tags: QA, fedora.planet
og_image: images/login_form_wireframe.jpg
twitter_image: images/login_form_wireframe.jpg

Many people have asked me how do I make sure a person who applies for a
QA/software tester position is a good fit ? On the opposite side people
have asked online how do they give correct answers on test related questions
at job interviews. I have two general questions to help me decide if a
person knows about testing and if they are a good fit for the team or not.

![Login form](/images/login_form_wireframe.jpg "Login form")


How do You Test a Login Form
----------------------------

You are given the login form above and the following constraints:

* Log in is possible with username and password or through the social networks;
* After successful registration an email with the following content is sent to the user:

`Helo and welcome to atodorov.org! Click _here_ to confirm your emeil address.`

You have 10 minutes to write down a list of all test cases you can think of!

Behind The Scenes
-----------------

The question looks trivial but isn't as easy to answer as you may think.
If you haven't spent the last 20 years of your life in a cave, chances are
that you will give technically correct answers but this is not the only
thing I'm looking for.

The question is designed to simulate a real-world scenario, where the QA
person is given a piece of software, or requirements document and tasked with
creating a test plan for it. The question is intentionally vague because that's
how real-world works, most often testers don't have all the requirements and
specifications available beforehand.

The time constrain, especially when the interview is performed in person,
simulates work under pressure - get the job done as soon as possible.

While I review the answers I'm trying to figure out how does the person think,
not how much about technology they know. I'm trying to figure out what are their
strong areas and where they need to improve. IMO being able to think as a tester
and having attention to details, being able to easily spot corner cases and
look at the problem from different angles is much more important than
technical knowledge in a particular domain.

As long as a person is suited to think like a tester they can learn to
apply their critical thinking to any software under test and use various
testing techniques to discover or safeguard against problems.

* A person that answers quickly and intuitively is better than a person who
takes a long time to figure out what to test. I can see they are active
thinkers and can work without micro-management and hand-holding.

* A person that goes on and on
describing different test cases is better than one who limits themselves to
the most obvious cases. I can see they have an exploratory passion, which
is the key to finding many bugs and making the software better;

* A person that goes to explore the system in breadth is better than one who
keeps banging on the same test case with more and more variations. I can see
they are noticing the various aspects of the software (e.g. social login,
email confirmation, etc) but also to some extent, not investing all of their
resources (the remaining time to answer) into a single direction. Also in
real-world testing, testing the crap out of something is useful up to a point.
Afterwards we don't really see any significant value from additional testing
efforts.

* A person that is quick to figure out one or two corner cases is better
than a person who can't. This tells me they are thinking about what goes
on under the hood and trying to predict unpredictable behavior - for example
what happens if you try to register with already registered username or email?

* A person that asks questions in order to minimize uncertainty and vagueness
is better than the one who doesn't. In real-world if the tester doesn't know
something they have to ask. Quite often even developers and product managers
don't know the answer. Then how are we developing software if we don't know
what it is supposed to do ?

* If given more time (writing interview), a person that organizes their answers
into steps (1, 2, 3) is a bit better than one who simply throws at you random
answers without context. Similar thought applies to people who write down their
test pre-conditions before writing down scenarios. From this I can see that
the person is well organized and will have no trouble writing detailed test cases,
with pre-conditions, steps to execute and expected results. This is what QAs do.
Also we have the, sometimes tedious, task of organizing all test results into
a test case management system (aka test book) for further reference.

* The question intentionally includes some mistakes. In this example 2 spelling
errors in the email text. Whoever manages to spot them and tell me about it is
better than others who don't spot the errors or assume that's how it is. QAs job
is to always question everything and never blindly trust that the state of the
system is the way it is. Also simple errors like typos can be
[embarrassing]({filename}2016-01-15-tesla-needs-more-qa.markdown) or generate
unnecessary support calls.

* Bravo if you tested not only the outgoing email but also social login. This
shows attention to details, not to mention social is 1/3rd of our example system.
It also shows that QA's job doesn't end with testing
the core, perceived functionality of the system. QA tests everything,
even interactions with external systems if that is necessary.


What Are The Correct Answers
-----------------------------

I will document some of the possible answers as I recall them from memory.
I will update the list with other interesting answers given by students who
applied to my
[QA and Automation 101](https://github.com/HackBulgaria/QA-and-Automation-101)
course, answering this very same question.

* Test if users can register using valid username, email and password;
* Test if SUT gives an error message when email or password (or username)
format doesn't follow a particular format (e.g. no special symbols);
* After registration, test that the user can login successfully;
* Depending on requirements test if the user can login before they have
confirmed their email address;
* Test that upon registration a confirmation email is actually sent;
* Spell-check the email text;
* Test if the _click here_ piece of text is a hyperlink;
* Verify that when clicked, the hyperlink successfully confirmed email/activates the account
(depending on what confirmed/activated means per requirements);
* Test what happens if the link is clicked a second time;
* Test what happens if the link is clicked after 24 or 48 hrs;
* Test that the social network icons, actually link to the desired SN and
not someplace else;
* Test if new user accounts can be created via all specified social networks;
* Test what happens if there is an existing user, who registered with a password
and they (or somebody else) tries to register via social with an account that has
the same email address, aka account hijacking;
* Same as previous test but try to register a new user, using email address that
was previously used with social login;
* Test what happens if users forget their password - intentionally we don't have
the '[] Forgot my password' checkbox. This is both usability feature and missing
requirements;
* Test for simple SQL injections like
[Bobby Tables](http://php.net/manual/en/images/fa7c5b5f326e3c4a6cc9db19e7edbaf0-xkcd-bobby-tables.png).
*btw I was given this image as an answer which scored high on the geek-o-meter*;
* Test for XSS - [Tweetdeck didn't](https://twitter.com/dergeruhn/status/476764918763749376);
* Test if non-activated/non-confirmed usernames expire after some time and can be used again;
* Test of fields tab order - something I haven't done in 15 or more years
but still valid and I've seen sites getting it wrong quite often;
* When trying to login test what happens when username/password is wrong or empty;
* Test if email is required for login - this isn't clear from the requirements
so it is a valid answer. Better answer is to clarify that;
* Test if username/email or password is case sensitive. Valid test and indeed I
recently saw a problem where upon registration users entered their emails using
some capital letters but they were lower-cased before saving to the DB. Later this
broke a piece of code which forgot to apply the lowercase on the input data. The code
was handling account reactivation;
* Test if the password field shows the actual password or not. I haven't seen this
in person but I'm certain there is some site which maybe used CSS and nice images
instead of the default ugly password field and that didn't work on all browsers;
* Test if you can copy&paste the masked password, probably trying to steal somebody
else's password. Last time I saw this was on early Windows 95 with the modem connection
dialog. Very briefly it allowed you to copy the text from the field and paste it into
Notepad to reveal the actual password;
* If we're on mobile (intentionally not specified) test for buffer overflows;
Actually test that everywhere and see what happens;
* Test if the social network buttons use the same action verb. In the example
we have *Log in*, *Connect* and *Sign in*. This is sort of usability testing
and helping have a unified look and feel of the product;
* Test which of the *Log in* and *Sign up* tabs is active at the moment.
The example is intentionally left to look like a wireframe but it is important
for the user to easily tell where they are. Otherwise they'll call support or
even worse, simply give up on us;
* Test if all static files (images) will load if they are deployed onto CDN.
Not surprisingly I've seen [this bug](https://github.com/Nitrate/Nitrate/pull/80);
* In case we have a "[] Remember me" checkbox, test if it actually remembers
the user credentials. Yesterday I saw this same functionality not working on
a specialized desktop app in the corner case where you supply a different
connection endpoint (server) instead of the ones already provided. The user
defined value is accepted but not saved automatically;
* Test if the "Remember me" functionality actually saves your last credentials
or only the first ones you provided. There is a similar bug in 
[Grajdanite](https://play.google.com/store/apps/details?id=com.xevica.grajdanite),
where once you enter a wrong email, it is remembered and every time the form is
pre-filled with the previous value (which is wrong). I'm yet to report it though;
* Cross-browser testing - hmm, login and registration should work on all browsers
you say. It's not browser dependent, is it? Well yeah, login isn't browser dependent
unless we did something stupid like pre-handling the form submit via non-cross-platform
JavaScript or even
[accidentally doing so](https://github.com/gilsondev/pelican-clean-blog/pull/6);
* Test with Unicode characters, especially non Latin ones. It's been many years
since we had Unicode but quite a few apps haven't learned how to deal with Unicode
text properly.


I'm certain there are more answers and I will update the list as I figure them out.
You can always post in the comments and tell me something I've missed.

How to Pass The Job Interview
-----------------------------

This is a question I often see on [Quora](https://www.quora.com/profile/Alexander-Todorov).
*I have a job interview tomorrow. How do I test a login form (or whatever) ?*

If this section is what you're after I suspect you are a junior or wanna-be
software tester. As you've seen the interviewer isn't really interested in what you know already,
at least not as much. We're interested in getting to know how you
think in the course of 30-60 minutes.

If you ever find yourself being asked a similar question just start thinking and
answering and don't stop. Vocalize your thoughts, even if you don't know what will
happen when testing a certain condition. Then keep going on and on. Look at the problem
from all angles, explain how you'd test various aspects and features of the SUT.
Then move on to the next bit. Always think about what you may have forgotten and
revisit your answers - this is what real QAs do - learn from mistakes.
Ask questions, don't ever assume anything. If something is unclear ask to be
clarified. For example I've seen a person who doesn't use social networks and
didn't know how social login/registration worked. They did good by asking me to
describe how that works.

Your goal is to make the interviewer ask you to stop answering. Then tell them
a few more answers.

However beware of cheating. You may cheat a little bit by
saying you will test this and that or design scenarios you have no clue about.
Maybe you read them in my blog or elsewhere. If the interviewer knows their job
(which they should) they will instantly ask you another question to verify what
you say. Don't forget the interviewer is probably an experienced tester and validating
assumptions is what they do every day.

For example, if you told me something about security testing or SQL injection
or XSS I will ask you to explain that in more details. If you forgot to mention,
one of them, say XSS but only heard about SQL injection I will ask you about the
other one. This will immediately tell me if you have a clue what you are talking
about.



Feel free to send me suggestions and answers in the comments below. In the next few
days I will blog about my other question *How do you test a Sudoku solving function*.

Thanks for reading and happy testing!
