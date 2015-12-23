Title: Interesting Ruby Resources
date: 2015-12-23 12:48
comments: true
Tags: fedora.planet, Ruby

During my quest for
[faster RSpec tests]({filename}2015-12-23-speeding-up-rspec-postgresql.markdown)
I've come across several interesting posts about Ruby. Being new to the language
they've helped me understand a bit more about the internals. Posting them here
so they don't get lost.

Garbage Collection
-------------------

[The road to faster tests](https://signalvnoise.com/posts/2742-the-road-to-faster-tests)
- a story about tests and garbage collection.

[Tuning Ruby garbage collection for RSpec](http://labs.clio.com/tuning-ruby-garbage-collection-for-rspec/)
- practical explanation of Ruby's garbage collector and how to adjust its
performance for RSpec

[Demystifying the Ruby GC](http://samsaffron.com/archive/2013/11/22/demystifying-the-ruby-gc)

Probably the very first posts I found referencing slow RSpec tests. It turned out
this was not the issue but I've nevertheless tried running GC manually. I can clearly
see (using `puts GC.count` in after()) GC invoked less frequently, memory usage rising
but the overall execution time wasn't affected. The profiler said 2% speed increase
to be honest.


Profiling
---------

Not being very clear about the different profiling tools available and how to
interpret their results I've found these articles:

[Profiling Ruby With Google's Perftools](https://www.igvita.com/2009/06/13/profiling-ruby-with-googles-perftools/)
- practical example for using perftools.rb

[How to read ruby profiler's output](http://stackoverflow.com/questions/32212970/how-to-read-ruby-profilers-output) -
also see the [Profiler__ module](http://ruby-doc.org/stdlib-2.1.0/libdoc/profiler/rdoc/Profiler__.html)

[Show runtime for each rspec example](http://stackoverflow.com/questions/4856500/show-runtime-for-each-rspec-example)
- using `rspec --profile`


Suggestions for Faster Tests
-----------------------------

Several general best practices for faster tests:

[9 ways to speed up your RSpec tests](https://www.netguru.co/blog/9-ways-to-speed-up-your-rspec-tests)

[Run faster Ruby on Rails tests](https://infinum.co/the-capsized-eight/articles/run-faster-ruby-on-rails-tests)

[Three tips to improve the performance of your test suite](http://blog.plataformatec.com.br/2011/12/three-tips-to-improve-the-performance-of-your-test-suite/)

RubyGems related
-----------------

I've noticed Bundler loading tons of requirements (nearly 3000 unique modules)
and for some particular specs this wasn't necessary (for example running Rubocop).
I've found the following articles below which sound very reasonable to me:

[Use Bundler.setup Instead of Bundler.require](http://anti-pattern.com/use-bundler-setup-instead-of-bundler-require)

[5 Reasons to Avoid Bundler.require](http://myronmars.to/n/dev-blog/2012/12/5-reasons-to-avoid-bundler-require)

[Why "require 'rubygems'" Is Wrong](http://2ndscale.com/rtomayko/2009/require-rubygems-antipattern)


Weird
-----

Finally (or more precisely first of all) I've seen this
[Weird performance issue](https://www.ruby-forum.com/topic/184516 suggests broken rubygems).

During my initial profiling I've seen (and still see) a similar issue.
When calling require it goes through lots of hoops before finally loading
the module. My profiling results show this taking a lot of time but this time
is likely measured with profiling enabled and doesn't represent the real deal.

On my
[MacBook Air with Red Hat Enterprise Linux 7]({filename}2015-04-26-installing-red-hat-enterprise-linux-7-on-macbook-air-2015.markdown)
this happens when using Ruby 2.2.2 from Software Collections. If using Ruby
installed from source with rbenv the profiling profile is completely different.

I will be examining this one in more details. I'm interested to know what is
the difference and if that affects performance somehow so stay tuned!

