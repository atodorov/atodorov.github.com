#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://atodorov.org'
RELATIVE_URLS = False

FEED_ALL_ATOM = "atom.xml"
FEED_MAX_ITEMS = DEFAULT_PAGINATION
TAG_FEED_ATOM = TAG_URL.replace('{slug}', "%s") + 'atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "atodorov"
GOOGLE_ANALYTICS = "UA-37979549-1"
GOOGLE_SITE_VERIFICATION = "XynqZtldWNBbmsynVQZremIxaaO8Wgs6AGR8UZ7KIkM"
LUCKY_ORANGE_ID = "55936"
