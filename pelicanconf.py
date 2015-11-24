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

# static paths will be copied under the same name
STATIC_PATHS = ["images/", 'robots.txt', 'favicon.png', 'CNAME', 'override.css']

HEADER_COVER = "/images/bricks.jpg"

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

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../pelican-clean-blog'

DISQUS_SITENAME = "atodorov"
TWITTER_USERNAME = "atodorov_"
TWITTER_URL = "https://twitter.com/%s" % TWITTER_USERNAME
GITHUB_URL = "https://github.com/atodorov"