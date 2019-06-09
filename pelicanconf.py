#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Robert Callicotte'
SITENAME = 'robbyc.io'
SITEURL = ''

PATH = 'content'
THEME = 'pelican-svbhack'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/c4t3l'),
          ('Twitter', 'https://twitter.com/robbycl2v'),
          ('Email', 'mailto:rcallicotte@gmail.com'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# svbhack settings
DISPLAY_CATEGORIES_ON_MENU = False
USER_LOGO_URL = SITEURL + '/images/me-guitar.jpg'
ROUND_USER_LOGO = False
TAGLINE = '♫♩♪♪♪♪♫'

