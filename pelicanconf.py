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

    if label in u:
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

MARKDOWN = DEFAULT_CONFIG['MARKDOWN'].copy()
MARKDOWN['extension_configs'].update({
        'markdown.extensions.wikilinks' : {
            'build_url' : build_url,
        },
        'nlbqx.nlbqx': {},
        'nlcx.nlcx' : {},
    })

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
IGNORE_FILES = [FOOTER_INCLUDE]
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

ADDTHIS_PUBID = "ra-5103cc5a2bc6ba17"

SOCIAL = (
            ('twitter',  "https://twitter.com/atodorov_"),
            ('github',   "https://github.com/atodorov"),
            ('linkedin', "https://bg.linkedin.com/in/alextodorov"),
            ('rss',      "http://feeds.feedburner.com/atodorov"),
            ('youtube', "https://www.youtube.com/playlist?list=PLFjlI7p-h1hxBP3cIjEqePSeoBDHud5Db"),
            ('amazon',   "https://amzn.to/4dKB8VJ"),
            ('user-secret', "http://mrsenko.com/?utm_source=atodorov.org&utm_medium=blog&utm_campaign=social_icon"),
        )

SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True

FACEBOOK_ADMINS = ['1616937247']

MENUITEMS = (
    ("Pylint Workshop", "http://mrsenko.com/pylint-workshop/"),
)
