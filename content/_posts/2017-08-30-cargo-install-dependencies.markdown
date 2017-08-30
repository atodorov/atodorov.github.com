Title: Speeding up Rust builds inside Docker
Headline: aka cargo build --deps-only
date: 2017-08-30 09:00
comments: true
Tags: fedora.planet, QA
og_image: images/cargo-containers.jpg
twitter_image: images/cargo-containers.jpg


Currently [it is not possible](https://github.com/rust-lang/cargo/pull/3567)
to instruct `cargo`, the Rust package manager, to build only the dependencies
of the software you are compiling! This means you can't easily pre-install
build dependencies. Luckily you can workaround this with `cargo build -p`!
I've been using this Python script to parse `Cargo.toml`:

    :::python parse-cargo-toml.py
    #!/usr/bin/env python
    
    from __future__ import print_function
    
    import os
    import toml
    
    _pwd = os.path.dirname(os.path.abspath(__file__))
    cargo = toml.loads(open(os.path.join(_pwd, 'Cargo.toml'), 'r').read())
    
    for section in ['dependencies', 'dev-dependencies']:
        for dep, version in cargo[section].items():
            print('cargo build -p %s' % dep)
    

and then inside my `Dockerfile`:

    RUN mkdir /bdcs-api-rs/
    COPY parse-cargo-toml.py /bdcs-api-rs/
    
    # Manually install cargo dependencies before building
    # so we can have a reusable intermediate container.
    # This workaround is needed until cargo can do this by itself:
    # https://github.com/rust-lang/cargo/issues/2644
    # https://github.com/rust-lang/cargo/pull/3567
    COPY Cargo.toml /bdcs-api-rs/
    WORKDIR /bdcs-api-rs/
    RUN python ./parse-cargo-toml.py | while read cmd; do \
            $cmd;                                    \
        done


It doesn't take into account the version constraints specified in `Cargo.toml` but
is still able to produce an intermediate docker layer which I can use to
[speed-up my tests by caching the dependency compilation part]({filename}2017-08-07-faster-travis-docker-cache.markdown).

As seen in the [build log](https://travis-ci.org/weldr/bdcs-api-rs/builds/268489460#L1173),
lines 1173-1182, when doing `cargo build` it downloads and compiles `chrono v0.3.0` and
`toml v0.3.2`. The rest of the dependencies are already available. The logs also show
that after Job #285 the build times dropped from 16 minutes down to 3-4 minutes due to
Docker caching. This would be even less if the cache is kept locally!


Thanks for reading and happy testing!
