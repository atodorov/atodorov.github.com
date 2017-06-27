Title: Producing coverage report for Haskell binaries
Headline: and integration with Coveralls.io
date: 2017-06-27 10:00
comments: true
Tags: fedora.planet, QA

Recently I've started testing a Haskell application and a question I find
unanswered (or at least very poorly documented) is how to produce coverage
reports for binaries ?

Understanding HPC & cabal
-------------------------

`hpc` is the Haskell code coverage tool. It produces the following files:

* .mix - module index file, contains information about *tick boxes* - their type
  and location in the source code;
* .tix - tick index file aka coverage report;
* .pix - program index file, used only by `hpc trans`.

The invocation to `hpc report` needs to know where to find the .mix files in order
to be able to translate the coverage information back to source and it needs to
know the location (full path or relative from pwd) to the tix file we want to
report.


`cabal` is the package management tool for Haskell. Among other thing it can be used
to build your code, execute the test suite and produce the coverage report for you.
`cabal build` will produce module information in `dist/hpc/vanilla/mix` and
`cabal test` will store coverage information in `dist/hpc/vanilla/tix`!

A particular thing about Haskell is that you can only test code which can be
`import`ed, e.g. it is a library module. You can't test (via Hspec or Hunit) code which
lives inside a file that produces a binary (e.g. Main.hs). However you can still
execute these binaries (e.g. invoke them from the shell) and they will produce a
coverage report in the current directory (e.g. main.tix).


Putting everything together
---------------------------

1. Using `cabal build` and `cabal test` build the project and execute your unit tests.
   This will create the necessary .mix files (including ones for binaries) and .tix
   files coming from unit testing;
2. Invoke your binaries passing appropriate data and examining the results (e.g. compare
   the output to a known value). A simple shell or Python script could do the job;
3. Copy the `binary.tix` file under `dist/hpc/vanilla/binary/binary.tix`!


Produce coverage report with hpc:

    hpc markup --hpcdir=dist/hpc/vanilla/mix/lib --hpcdir=dist/hpc/vanilla/mix/binary  dist/hpc/vanilla/tix/binary/binary.tix

Convert the coverage report to JSON and send it to Coveralls.io:

    cabal install hpc-coveralls
    ~/.cabal/bin/hpc-coveralls --display-report tests binary

Example
-------

Check out the [haskell-rpm](https://github.com/weldr/haskell-rpm/pull/18) repository
for an example. See [job #45](https://coveralls.io/builds/12131112) where there is now
coverage for the `inspect.hs`, `unrpm.hs` and `rpm2json.hs` files, producing binary executables.
Also notice that in
[RPM/Parse.hs](https://coveralls.io/builds/12131112/source?filename=.%2FRPM%2FParse.hs)
the function `parseRPMC` is now covered, while it was not covered in the
[previous job #42](https://coveralls.io/builds/12102486/source?filename=.%2FRPM%2FParse.hs)!

    :::yaml .travis.yml snippet
    script:
      - ~/.cabal/bin/hlint .
      - cabal install --dependencies-only --enable-tests
      - cabal configure --enable-tests --enable-coverage --ghc-option=-DTEST
      - cabal build
      - cabal test --show-details=always
    
      # tests to produce coverage for binaries
      - wget https://s3.amazonaws.com/atodorov/rpms/macbook/el7/x86_64/efivar-0.14-1.el7.x86_64.rpm
      - ./tests/test_binaries.sh ./efivar-0.14-1.el7.x86_64.rpm
    
      # move .tix files in appropriate directories
      - mkdir ./dist/hpc/vanilla/tix/inspect/ ./dist/hpc/vanilla/tix/unrpm/ ./dist/hpc/vanilla/tix/rpm2json/
      - mv inspect.tix ./dist/hpc/vanilla/tix/inspect/
      - mv rpm2json.tix ./dist/hpc/vanilla/tix/rpm2json/
      - mv unrpm.tix ./dist/hpc/vanilla/tix/unrpm/
    
    after_success:
      - cabal install hpc-coveralls
      - ~/.cabal/bin/hpc-coveralls --display-report tests inspect rpm2json unrpm


Thanks for reading and happy testing!
