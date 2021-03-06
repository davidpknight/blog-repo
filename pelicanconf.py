#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'david knight'
SITENAME = u'davidknight'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/davepknight'),
          ('linkedin', 'https://au.linkedin.com/in/davidknightplanner'),)
          

DEFAULT_PAGINATION = 10

THEME = 'pelican-bootstrap3-master'
BOOTSTRAP_THEME = 'simplex'

AVATAR = './images/david-knight-hs.jpg'

BANNER = './images/urbanplanbanner.png'

TWITTER_USERNAME = 'davepknight'
TWITTER_WIDGET_ID = 'https://twitter.com/settings/widgets/718741304658669568/edit'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
