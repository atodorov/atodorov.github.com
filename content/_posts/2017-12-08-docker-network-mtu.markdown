Title: How to configure MTU for the Docker network
date: 2017-12-08 16:02
comments: true
Tags: fedora.planet

On one of my Jenkins slaves I've been experiencing problems when downloading
files from the network. In particular with `cabal update` which fetches data
from hackage.haskell.org. As suggested by David Roble the problem and solution
lies in the MTU configured for the default `docker0` interface!

By default `docker0` had MTU of `1500` which should be lower than the
host `eth0` MTU of 1400! To configure this before the docker daemon is started
place any non-default settings in `/etc/docker/daemon.json`! For more information
head to
<https://docs.docker.com/engine/userguide/networking/default_network/custom-docker0/>.


Thanks for reading and happy testing!
