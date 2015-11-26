---
layout: post
Title: Proxy Support for wrk HTTP Benchmarking Tool
date: 2014-11-18 10:04
comments: true
Tags: QA
---

Few times recently I've seen people using an HTTP benchmarking tool called
[wrk](https://github.com/wg/wrk) and decided to give it a try. It is a very cool
instrument but didn't fit my use case perfectly. What I needed is to be able to
redirect the connection through a web proxy and measure how much the proxy
slows down things compared to hitting the web server directly with wrk.
In other words - how fast is the proxy server.

How does a proxy work
---------------------

I've examined the source code of two proxies (one in Python and another one in Go)
and what happens is this:

* The proxy server starts listening to a TCP port
* A client (e.g. the browser) sends the request using an absolute URL (GET http://example.com/about.html)
* Instead of connecting directly to the web server behind example.com the client connects to the proxy
* The proxy server does connect to example.com directly, reads the response and delivers it back to 
the client.

Proxy in wrk
-------------

Luckily wrk supports the execution of Lua scripts so we can make a 
[simple script](https://github.com/wg/wrk/pull/107) like this:


    init = function(args)
        target_url = args[1] -- proxy needs absolute URL
    end
    
    request = function()
        return wrk.format("GET", target_url)
    end

Then update your command line to something like this:
    ./wrk [options] http://proxy:port -s proxy.lua -- http://example.com/about.html


This causes wrk to connect to our proxy server but instead issue GET requests for another URL.
Depending on how your proxy works you may need to add the `Host: example.com` header as well.
Now let's do some testing.
