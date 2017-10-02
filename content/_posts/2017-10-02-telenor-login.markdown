Title: More tests for login forms
Headline: with examples from Telenor & Kiwi TCMS
date: 2017-10-02 15:06
comments: true
Tags: fedora.planet, QA
og_image: images/telenor_login.png
twitter_image: images/telenor_login.png


!["Telenor's login form"](/images/telenor_login.png "Telenor's login form")

By now I probably have documented more test cases for login forms than anyone
else. You can check out my previous posts on the topic
[here]({filename}2016-04-12-hiring-qa-login-form.markdown) and
[here]({filename}2017-06-14-vmware-login-form.markdown). I give you a few more
examples.

Test 01 and 02:
First of all let's start by saying that a "Remember me" checkbox should actually
remember the user and login them automatically on the next visit if checked. The
other way around if not checked. I don't think this has been mentioned previously!


Test 03:
When there is a "Remember me" checkbox it should be selectable both with the mouse
and the keyboard. On my.telenor.bg the checkbox changes its image only when
clicked with the mouse. Also clicking the login button with Space doesn't work!

Interestingly enough when I don't select "Remember me" at all and close then
revisit the page I am still able to access the internal pages of my account!
At this point I'm not quite sure what this checkbox does!


Test 04:
Testing two factor authentication. I had the case where GitHub SMS didn't
arrive for over 24 hrs and I wasn't able to login. After requesting a new code
you can see the UI updating but I didn't receive another message. In this particular
case I received only one message with an already invalid code. So test for:

- how long does it take for the codes to expire
- is there a visual feedback indicating how many codes have been requested
- do latest code invalidates all the previous ones or all that have been unused
  still work
- what happens if I'm already logged in and somebody tries to access my account
  requesting additional codes which may or may not invalidate my login session?


Test 05:
Check that confirmation codes, links, etc will actually expire after their
configured time. Kiwi TCMS had this problem which has been fixed in
[version 3.32](https://github.com/kiwitcms/Kiwi/commit/92162112bf2214b8eacf37ba3a796414b129a700#diff-353aa238f7ee459b1236e2a21f1142ba).

Test 06:
Is this a social-network-login only site? Then which of my profiles did I use?
Check that there is a working
[social auth provider reminder]({filename}2013-03-14-django-social-auth-tip-reminder-of-login-provider.markdown).

Test 07:
Check that there is an error message visible (e.g. wrong login credentials).
After the redesign Kiwi TCMS had stopped displaying this message and instead
presents the user with the login form again!


Also checkout these
[testing challenges](http://testingchallenges.thetestingmap.org/index.php)
by Claudiu Draghia where you can see many cases related to input field
validation! For example empty field, value too long, special characters in field, etc.
All of these can lead to issues depending on how login is implemented.


Thanks for reading and happy testing!
