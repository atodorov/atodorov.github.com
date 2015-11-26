#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alexander Todorov'
SITENAME = 'atodorov.org'
SITESUBTITLE = u'you can logoff, but you can never leave'
SITEURL = 'http://localhost:8000'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

TAG_URL = 'blog/categories/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

MD_EXTENSIONS = ['codehilite', 'extra', 'nlbqx.nlbqx', 'nlcx.nlcx']

# static paths will be copied under the same name
STATIC_PATHS = ["images/", 'robots.txt', 'favicon.png', 'CNAME', 'override.css']

HEADER_COVER = "/images/header_02.jpg"

# the theme hijacks the form input fields
# and the search box doesn't work
DISABLE_CUSTOM_THEME_JAVASCRIPT = True

COLOR_SCHEME_CSS = "github.css"
CSS_OVERRIDE = "override.css"

PATH = 'content'

TIMEZONE = 'Europe/Sofia'

DEFAULT_LANG = u'en'
LOCALE = 'en_US.UTF-8'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../pelican-clean-blog'

TWITTER_USERNAME = "atodorov_"
TWITTER_URL = "https://twitter.com/%s" % TWITTER_USERNAME
GITHUB_URL = "https://github.com/atodorov"

ADDTHIS_PUBID = "ra-5103cc5a2bc6ba17"
FEEDBURNER_URL = "http://feeds.feedburner.com/atodorov"
