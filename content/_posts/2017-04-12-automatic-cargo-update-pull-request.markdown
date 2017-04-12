Title: Automatic cargo update & pull requests for Rust projects
date: 2017-04-15 23:18
comments: true
Tags: QA, fedora.planet

If you follow my blog you are aware that I use automated tools to do some
boring tasks instead of me. For example they can detect when new versions of
dependencies I'm using are available and then schedule testing against them on the fly.

One of these tools is
[Strazar](http://mrsenko.com/blog/mr-senko/2016/05/18/triggering-automatic-dependency-testing/)
which I use heavily for my Django based packages.
Example: [django-s3-cache build job](https://travis-ci.org/atodorov/django-s3-cache/builds/218758538).

Recently I've made a slightly different proof-of-concept for a Rust project.
Because rustc and various dependencies (called crates) are updated very often
we didn't want to expand the test matrix like Strazar does. Instead we wanted to
always build & test against the latest crates versions and if that passes
create a pull request for the update (in `Cargo.lock`). All of this unattended
of course!


To start create a cron job in Travis CI which will execute once per day and call your
test script. The script looks like this:

    :::bash cargo-update-and-pr
    #!/bin/bash
    
    if [ -z "$GITHUB_TOKEN" ]; then
        echo "GITHUB_TOKEN is not defined"
        exit 1
    fi
    
    BRANCH_NAME="automated_cargo_update"
    
    git checkout -b $BRANCH_NAME
    cargo update && cargo test
    
    DIFF=`git diff`
    # NOTE: we don't really check the result from testing here. Only that
    # something has been changed, e.g. Cargo.lock
    if [ -n "$DIFF" ]; then
        # configure git authorship
        git config --global user.email "atodorov@MrSenko.com"
        git config --global user.name "Alexander Todorov"
    
        # add a remote with read/write permissions!
        # use token authentication instead of password
        git remote add authenticated https://atodorov:$GITHUB_TOKEN@github.com/atodorov/bdcs-api-rs.git
    
        # commit the changes to Cargo.lock
        git commit -a -m "Auto-update cargo crates"
    
        # push the changes so that PR API has something to compare against
        git push authenticated $BRANCH_NAME
    
        # finally create the PR
        curl -X POST -H "Content-Type: application/json" -H "Authorization: token $GITHUB_TOKEN" \
             --data '{"title":"Auto-update cargo crates","head":"automated_cargo_update","base":"master", "body":"@atodorov review"}' \
             https://api.github.com/repos/atodorov/bdcs-api-rs/pulls
    fi


A few notes here:

* You need to define a secret `GITHUB_TOKEN` variable for authentication;
* The script doesn't force push, but in practice that may be useful (e.g. updating the PR);
* The script doesn't have any error handling;
* If PR is still open GitHub will tell us about it but we ignore the result here;
* **DON'T** paste this into your `Makefile` because the `GITHUB_TOKEN` variable will be
  expanded into the logs and your secrets go away! Always call the script from your
  `Makefile` to avoid revealing secrets.
* I am using topic branches because this is a POC. Switch to *master* and maybe move
  all URLs as variables at the top of the script!
* I run this cron build against a fork of the project because the team doesn't feel
  comfortable having automated commits/pushes. I also create the pull requests against
  my own fork. You will have to adjust the targets if you want your PR to go to the
  original repository.

Here is the PR which was created by this script:
<https://github.com/atodorov/bdcs-api-rs/pull/5>

Notice that it includes previous commits b/c they have not been merged to the master branch!

Here's the test job (#77) which generated this PR:
<https://travis-ci.org/atodorov/bdcs-api-rs/builds/219274916>

Here's a test job (#87) which bails out miserably because the PR already exists:
<https://travis-ci.org/atodorov/bdcs-api-rs/builds/220954269>



This post is part of my *Quality Assurance According to Einstein* series - a detailed description
of useful techniques I will be presenting very soon.

Thanks for reading and happy testing!
