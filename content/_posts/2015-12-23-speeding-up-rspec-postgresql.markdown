Title: Speeding up RSpec and PostgreSQL tests
date: 2015-12-23 11:34
comments: true
Tags: fedora.planet, Ruby

I've been working with [[Tradeo]] on testing one of their applications. The app
is standard Ruby on Rails application with over 1200 tests written with RSpec.
And they were horribly slow. On my [[MacBook Air]] the entire test suite
took 27 minutes to execute. On the Jenkins slaves it took over an hour.
After a few changes Jenkins now takes 15 minutes to execute the test suite.
Locally it takes around 11 minutes!

The Problem
-----------

I've measured the speed (with Time.now) at which individual examples execute
and it was quickly apparent they were taking a lot of time cleaning the DB. The
offending code in question was:

    :::ruby
    config.before(:all) do
      DatabaseCleaner.clean_with :truncation
    end

This is truncating the tables quite often but it turns out this is a very
expensive operation on tables with small number of records. I've measured it
locally around 2.5 seconds. Check out this
[SO thread](http://stackoverflow.com/questions/11419536/postgresql-truncation-speed/)
which describes pretty much the same symptoms:

    Right now, locally (on a Macbook Air) a full test suite takes 28 minutes....
    Tailing the logs on our CI server (Ubuntu 10.04 LTS) .... a build takes 84 minutes.

This
[excellent answer](http://stackoverflow.com/questions/11419536/postgresql-truncation-speed/11423886#11423886)
explains why this is happening:


    (a) The bigger shared_buffers may be why TRUNCATE is slower on the CI server.
        Different fsync configuration or the use of rotational media instead of
        SSDs could also be at fault.
    
    (b) TRUNCATE has a fixed cost, but not necessarily slower than DELETE,
        plus it does more work.

The Fix
-------

    :::ruby
    config.before(:suite) do
      DatabaseCleaner.clean_with :truncation
    end
    
    config.before(:all) do
      DatabaseCleaner.clean_with :deletion
    end

`before(:suite)` will truncate tables every time we run rspec, which is when we
launch the entire test suite. This is to account for the possible side effects
of DELETE in the future (see the SO thread). Then `before(:all)` aka
`before(:context)` simply deletes the records which is significantly faster!

Also updated the CI servers `postgresql.conf` to

    fsync=off
    full_page_writes=off

The entire build/test process now takes only 15 minutes! Only one test broke
due to PostgreSQL returning records in a different order, but it's the test
case fault not handling this in the first place!

**NOTE:** Using fsync=off with rotational media pretty much hides any improvements
introduced by updating the DatabaseCleaner strategy.

What's Next
-----------

There are several other things worth trying:

* Use UNIX domain sockets instead of TCP/IP (localhost) to connect to PostgreSQL;
* Load the entire
[PostgreSQL partition in memory](http://magazine.redhat.com/2007/12/12/tip-from-an-rhce-memory-storage-on-postgresql/);
* Don't delete anything from the database, except once in `before(:suite)`.
If any tests need a particular DB state they have to set this up on their own
instead of relying on a global cleanup process. I expect this to break quite
a few examples.

After the changes and with my crude measurements I have individual examples
taking 0.31 seconds to execute. Interestingly before and after take less than
a second while the example code takes around 0.15 seconds. I have no idea where
the rest 0.15 seconds are spent. My current speculation is probably RSpec.
This is 50% of the execution time and is also worth looking into!

