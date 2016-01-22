#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
from pelican.settings import DEFAULT_CONFIG

def build_url(label, base, end):
    from markdown.extensions import wikilinks

    u = {
        'MacBook'     : 'http://amzn.to/1RdviyD',
        'MacBook Air' : 'http://amzn.to/1RdviyD',
        'Tradeo' : 'http://tradeo.com',
    }

    if u.has_key(label):
        return u[label]
    else:
        return wikilinks.build_url(label, base, end)


AUTHOR = u'Alexander Todorov'
SITENAME = 'atodorov.org'
SITESUBTITLE = u'you can logoff, but you can never leave'
SHOW_SITESUBTITLE_IN_HTML = True
SITEURL = 'http://localhost:8000'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

TAG_URL = 'blog/categories/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

# prepare for the change in
# https://github.com/getpelican/pelican/pull/1638
# expected in Pelican 3.7
if type(DEFAULT_CONFIG['MD_EXTENSIONS']) == dict:
    MD_EXTENSIONS = {}
    MD_EXTENSIONS.update(DEFAULT_CONFIG['MD_EXTENSIONS'])
    MD_EXTENSIONS.update({
            'markdown.extensions.wikilinks' : {
                'build_url' : build_url,
            },
            'nlbqx.nlbqx': {},
            'nlcx.nlcx' : {},
            'mdbz.rhbz' : {},
        })
else:
    MD_EXTENSIONS = []
    MD_EXTENSIONS += DEFAULT_CONFIG['MD_EXTENSIONS']
    MD_EXTENSIONS += ['wikilinks', 'nlbqx.nlbqx', 'nlcx.nlcx', 'mdbz.rhbz']
    MD_EXTENSION_CONFIGS = {
        'wikilinks' : {
            'build_url' : build_url,
        }
    }

# static paths will be copied under the same name
STATIC_PATHS = ["images/", 'robots.txt', 'favicon.png', 'CNAME', 'override.css']

HEADER_COVER = "/images/header_02.jpg"

# the theme hijacks the form input fields
# and the search box doesn't work
DISABLE_CUSTOM_THEME_JAVASCRIPT = True

SHOW_FULL_ARTICLE = True

COLOR_SCHEME_CSS = "github.css"
CSS_OVERRIDE = "override.css"

PATH = 'content'

FOOTER_INCLUDE = "myfooter.html"
EXTRA_TEMPLATES_PATHS = [os.path.join(os.path.dirname(__file__), PATH)]

TIMEZONE = 'Europe/Sofia'

DEFAULT_LANG = u'en'
LOCALE = 'en_US'

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
LINKEDIN_URL = "https://bg.linkedin.com/in/alextodorov"

SOCIAL = (
            ('twitter',  TWITTER_URL),
            ('github',   GITHUB_URL),
            ('linkedin', LINKEDIN_URL),
        )


ADDTHIS_PUBID = "ra-5103cc5a2bc6ba17"
FEEDBURNER_URL = "http://feeds.feedburner.com/atodorov"
