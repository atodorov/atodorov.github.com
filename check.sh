#!/bin/bash

pushd ../pelican-clean-blog/
BRANCH=`git branch | grep "* " | cut -f2 -d" "`

if [ "$BRANCH" != "atodorov.org" ]; then
    popd
    echo "ERROR: Theme is not on the atodorov.org branch"
    exit 1
fi

STATUS=`git status -s`
if [ -n "$STATUS" ]; then
    git status
    popd
    exit 2
fi



popd
