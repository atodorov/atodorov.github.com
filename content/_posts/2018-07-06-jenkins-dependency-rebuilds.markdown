Title:  Upstream rebuilds with Jenkins Job Builder
Headline: for downstream pull requests
date: 2018-07-06 13:20
comments: true
Tags: fedora.planet, QA
og_image: images/bricks.jpg
twitter_image: images/bricks.jpg


I have been working on [Weldr](http://weldr.io/) for some time now.
It is a multi-component software with several layers built on top of
each other as seen on the image below.

![Weldr components](/images/welder_upstream.png)

One of the risks that we face is introducing changes in
downstream components which are going to break something up the stack!
In this post I am going to show you how I have configured
Jenkins to trigger dependent rebuilds and report all of the statuses
back to the original GitHub PR. All of the code below is Jenkins Job Builder
yaml.


`bdcs` is the first layer of our software stack. It provides command line
utilities. `codec-rpm` is a library component that facilitates working
with RPM packages (in Haskell). `bdcs` links to `codec-rpm` when it is compiled,
`bdcs` uses some functions and data types from `codec-rpm`.

When a pull request is opened against `codec-rpm` and testing completes successfully
I want to reuse that particular version of the `codec-rpm` library and
rebuild/test `bdcs` with that.


YAML configuration
------------------

All jobs have the following structure: -trigger -> -provision -> -runtest -> -teardown.
This means that Jenkins will start executing a new job when it gets triggered by
an event in GitHub (commit to master branch or new pull request), then it will
provision a slave VM in OpenStack, execute the test suite on the slave and destroy
all of the resources at the end. This is repeated twice: for master branch and for
pull requests! Here's how the -runtest jobs look:

    :::yaml
    - job-template:
        name: '{name}-provision'
        node: master
        parameters:
          - string:
              name: PROVIDER
        scm:
            - git:
                url: 'https://github.com/weldr/{repo_name}.git'
                refspec: ${{git_refspec}}
                branches:
                  - ${{git_branch}}
        builders:
          - github-notifier
          - shell: |
                #!/bin/bash -ex
                # do the openstack provisioning here
            # NB: runtest_job is passed to us via the -trigger job
          - trigger-builds:
              - project: '${{runtest_job}}'
                block: true
                current-parameters: true
                condition: 'SUCCESS'
                fail-on-missing: true
    
    
    - job-template:
        name: '{name}-master-runtest'
        node: cinch-slave
        project-type: freestyle
        description: 'Build master branch of {name}!'
        scm:
            - git:
                url: 'https://github.com/weldr/{repo_name}.git'
                branches:
                    - master
        builders:
          - github-notifier
          - conditional-step:
              condition-kind: regex-match
              regex: "^.+$"
              label: '${{UPSTREAM_BUILD}}'
              on-evaluation-failure: dont-run
              steps:
                - copyartifact:
                    project: ${{UPSTREAM_BUILD}}
                    which-build: specific-build
                    build-number: ${{UPSTREAM_BUILD_NUMBER}}
                    filter: ${{UPSTREAM_ARTIFACT}}
                    flatten: true
          - shell: |
                #!/bin/bash -ex
                make ci
        publishers:
          - trigger-parameterized-builds:
              - project: '{name}-teardown'
                current-parameters: true
          - github-notifier
    
    
    - job-template:
        name: '{name}-PR-runtest'
        node: cinch-slave
        description: 'Build PRs for {name}!'
        scm:
            - git:
                url: 'https://github.com/weldr/{repo_name}.git'
                refspec: +refs/pull/*:refs/remotes/origin/pr/*
                branches:
                    # builds the commit hash instead of a branch
                    - ${{ghprbActualCommit}}
        builders:
          - github-notifier
          - shell: |
                #!/bin/bash -ex
                make ci
          - conditional-step:
              condition-kind: current-status
              condition-worst: SUCCESS
              condition-best: SUCCESS
              on-evaluation-failure: dont-run
              steps:
                - shell: |
                    #!/bin/bash -ex
                    make after_success
        publishers:
          - archive:
              artifacts: '{artifacts_path}'
              allow-empty: '{artifacts_empty}'
          - conditional-publisher:
              - condition-kind: '{execute_dependent_job}'
                on-evaluation-failure: dont-run
                action:
                  - trigger-parameterized-builds:
                    - project: '{dependent_job}'
                      current-parameters: true
                      predefined-parameters: |
                        UPSTREAM_ARTIFACT={artifacts_path}
                        UPSTREAM_BUILD=${{JOB_NAME}}
                        UPSTREAM_BUILD_NUMBER=${{build_number}}
                      condition: 'SUCCESS'
          - trigger-parameterized-builds:
              - project: '{name}-teardown'
                current-parameters: true
          - github-notifier
    
    
    - job-group:
        name: '{name}-tests'
        jobs:
        - '{name}-provision'
        - '{name}-teardown'
        - '{name}-master-trigger'
        - '{name}-master-runtest'
        - '{name}-PR-trigger'
        - '{name}-PR-runtest'
    
    
    - job:
        name: 'codec-rpm-rebuild-bdcs'
        node: master
        project-type: freestyle
        description: 'Rebuild bdcs after codec-rpm PR!'
        scm:
            - git:
                url: 'https://github.com/weldr/codec-rpm.git'
                refspec: +refs/pull/*:refs/remotes/origin/pr/*
                branches:
                    # builds the commit hash instead of a branch
                    - ${ghprbActualCommit}
        builders:
          - github-notifier
          - trigger-builds:
              - project: 'bdcs-master-trigger'
                block: true
                predefined-parameters: |
                    UPSTREAM_ARTIFACT=${UPSTREAM_ARTIFACT}
                    UPSTREAM_BUILD=${UPSTREAM_BUILD}
                    UPSTREAM_BUILD_NUMBER=${UPSTREAM_BUILD_NUMBER}
        publishers:
          - github-notifier
    
    
    - project:
        name: codec-rpm
        dependent_job: '{name}-rebuild-bdcs'
        execute_dependent_job: always
        artifacts_path: 'dist/{name}-latest.tar.gz'
        artifacts_empty: false
        jobs:
          - '{name}-tests'



Publishing artifacts
--------------------

`make after_success` is responsible for creating a tarball if `codec-rpm` test suite
passed. This tarball gets uploaded as artifact into Jenkins and we can make use of it later!


Inside -master-runtest I have a `conditional-step` inside the `builders` section which
will copy the artifacts from the previous build if they are present. Notice that I copy
artifacts for a particular job number, which is the job for codec-rpm PR.

Making use of local artifacts is handled inside bdcs' `make ci` because it is
per-project specific and because I'd like to reuse my YAML templates.


Reporting statuses to GitHub
----------------------------

For `github-notifier` to be able to report statuses back to the pull request
the job needs to be configured with the git repository this pull request came from.
This is done by specifying the same `scm` section for all jobs that are related and
`current-parameters: true` to pass the revision information to the other jobs.

This also means that if I want to report status from `codec-rpm-rebuild-bdcs` then
it needs to be configured for the `codec-rpm` repository (see yaml) but somehow
it should trigger jobs for another repository!


When jobs are started via `trigger-parameterized-builds` their statuses are reported
separately to GitHub. When they are started via `trigger-builds` there should be only
one status reported.


Trigger chain for dependency rebuilds
-------------------------------------

With all of the above info we can now look at the `codec-rpm-rebuild-bdcs` job.

* It is configured for the codec-rpm repository so it will report its status to the PR
* It is conditionally started after `codec-rpm-PR-runtest` finishes successfully
* It triggers `bdcs-master-trigger` which in turn will rebuild & retest the bdcs component.
  Additional parameters specify whether we're going to use locally built artifacts or
  attempt to download then from Hackage
* It uses `block: true` so that the status of `codec-rpm-rebuild-bdcs` is dependent
  on the status of `bdcs-master-runtest` (everything in the job chain uses `block: true` because of this)


How this looks like in practice
-------------------------------

I have opened [codec-rpm #39](https://github.com/weldr/codec-rpm/pull/39)
to validate my configuration. The chain of jobs that gets executed in Jenkins is:

    --- console.log for bdcs-master-runtest ---
    Started by upstream project "bdcs-jslave-1-provision" build number 267
    originally caused by:
     Started by upstream project "bdcs-master-trigger" build number 133
     originally caused by:
      Started by upstream project "codec-rpm-rebuild-bdcs" build number 25
      originally caused by:
       Started by upstream project "codec-rpm-PR-runtest" build number 77
       originally caused by:
        Started by upstream project "codec-rpm-jslave-1-provision" build number 178
        originally caused by:
         Started by upstream project "codec-rpm-PR-trigger" build number 118
         originally caused by:
          GitHub pull request #39 of commit b00c923065e367afd5b7a7cc068b049bb1ed25e1, no merge conflicts.

Statuses are reported on GitHub as follows:

![example of PR statuses](/images/codec-rpm-pr-39.png)

`default` is coming from the provisioning step and I think this is some sort of a bug
or misconfiguration of the provisioning job. We don't really care about this.

On the picture you can see that `codec-rpm-PR-runtest` was successful but
`codec-rpm-rebuild-bdcs` was not. The actual error when compiling bdcs is:

    :::
    src/BDCS/Import/RPM.hs:110:24: error:
        * Couldn't match type `Entry' with `C8.ByteString'
          Expected type: conduit-1.2.13.1:Data.Conduit.Internal.Conduit.ConduitM
                           C8.ByteString
                           Data.Void.Void
                           Data.ContentStore.CsMonad
                           ([T.Text], [Maybe ObjectDigest])
            Actual type: conduit-1.2.13.1:Data.Conduit.Internal.Conduit.ConduitM
                           Entry
                           Data.Void.Void
                           Data.ContentStore.CsMonad
                           ([T.Text], [Maybe ObjectDigest])
        * In the second argument of `(.|)', namely
            `getZipConduit
               ((,) <$> ZipConduit filenames <*> ZipConduit digests)'
          In the second argument of `($)', namely
            `src
               .|
                 getZipConduit
                   ((,) <$> ZipConduit filenames <*> ZipConduit digests)'
          In the second argument of `($)', namely
            `runConduit
               $ src
                   .|
                     getZipConduit
                       ((,) <$> ZipConduit filenames <*> ZipConduit digests)'
        |
    110 |                     .| getZipConduit ((,) <$> ZipConduit filenames
        |                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...


That is because PR #39 changes the return type of `Codec.RPM.Conduit::payloadContentsC`
from `Entry` to `C8.ByteString`.

Thanks for reading and happy testing!


*social image CC by https://pxhere.com/en/photo/226978*
