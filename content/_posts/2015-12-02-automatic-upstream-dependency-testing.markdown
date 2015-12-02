Title: Automatic Upstream Dependency Testing
Headline: with Travis-CI, GitHub and Python
date: 2015-12-02 10:34
comments: true
Tags: fedora.planet, Python, OpenShift, Django, QA
og_image: images/travisci_matrix.png

Ever since
[RHEL 7.2 python-libs broke s3cmd]({filename}2015-11-24-python-libs-in-rhel-7.2-broke-ssl-verification-in-s3cmd.markdown)
I've been pondering an age old problem: *How do I know if my software works with the
latest upstream dependencies ? How can I pro-actively monitor for new versions
and add them to my test matrix ?*

Mixing together my previous experience with
[Difio]({filename}2014-05-06-opensource-dot-com-article-10-steps-to-migrate-your-closed-software-to-open-source.markdown)
and monitoring upstream sources,
and [Forbes Lindesay's](https://twitter.com/ForbesLindesay) *GitHub Automation* talk
at [DEVit Conf]({filename}2015-05-22-devit-conf-2015-impressions.markdown) I came
together with a plan:

* Make an application which will execute when new upstream version is available;
* [Automatically update `.travis.yml`]({filename}2015-12-01-commit-github-api-python.markdown)
for the projects I'm interested in;
* Let Travis-CI execute my test suite for all available upstream versions;
* Profit!

How Does It Work
----------------

First we need to monitor upstream! RubyGems.org has nice
[webhooks interface](http://guides.rubygems.org/rubygems-org-api/#webhook-methods),
you can even trigger on individual packages. PyPI however doesn't have anything
like this :(. My solution is to run a cron job every hour and parse their RSS
stream for newly released packages. This has been working previously for Difio
so I re-used one function from the code.

After finding anything we're interested in comes the hard part - automatically
updating `.travis.yml` using the GitHub API. I've described this in more detail
[here]({filename}2015-12-01-commit-github-api-python.markdown). This time
I've slightly modified the code to update only when needed and accept more
parameters so it can be reused.

Travis-CI has a clean interface to specify environment variables and
[defining several](https://docs.travis-ci.com/user/environment-variables/#Defining-Multiple-Variables-per-Item)
of them crates a test matrix. This is exactly what I'm doing.
`.travis.yml` is updated with a new ENV setting, which determines the upstream
package version. After commit new build is triggered which includes the expanded
test matrix.

Example
--------

![Travis-CI build log]({filename}/images/travisci_matrix.png "Travis-CI build log")

Imagine that our *Project 2501* depends on FOO version *0.3.1*. The
[build log](https://travis-ci.org/atodorov/bztest/builds) illustrates what
happened:

* Build #9 is what we've tested with *FOO-0.3.1* and released to production.
Test result is PASS!
* Build #10 - meanwhile upstream releases *FOO-0.3.2* which causes our project
to break. We're not aware of this and continue developing new features
while all test results still PASS! When our customers upgrade their systems
*Project 2501* will break ! Tests didn't catch it because test matrix wasn't
updated. Please
ignore the actual commit message in the example! I've used the same repository
for the dummy dependency package.
* Build #11 - the monitoring solution finds *FOO-0.3.2* and updates the test
matrix automatically. The build immediately breaks! More precisely the
[test with version *0.3.2* fails](https://travis-ci.org/atodorov/bztest/builds/94263181)!
* Build #12 - we've alerted FOO.org about their problem and they've released
*FOO-0.3.3*. Our monitor has found that and updated the test matrix.
However [the 0.3.2 test job still fails](https://travis-ci.org/atodorov/bztest/builds/94270592)!
* Build #13 - we decide to workaround the 0.3.2 failure or simply handle the
error gracefully. In this example I've removed version 0.3.2 from the test
matrix to simulate that. In reality I wouldn't touch `.travis.yml` but instead
update my application and tests to check for that particular version.
All test results are PASS again!

Btw Build #11 above was triggered manually (./monitor.py) while Build #12
came from OpenShit, my hosting environment.

At present I have this monitoring enabled for my
[new Markdown extensions]({filename}2015-11-26-new-markdown-extensions.markdown)
and will also add it to [django-s3-cache](https://github.com/atodorov/django-s3-cache)
once it migrates to Travis-CI (it uses drone.io now).

Enough Talk, Show me the Code
------------------------------

    :::python monitor.py
    #!/usr/bin/env python
    
    import os
    import sys
    import json
    import base64
    import httplib
    from pprint import pprint
    from datetime import datetime
    from xml.dom.minidom import parseString
    
    def get_url(url, post_data = None):
        # GitHub requires a valid UA string
        headers = {
            'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.5) Gecko/20120601 Firefox/10.0.5',
        }
    
        # shortcut for GitHub API calls
        if url.find("://") == -1:
            url = "https://api.github.com%s" % url
    
        if url.find('api.github.com') > -1:
            if not os.environ.has_key("GITHUB_TOKEN"):
                raise Exception("Set the GITHUB_TOKEN variable")
            else:
                headers.update({
                    'Authorization': 'token %s' % os.environ['GITHUB_TOKEN']
                })
    
        (proto, host_path) = url.split('//')
        (host_port, path) = host_path.split('/', 1)
        path = '/' + path
    
        if url.startswith('https'):
            conn = httplib.HTTPSConnection(host_port)
        else:
            conn = httplib.HTTPConnection(host_port)
    
    
        method = 'GET'
        if post_data:
            method = 'POST'
            post_data = json.dumps(post_data)
    
        conn.request(method, path, body=post_data, headers=headers)
        response = conn.getresponse()
    
        if (response.status == 404):
            raise Exception("404 - %s not found" % url)
    
        result = response.read().decode('UTF-8', 'replace')
        try:
            return json.loads(result)
        except ValueError:
            # not a JSON response
            return result
    
    def post_url(url, data):
        return get_url(url, data)
    
    
    def monitor_rss(config):
        """
            Scan the PyPI RSS feeds to look for new packages.
            If name is found in config then execute the specified callback.
    
            @config is a dict with keys matching package names and values
            are lists of dicts
                {
                    'cb' : a_callback,
                    'args' : dict
                }
        """
        rss = get_url("https://pypi.python.org/pypi?:action=rss")
        dom = parseString(rss)
        for item in dom.getElementsByTagName("item"):
            try:
                title = item.getElementsByTagName("title")[0]
                pub_date = item.getElementsByTagName("pubDate")[0]
    
                (name, version) = title.firstChild.wholeText.split(" ")
                released_on = datetime.strptime(pub_date.firstChild.wholeText, '%d %b %Y %H:%M:%S GMT')
    
                if name in config.keys():
                    print name, version, "found in config"
                    for cfg in config[name]:
                        try:
                            args = cfg['args']
                            args.update({
                                'name' : name,
                                'version' : version,
                                'released_on' : released_on
                            })
    
                            # execute the call back
                            cfg['cb'](**args)
                        except Exception, e:
                            print e
                            continue
            except Exception, e:
                print e
                continue
    
    def update_travis(data, new_version):
        travis = data.rstrip()
        new_ver_line = "  - VERSION=%s" % new_version
        if travis.find(new_ver_line) == -1:
            travis += "\n" + new_ver_line + "\n"
        return travis
    
    
    def update_github(**kwargs):
        """
            Update GitHub via API
        """
        GITHUB_REPO = kwargs.get('GITHUB_REPO')
        GITHUB_BRANCH = kwargs.get('GITHUB_BRANCH')
        GITHUB_FILE = kwargs.get('GITHUB_FILE')
    
        # step 1: Get a reference to HEAD
        data = get_url("/repos/%s/git/refs/heads/%s" % (GITHUB_REPO, GITHUB_BRANCH))
        HEAD = {
            'sha' : data['object']['sha'],
            'url' : data['object']['url'],
        }
    
        # step 2: Grab the commit that HEAD points to
        data = get_url(HEAD['url'])
        # remove what we don't need for clarity
        for key in data.keys():
            if key not in ['sha', 'tree']:
                del data[key]
        HEAD['commit'] = data
    
        # step 4: Get a hold of the tree that the commit points to
        data = get_url(HEAD['commit']['tree']['url'])
        HEAD['tree'] = { 'sha' : data['sha'] }
    
        # intermediate step: get the latest content from GitHub and make an updated version
        for obj in data['tree']:
            if obj['path'] == GITHUB_FILE:
                data = get_url(obj['url']) # get the blob from the tree
                data = base64.b64decode(data['content'])
                break
    
        old_travis = data.rstrip()
        new_travis = update_travis(old_travis, kwargs.get('version'))
    
        # bail out if nothing changed
        if new_travis == old_travis:
            print "new == old, bailing out", kwargs
            return
    
        ####
        #### WARNING WRITE OPERATIONS BELOW
        ####
    
        # step 3: Post your new file to the server
        data = post_url(
                    "/repos/%s/git/blobs" % GITHUB_REPO,
                    {
                        'content' : new_travis,
                        'encoding' : 'utf-8'
                    }
                )
        HEAD['UPDATE'] = { 'sha' : data['sha'] }
    
        # step 5: Create a tree containing your new file
        data = post_url(
                    "/repos/%s/git/trees" % GITHUB_REPO,
                    {
                        "base_tree": HEAD['tree']['sha'],
                        "tree": [{
                            "path": GITHUB_FILE,
                            "mode": "100644",
                            "type": "blob",
                            "sha": HEAD['UPDATE']['sha']
                        }]
                    }
                )
        HEAD['UPDATE']['tree'] = { 'sha' : data['sha'] }
    
        # step 6: Create a new commit
        data = post_url(
                    "/repos/%s/git/commits" % GITHUB_REPO,
                    {
                        "message": "New upstream dependency found! Auto update .travis.yml",
                        "parents": [HEAD['commit']['sha']],
                        "tree": HEAD['UPDATE']['tree']['sha']
                    }
                )
        HEAD['UPDATE']['commit'] = { 'sha' : data['sha'] }
    
        # step 7: Update HEAD, but don't force it!
        data = post_url(
                    "/repos/%s/git/refs/heads/%s" % (GITHUB_REPO, GITHUB_BRANCH),
                    {
                        "sha": HEAD['UPDATE']['commit']['sha']
                    }
                )
    
        if data.has_key('object'): # PASS
            pass
        else: # FAIL
            print data['message']
    
    
    if __name__ == "__main__":
        config = {
            "atodorov-test" : [
                {
                    'cb' : update_github,
                    'args': {
                        'GITHUB_REPO' : 'atodorov/bztest',
                        'GITHUB_BRANCH' : 'master',
                        'GITHUB_FILE' : '.travis.yml'
                    }
                }
            ],
            "Markdown" : [
                {
                    'cb' : update_github,
                    'args': {
                        'GITHUB_REPO' : 'atodorov/Markdown-Bugzilla-Extension',
                        'GITHUB_BRANCH' : 'master',
                        'GITHUB_FILE' : '.travis.yml'
                    }
                },
                {
                    'cb' : update_github,
                    'args': {
                        'GITHUB_REPO' :  'atodorov/Markdown-No-Lazy-Code-Extension',
                        'GITHUB_BRANCH' : 'master',
                        'GITHUB_FILE' : '.travis.yml'
                    }
                },
                {
                    'cb' : update_github,
                    'args': {
                        'GITHUB_REPO' :  'atodorov/Markdown-No-Lazy-BlockQuote-Extension',
                        'GITHUB_BRANCH' : 'master',
                        'GITHUB_FILE' : '.travis.yml'
                    }
                },
            ],
        }
    
        # check the RSS to see if we have something new
        monitor_rss(config)
