Title: Mutation Testing vs. Coverage
Headline: a practical experiment to find out which one is better
date: 2016-12-27 11:48
comments: true
Tags: QA, fedora.planet
og_image: images/ninja_turtles.jpg
twitter_image: images/ninja_turtles.jpg

At GTAC 2015 Laura Inozemtseva made a lightning talk titled
[Coverage is Not Strongly Correlated with Test Suite Effectiveness](https://www.youtube.com/watch?v=sAfROROGujU&list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db&index=47)
which is the single event that got me hooked up with mutation testing.
This year, at GTAC 2016, Rahul Gopinath made a counter argument
with his lightning talk
[Code Coverage is a Strong Predictor of Test Suite Effectiveness](https://www.youtube.com/watch?v=NKEptA3KP08&list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db&index=1).
So which one is better ? I urge you to watch both talks and take notes before
reading about my practical experiment and other opinions on the topic!

**DISCLAIMER:** I'm a heavy contributor to Cosmic-Ray, the mutation testing tool for Python
so my view is biased!


Both Laura and Rahul (you will too) agree that a test suite effectiveness depends
on the strength of its oracles. In other words the assertions you make in your tests.
This is what makes a test suite good and determines its ability to detect bugs when
present. I've decided to use [pelican-ab](https://github.com/MrSenko/pelican-ab) as
a practical example. pelican-ab is a plugin for Pelican, the static site generator
for Python. It allows you to generate A/B experiments by writing out the content
into different directories and adjusting URL paths based on the experiment name.

Can 100% code coverage detect bugs
----------------------------------

Absolutely **NOT**! In version 0.2.1,
[commit ef1e211](https://github.com/MrSenko/pelican-ab/commit/ef1e2117ad8ffa5b9fa8470d32d54a36ccb140bb),
pelican-ab had the following bug:

    Given: Pelican's DELETE_OUTPUT_DIRECTORY is set to True (which it is by default)
    When: we generate several experiments using the commands:
        AB_EXPERIMENT="control" make regenerate
        AB_EXPERIMENT="123" make regenerate
        AB_EXPERIMENT="xy" make regenerate
        make publish
    Actual result: only the "xy" experiment (the last one) would be published online.
    And: all of the other contents will be deleted.
    
    Expected result: content from all experiments will be available under the output directory.

This is because before each invocation Pelican deletes the output directory and
re-creates the entire content structure. The bug was not caught regardless of
having 100% line + branch coverage. See
[Build #10](https://travis-ci.org/MrSenko/pelican-ab/builds/129514715) for more
info.

Can 100% mutation coverage detect bugs
--------------------------------------

So I've branched off since commit ef1e211 into the
[mutation_testing_vs_coverage_experiment branch](https://github.com/MrSenko/pelican-ab/commits/mutation_testing_vs_coverage_experiment)
(requires Pelican==3.6.3).

After initial execution of Cosmic Ray I have 2 mutants left:

    :::diff
    $ cosmic-ray run --baseline=10 --test-runner=unittest example.json pelican_ab -- tests/
    $ cosmic-ray report example.json 
    job ID 29:Outcome.SURVIVED:pelican_ab
    command: cosmic-ray worker pelican_ab mutate_comparison_operator 3 unittest -- tests/
    --- mutation diff ---
    --- a/home/senko/pelican-ab/pelican_ab/__init__.py
    +++ b/home/senko/pelican-ab/pelican_ab/__init__.py
    @@ -14,7 +14,7 @@
         def __init__(self, output_path, settings=None):
             super(self.__class__, self).__init__(output_path, settings)
             experiment = os.environ.get(jinja_ab._ENV, jinja_ab._ENV_DEFAULT)
    -        if (experiment != jinja_ab._ENV_DEFAULT):
    +        if (experiment > jinja_ab._ENV_DEFAULT):
                 self.output_path = os.path.join(self.output_path, experiment)
                 Content.url = property((lambda s: ((experiment + '/') + _orig_content_url.fget(s))))
                 URLWrapper.url = property((lambda s: ((experiment + '/') + _orig_urlwrapper_url.fget(s))))
    
    job ID 33:Outcome.SURVIVED:pelican_ab
    command: cosmic-ray worker pelican_ab mutate_comparison_operator 7 unittest -- tests/
    --- mutation diff ---
    --- a/home/senko/pelican-ab/pelican_ab/__init__.py
    +++ b/home/senko/pelican-ab/pelican_ab/__init__.py
    @@ -14,7 +14,7 @@
         def __init__(self, output_path, settings=None):
             super(self.__class__, self).__init__(output_path, settings)
             experiment = os.environ.get(jinja_ab._ENV, jinja_ab._ENV_DEFAULT)
    -        if (experiment != jinja_ab._ENV_DEFAULT):
    +        if (experiment not in jinja_ab._ENV_DEFAULT):
                 self.output_path = os.path.join(self.output_path, experiment)
                 Content.url = property((lambda s: ((experiment + '/') + _orig_content_url.fget(s))))
                 URLWrapper.url = property((lambda s: ((experiment + '/') + _orig_urlwrapper_url.fget(s))))
    
    total jobs: 33
    complete: 33 (100.00%)
    survival rate: 6.06%

The last one, job 33 is equivalent mutation. The first one, job 29 is killed by the test
added in
[commit b8bff85](https://github.com/MrSenko/pelican-ab/commit/b8bff85eeca6c18fbf62cac55fd1a0d64295c43c).
For all practical purposes we now have 100% code coverage and 100% mutation coverage.
The bug described above still exists thought.

How can we detect the bug
-------------------------

The bug isn't detected by any test because
we don't have tests designed to perform and validate the exact same steps that a
physical person will execute when using pelican-ab. Such test is added in
[commit ca85bd0](https://github.com/MrSenko/pelican-ab/commit/ca85bd042d783f2f6551ae17f16b29aa3750711b)
and you can see that it causes
[Build #22](https://travis-ci.org/MrSenko/pelican-ab/builds/186510356) to fail.

Experiment with setting `DELETE_OUTPUT_DIRECTORY=False` in `tests/pelicanconf.py` and
the test will PASS!

Is pelican-ab bug free
----------------------

Not of course. Even after 100% code and mutation coverage and after manually constructing
a test which mimics user behavior there is at least one more bug present. There
is a pylint `bad-super-call` error, fixed in
[commit 193e3db](https://github.com/MrSenko/pelican-ab/commit/193e3db9e7d021e11b54f54ac8b8718651c633c8).
For more information about the error see
[this blog post](http://mrsenko.com/blog/atodorov/2016/09/14/beware-of-recursion-loop-when-using-super/).

Other bugs found
----------------

During my humble experience with mutation testing so far I've added
[quite a few new tests](https://github.com/rhinstaller/pykickstart/pulls/atodorov)
and discovered two bugs which went unnoticed for years. The first one is
constructor parameter not passed to parent constructor,
see
[PR#96, pykickstart/commands/authconfig.py](https://github.com/rhinstaller/pykickstart/pull/96/files#diff-f4294048719aeac4da7a86eee0fbdfd3)

    :::diff
         def __init__(self, writePriority=0, *args, **kwargs):
    -        KickstartCommand.__init__(self, *args, **kwargs)
    +        KickstartCommand.__init__(self, writePriority, *args, **kwargs)
             self.authconfig = kwargs.get("authconfig", "")

The second bug is parameter being passed to parent class constructor,
but the parent class doesn't care about this parameter. For example
[PR#96, pykickstart/commands/driverdisk.py](https://github.com/rhinstaller/pykickstart/pull/96/files#diff-7d2833450b6e1c9a94eb90e7f171ff52)

    :::diff
    -    def __init__(self, writePriority=0, *args, **kwargs):
    -        BaseData.__init__(self, writePriority, *args, **kwargs)
    +    def __init__(self, *args, **kwargs):
    +        BaseData.__init__(self, *args, **kwargs)

Also note that pykickstart has nearly 100% test coverage as a whole
and the affected files were 100% covered as well.

The bugs above don't seem like a big deal and when considered out of context
are relatively minor. However pykickstart's biggest client is anaconda, the Fedora
and Red Hat Enterprise Linux installation program. Anaconda uses pykickstart to
parse and generate text files (called kickstart files) which contain information
for driving the installation in a fully automated manner. This is used by everyone
who installs Linux on a large scale and is pretty important functionality!

`writePriority` controls the order of which individual commands are written to file
at the end of the installation. In rare cases the order of commands may depend
on each other. Now imagine the bugs above produce a disordered kickstart file,
which a system administrator thinks should work but it doesn't. It may be the case
this administrator is trying to provision hundreds of Linux systems to bootstrap
a new data center or maybe performing disaster recovery. You get the scale of
the problem now, don't you?

To be honest I've seen bugs of this nature but not in the last several years.

This is all to say a minor change like this may have
an unexpectedly big impact somewhere down the line.


Conclusion
----------

With respect to the above findings and my bias I'll say the following:

* Neither 100% coverage, nor 100% mutation coverage are a silver bullet against bugs;
* 100% mutation coverage appears to be better than 100% code coverage in practice;
* Mutation testing clearly shows out pieces of code which need refactoring
  which in turn minimizes the number of possible mutations;
* Mutation testing causes you to write more asserts and construct more detailed tests
  which is always a good thing when testing software;
* You can't replace humans designing test cases just yet but can give them tools
  to allow them to write more and better tests;
* You should not rely on a single tool (or two of them) because tools are only
  able to find bugs they were designed for!


Bonus: What others think
-------------------------

As a bonus to this article let me share a transcript from the
[mutation-testing.slack.com](https://mutation-testing.slack.com) community:

    atodorov 2:28 PM
    Hello everyone, I'd like to kick-off a discussion / interested in what you think about
    Rahul Gopinath's talk at GTAC this year. What he argues is that test coverage is still
    the best metric for how good a test suite is and that mutation coverage doesn't add much
    additional value. His talk is basically the opposite of what @lminozem presented last year
    at GTAC. Obviously the community here and especially tools authors will have an opinion on
    these two presentations.
    
    tjchambers 12:37 AM
    @atodorov I have had the "pleasure" of working on a couple projects lately that illustrate
    why LOC test coverage is a misnomer. I am a **strong** proponent of mutation testing so will
    declare my bias.
    
    The projects I have worked on have had a mix of test coverage - one about 50% and
    another > 90%.
    
    In both cases however there was a significant difference IMO relative to mutation coverage
    (which I have more faith in as representative of true tested code).
    
    Critical factors I see when I look at the difference:
    
    - Line length: in both projects the line lengths FAR exceeded visible line lengths that are
    "acceptable". Many LONGER lines had inline conditionals at the end, or had ternary operators
    and therefore were in fact only 50% or not at all covered, but were "traversed"
    
    - Code Conviction (my term): Most of the code in these projects (Rails applications) had
    significant Hash references all of which were declared in "traditional" format hhh[:symbol].
    So it was nearly impossible for the code in execution to confirm the expectation of the
    existence of a hash entry as would be the case with stronger code such as "hhh.fetch(:symbol)"
    
    - Instance variables abound: As with most of Rails code the number of instance variables
    in a controller are extreme. This pattern of reference leaked into all other code as well,
    making it nearly impossible with the complex code flow to ascertain proper reference
    patterns that ensured the use of the instance variables, so there were numerous cases
    of instance variable typos that went unnoticed for years. (edited)
    
    - .save and .update: yes again a Rails issue, but use of these "weak" operations showed again
    that although they were traversed, in many cases those method references could be removed
    during mutation and the tests would still pass - a clear indication that save or update was
    silently failing.
    
    I could go on and on, but the mere traversal of a line of code in Ruby is far from an indication
    of anything more than it may be "typed in correctly".
    
    @atodorov Hope that helps.
    
    LOC test coverage is a place to begin - NOT a place to end.
    
    atodorov 1:01 AM
    @tjchambers: thanks for your answer. It's too late for me here to read it carefully but
    I'll do it tomorrow and ping you back
    
    dkubb 1:13 AM
    As a practice mutation testing is less widely used. The tooling is still maturing. Depending on your
    language and environment you might have widely different experiences with mutation testing
    
    I have not watched the video, but it is conceivable that someone could try out mutation testing tools
    for their language and conclude it doesn’t add very much
    
    mbj 1:14 AM
    Yeah, I recall talking with @lminozem here and we identified that the tools she used likely
    show high rates of false positives / false coverage (as the tools likely do not protect against
    certain types of integration errors)
    
    dkubb 1:15 AM
    IME, having done TDD for about 15+ years or so, and mutation testing for about 6 years, I think
    when it is done well it can be far superior to using line coverage as a measurement of test quality
    
    mbj 1:16 AM
    Any talk pro/against mutation testing must, as the tool basis is not very homogeneous, show a non consistent result.
    
    dkubb 1:16 AM
    Like @tjchambers says though, if you have really poor line coverage you’re not going to
    get as much of a benefit from mutation testing, since it’s going to be telling you what
    you already know — that your project is poorly tested and lots of code is never exercised
    
    mbj 1:19 AM
    Thats a good and likely the core point. I consider that mutation testing only makes sense
    when aiming for 100% (and this is to my experience not impractical).
    
    tjchambers 1:20 AM
    I don't discount the fact that tool quality in any endeavor can bring pro/con judgements
    based on particular outcomes
    
    dkubb 1:20 AM
    What is really interesting for people is to get to 100% line coverage, and then try mutation
    testing. You think you’ve done a good job, but I guarantee mutation testing will find dozens
    if not hundreds of untested cases .. even in something with 100% line coverage
    
    To properly evaluate mutation testing, I think this process is required, because you can’t
    truly understand how little line coverage gives you in comparison
    
    tjchambers 1:22 AM
    But I don't need a tool to tell me that a 250 character line of conditional code that by
    itself would be an oversized method AND counts more because there are fewer lines in the
    overall percentage contributes to a very foggy sense of coverage.
    
    dkubb 1:22 AM
    It would not be unusual for something with 100% line coverage to undergo mutation testing
    and actually find out that the tests only kill 60-70% of possible mutations
    
    tjchambers 1:22 AM
    @dkubb or less
    
    dkubb 1:23 AM
    usually much less :stuck_out_tongue:
    
    it can be really humbling
    
    mbj 1:23 AM
    In this discussion you miss that many test suites (unless you have noop detection):
    Will show false coverage.
    
    tjchambers 1:23 AM
    When I started with mutant on my own project which I developed I had 95% LOC coverage
    
    mbj 1:23 AM
    Test suites need to be fixed to comply to mutation testing invariants.
    
    tjchambers 1:23 AM
    I had 34% mutation coverage
    
    And that was ignoring the 5% that wasn't covered at all
    
    mbj 1:24 AM
    Also if the tool you compare MT with line coverage on: Is not very strong,
    the improvement may not be visible.
    
    dkubb 1:24 AM
    another nice benefit is that you will become much better at enumerating all
    the things you need to do when writing tests
    
    tjchambers 1:24 AM
    @dkubb or better yet - when writing code.
    
    The way I look at it - the fewer the alive mutations the better the test,
    the fewer the mutations the better the code.
    
    dkubb 1:29 AM
    yeah, you can infer a kind of cyclomatic complexity by looking at how many mutations there are
    
    tjchambers 1:31 AM
    Even without tests (not recommended) you can judge a lot from the mutations themselves.
    
    I still am an advocate for mutations/LOC metric

As you can see members in the community are strong supporters of mutation testing, all of them
having much more experience than I do.

I'd like to hear more practical examples if you are able to share them since I'm
collecting conference material on this topic. Thanks for reading and happy testing!
