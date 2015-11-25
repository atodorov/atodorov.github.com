---
layout: post
Title: Speed Comparison of Web Proxies Written in Python Twisted and Go
date: 2014-11-19 16:57
comments: true
Tags: QA
---

After I figured out that
[Celery is rather slow](/blog/2014/11/11/speeding-up-celery-backends-part-3/)
I moved on to test another part of my environment - a web proxy server.
The test here compares two proxy 
[implementations](https://gist.github.com/atodorov/666035d270d97d982cd5)
- one with Python Twisted,
the other in Go. The backend is a simple web server written in Go, which is
probably the fastest thing when it comes to serving HTML.

The test content is a snapshot of the front page of this blog taken few days ago.
The system is a standard Lenovo X220 laptop, with Intel Core i7 CPU, with 4 cores.
The measurement instrument is the popular wrk tool with a
[custom Lua script to redirect the requests through the proxy](/blog/2014/11/18/proxy-support-for-wrk-http-benchmarking-tool/).

All tests were repeated several times, only the best results are shown here.
I've taken time between the tests in order for all open TCP ports to close.
I've also observed the number of open ports (e.g. sockets) using `netstat`.

Baseline
--------

Using wrk against the web server in Go yields around 30000 requests per second
with an average of 2000 TCP ports in use:

    $ ./wrk -c1000 -t20 -d30s http://127.0.0.1:8000/atodorov.html
    Running 30s test @ http://127.0.0.1:8000/atodorov.html
      20 threads and 1000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   304.43ms  518.27ms   1.47s    82.69%
        Req/Sec     1.72k     2.45k   17.63k    88.70%
      1016810 requests in 29.97s, 34.73GB read
      Non-2xx or 3xx responses: 685544
    Requests/sec:  33928.41
    Transfer/sec:      1.16GB


Python Twisted
--------------

The [Twisted implementation](https://gist.github.com/atodorov/666035d270d97d982cd5)
performs at little over 1000 reqs/sec with an average TCP port use between 20000 and 30000:

    ./wrk -c1000 -t20 -d30s http://127.0.0.1:8080 -s scripts/proxy.lua -- http://127.0.0.1:8000/atodorov.html
    Running 30s test @ http://127.0.0.1:8080
      20 threads and 1000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   335.53ms  117.26ms 707.57ms   64.77%
        Req/Sec   104.14     72.19   335.00     55.94%
      40449 requests in 30.02s, 3.67GB read
      Socket errors: connect 0, read 0, write 0, timeout 8542
      Non-2xx or 3xx responses: 5382
    Requests/sec:   1347.55
    Transfer/sec:    125.12MB


Go proxy
--------

First I've run several 30 seconds tests and performance was around 8000 req/sec
with around 20000 ports used (most of them remain in TIME_WAIT state for a while).
Then I've modified `proxy.go` to make use of all available CPUs on the system and let
the test run for 5 minutes.

    $ ./wrk -c1000 -t20 -d300s http://127.0.0.1:9090 -s scripts/proxy.lua -- http://127.0.0.1:8000/atodorov.html
    Running 5m test @ http://127.0.0.1:9090
      20 threads and 1000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   137.22ms  437.95ms   4.45s    97.55%
        Req/Sec   669.54    198.52     1.71k    76.40%
      3423108 requests in 5.00m, 58.27GB read
      Socket errors: connect 0, read 26, write 181, timeout 24268
      Non-2xx or 3xx responses: 2870522
    Requests/sec:  11404.19
    Transfer/sec:    198.78MB

Performance peaked at 10000 req/sec. TCP port usage initially rose to around 30000
but rapidly dropped and stayed around 3000. Both `webserver.go` and `proxy.go` were
printing the following messages on the console:

    2014/11/18 21:53:06 http: Accept error: accept tcp [::]:9090: too many open files; retrying in 1s

Conclusion
----------

There's no doubt that Go is blazingly fast compared to Python and I'm most likely to use it
further in my experiments. Still I didn't expect a 3x difference in performance from webserver vs. proxy.

Another thing that worries me is the huge number of open TCP ports which then drops and stays
consistent over time and the error messages from both webserver and proxy (maybe per process sockets limit).

At the moment I'm not aware of the internal workings of neither wrk, nor
Go itself, nor the goproxy library to make conclusion if this is a bad thing or expected.
I'm eager to hear what others think in the comments. Thanks!


Update 2015-01-27
-----------------

I have retested with PyPy but on a different system so I'm giving all the test results
on it as well. `/proc/cpuinfo` says we have 16 x Intel(R) Xeon(R) CPU E5-2450L 0 @ 1.80GHz
CPUs. 

Baseline - Go server:

    $ ./wrk -c1000 -t20 -d30s http://127.0.0.1:8000/atodorov.html
    Running 30s test @ http://127.0.0.1:8000/atodorov.html
      20 threads and 1000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    15.57ms   20.38ms 238.93ms   98.11%
        Req/Sec     3.55k     1.32k   15.91k    82.49%
      1980738 requests in 30.00s, 174.53GB read
      Socket errors: connect 0, read 0, write 0, timeout 602
      Non-2xx or 3xx responses: 60331
    Requests/sec:  66022.87
    Transfer/sec:      5.82GB


Go proxy (30 sec):

    $ ./wrk -c1000 -t20 -d30s http://127.0.0.1:9090 -s scripts/proxy.lua -- http://127.0.0.1:8000/atodorov.html
    Running 30s test @ http://127.0.0.1:9090
      20 threads and 1000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    68.93ms  718.98ms  12.60s    99.58%
        Req/Sec     1.61k   784.01     4.83k    62.50%
      942757 requests in 30.00s, 32.16GB read
      Socket errors: connect 0, read 26, write 0, timeout 3050
      Non-2xx or 3xx responses: 589940
    Requests/sec:  31425.47
    Transfer/sec:      1.07GB


Python proxy with `Twisted==14.0.2` and `pypy-2.2.1-2.el7.x86_64`:

    $ ./wrk -c1000 -t20 -d30s http://127.0.0.1:8080 -s scripts/proxy.lua -- http://127.0.0.1:8000/atodorov.html
    Running 30s test @ http://127.0.0.1:8080
      20 threads and 1000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   858.75ms    1.47s    6.00s    88.09%
        Req/Sec   146.39    104.83   341.00     54.18%
      85645 requests in 30.00s, 853.54MB read
      Socket errors: connect 0, read 289, write 0, timeout 3297
      Non-2xx or 3xx responses: 76567
    Requests/sec:   2854.45
    Transfer/sec:     28.45MB

**Update 2015-01-27-2**

Python proxy with `Twisted==14.0.2` and `python-2.7.5-16.el7.x86_64`:

    $ ./wrk -c1000 -t20 -d30s http://127.0.0.1:8080 -s scripts/proxy.lua -- http://127.0.0.1:8000/atodorov.html
    Running 30s test @ http://127.0.0.1:8080
      20 threads and 1000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   739.64ms    1.58s   14.22s    96.18%
        Req/Sec    84.43     36.61   157.00     67.79%
      49173 requests in 30.01s, 701.77MB read
      Socket errors: connect 0, read 240, write 0, timeout 2463
      Non-2xx or 3xx responses: 41683
    Requests/sec:   1638.38
    Transfer/sec:     23.38MB


As seen Go proxy is slower than the Go server by factor of 2.
Python proxy is slower by than the Go server by factor of 20.
These results are similar to previous ones so I don't think PyPy
makes any significant difference.
