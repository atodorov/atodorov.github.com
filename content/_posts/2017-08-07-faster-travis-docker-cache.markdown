Title: Faster Travis CI tests with Docker cache
date: 2017-08-07 11:11
comments: true
Tags: fedora.planet, QA

For a while now I've been running tests on Travis CI using Docker
containers to build the project and execute the tests inside. In this
post I will explain how to speed up execution times.

A Docker image is a filesystem snapshot similar to a virtual machine
image. From these images we build containers (e.g. we run the container X
from the image Y). The construction of Docker images is controlled via
`Dockerfile` which contains a set of instructions how to build the image.
For example:

    FROM welder/web-nodejs:latest
    MAINTAINER Brian C. Lane <bcl@redhat.com>
    RUN dnf install -y nginx
    
    CMD nginx -g "daemon off;"
    EXPOSE 3000
    
    ## Do the things more likely to change below here. ##
    
    COPY ./docker/nginx.conf /etc/nginx/
    
    # Update node dependencies only if they have changed
    COPY ./package.json /welder/package.json
    RUN cd /welder/ && npm install
    
    # Copy the rest of the UI files over and compile them
    COPY . /welder/
    RUN cd /welder/ && node run build
    
    COPY entrypoint.sh /usr/local/bin/entrypoint.sh
    ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]


`docker build` is smart enough to actually build intermediate layers for each
command and store them on your computer. Each command is hashed and it is rebuilt
only if it has been changed. Thus the stuff which doesn't change often goes first
(like setting up a web server or a DB) and the stuff that changes (like the project source code)
goes at the end. All of this is beautifully explained by [Stefan Kanev in
this video](https://www.youtube.com/watch?v=3a0gVrfmWC8) (in Bulgarian).

Travis and Docker
-----------------

While intermediate layer caching is a standard feature for Docker it is disabled
by default in Travis CI and any other CI service I was able to find. To be frank
Circles CI offer this as a premium feature but their pricing plans on that aren't
clear at all.

However you can enable the use of caching following a few simple steps:

1. Make your Docker images publicly available (e.g. Docker Hub or Amazon EC2 Container Service)
2. Before starting the test job do a `docker pull my/image:latest`
3. When building your Docker images in Travis add `--cache-from my/image:latest` to `docker build`
4. After successful execution `docker tag` the latest image with the build job number and
   `docker push` it again to the hub!

**NOTES:**

- Everything you do will become public so take care not to expose internal code.
  Alternatively you may configure a private docker registry (e.g. Amazon EC2 CS)
  and use encrypted passwords for Travis to access your images;
- `docker pull` will download all layers that it needs. If your hosting is slow
  this will negatively impact execution times;
- `docker push` will upload only the layers that have been changed;
- I only push images coming from the master branch which are not from a pull request
  build job. This prevents me from accidentally messing something up.


If you examine the logs of [Job #247.4](https://travis-ci.org/weldr/welder-web/jobs/260970675)
and [Job #254.4](https://travis-ci.org/weldr/welder-web/jobs/261732264) you will notice
that almost all intermediate layers were re-used from cache:

    Step 3/12 : RUN dnf install -y nginx
     ---> Using cache
     ---> 25311f052381
    Step 4/12 : CMD nginx -g "daemon off;"
     ---> Using cache
     ---> 858606811c85
    Step 5/12 : EXPOSE 3000
     ---> Using cache
     ---> d778cbbe0758
    Step 6/12 : COPY ./docker/nginx.conf /etc/nginx/
     ---> Using cache
     ---> 56bfa3fa4741
    Step 7/12 : COPY ./package.json /welder/package.json
     ---> Using cache
     ---> 929f20da0fc1
    Step 8/12 : RUN cd /welder/ && npm install
     ---> Using cache
     ---> 68a30a4aa5c6

Here the slowest operations are `dnf install` and `npm install` which on normal execution
will take around 5 minutes.

You can check-out my
[.travis.yml](https://github.com/weldr/welder-web/blob/master/.travis.yml) for more info.

First time cache
----------------

It is important to note that you need to have your docker images available in the
registry before you execute the first `docker pull` from CI. I do this by manually building
the images on my computer and uploading them before configuring CI integration. Afterwards
the CI system takes care of updating the images for me.

Initially you may not notice a significant improvement as seen in
[Job #262](https://travis-ci.org/weldr/bdcs-api-rs/builds/261510313), Step 18/22.
The initial image available on Docker Hub has all the build dependencies installed
and the code has not been changed when job #262 was executed.

The `COPY` command copies the entire contents of the directory, including filesystem metadata!
Things like uid/gid (file ownership), timestamps (not sure if taken into account)
and/or extended attributes (e.g. SELinux)
will cause the intermediate layers checksums to differ even though the actual
source code didn't change. This will resolve itself once your CI system starts automatically
pushing the latest images to the registry.




Thanks for reading and happy testing!
