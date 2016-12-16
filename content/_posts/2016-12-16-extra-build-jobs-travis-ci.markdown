Title: How to create auxiliary build jobs in Travis-CI matrix
date: 2016-12-16 11:48
comments: true
Tags: QA, fedora.planet
og_image: images/travisci_extra_job_in_matrix.png
twitter_image: images/travisci_extra_job_in_matrix.png


![Auxiliary build job in Travis-CI](/images/travisci_extra_job_in_matrix.png "Auxiliary build job in Travis-CI")

In Travis-CI when you combine the three main configuration options of
*Runtime (language)*, *Environment* and *Exclusions/Inclusions* you get a
[build matrix](https://docs.travis-ci.com/user/customizing-the-build#Build-Matrix)
of all possible combinations! For example, for *django-chartit* the matrix includes
43 build jobs, spread across various Python and Django versions. For reference
see [Build #75](https://travis-ci.org/chartit/django-chartit/builds/181115880).

For *django-chartit* I wanted to have an additional build job which would execute
pylint. I wanted the job to be independent because currently pylint produces lots
of errors and warnings. Having an independent job instead of integrating pylint
together with all jobs makes it easier to see if any of the functional tests failed.

Using the inclusion functionality of Travis-CI I was able to define an auxiliary
build job. The trick is to provide sane environment defaults for all
build jobs (regular and auxiliary ones) so you don't have to expand your environment
section! In this case the change looks like this

    :::diff
    diff --git a/.travis.yml b/.travis.yml
    index 67f656d..9b669f9 100644
    --- a/.travis.yml
    +++ b/.travis.yml
    @@ -2,6 +2,8 @@ after_success:
     - coveralls
     before_install:
     - pip install coveralls
    +- if [ -z "$_COMMAND" ]; then export _COMMAND=coverage; fi
    +- if [ -z "$_DJANGO" ]; then export _DJANGO=1.10.4; fi
     env:
     - !!python/unicode '_DJANGO=1.10'
     - !!python/unicode '_DJANGO=1.10.2'
    @@ -41,6 +43,10 @@ matrix:
         python: 3.3
       - env: _DJANGO=1.10.4
         python: 3.3
    +  include:
    +  - env: _COMMAND=pylint
    +    python: 3.5
    +
     notifications:
       email:
         on_failure: change
    @@ -50,4 +56,4 @@ python:
     - 3.3
     - 3.4
     - 3.5
    -script: make coverage
    +script: make $_COMMAND

For more info take a look at
[commit b22eda7](https://github.com/chartit/django-chartit/commit/b22eda7cd67a062f49a0f60b8ac51383e4f8c3a5)
and [Build #77](https://travis-ci.org/chartit/django-chartit/builds/183883813). Note
Job #77.44!

Thanks for reading and happy testing!
