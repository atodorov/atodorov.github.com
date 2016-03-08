Title: Floating-point precision error with Ruby
Headline: Time.at(now.to_f) != now
date: 2016-03-08 11:08
comments: true
Tags: fedora.planet, Ruby, QA

One of my tests was faiing and it turned out this was caused by a
floating-point precision error. The functionality in question was a "Load more"
button with pagination which loads records from the database and the front-end displays them.

Ruby and JavaScript were passing around a parameter
which was only used as part of the SQL queries.
Now the problem is that JavaScript doesn't have a `Time` class and the parameter
was passed as string, then converted back to `Time` in Ruby. The problem
comes from the intermediate conversion to `float` which was used.

Here's a little code snippet to demonstrate the problem:

    :::ruby
    irb(main):068:0* now = Time.now
    => 2016-03-08 10:54:26 +0200
    irb(main):069:0> 
    irb(main):070:0* Time.at(now) == now
    => true
    irb(main):071:0> 
    irb(main):072:0* Time.at(now.to_f) == now
    => false
    irb(main):073:0> 
    irb(main):074:0* now.to_f
    => 1457427266.7206197
    irb(main):075:0> 
    irb(main):076:0* now.strftime('%Y-%m-%d %H:%M:%S.%9N')
    => "2016-03-08 10:54:26.720619705"
    irb(main):077:0> 
    irb(main):079:0* Time.at(now.to_f).strftime('%Y-%m-%d %H:%M:%S.%9N')
    => "2016-03-08 10:54:26.720619678"
    irb(main):080:0> 


As you can see the conversion to float and back to Time is off by a few
nano-seconds and the database either didn't return any records or was
returning the same set of records.
This isn't something you can usually see in production, right ? Unless you
have huge traffic and happen to have records created exactly at the same moment.

The solution is to simply send `Time.now.strftime` to the JavaScript and then
use `Time.parse` to reconstruct the value.

    :::ruby
    irb(main):077:0> 
    irb(main):001:0> require 'time'
    => true
    irb(main):002:0> Time.parse(now.strftime('%Y-%m-%d %H:%M:%S.%9N')).strftime('%Y-%m-%d %H:%M:%S.%9N')
    => "2016-03-08 10:54:26.720619705"
    irb(main):003:0> 


If you'd like to read more about floating point arithmetics please see
<http://floating-point-gui.de>.
