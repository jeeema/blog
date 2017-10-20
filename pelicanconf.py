#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# General ---------------------------------------------------------------------------------------------------------------
AUTHOR = 'jeeema'
SITENAME = 'MATH, SCIENCE, COMPUTER'
SITEURL = ''

#Uncomment this if you want document-relative URLs when developing
#RELATIVE_URLS = True

PATH = 'content'
STATIC_PATHS = ['images']

DEFAULT_METADATA = {'status': 'draft'}

TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE = 'fs'

DEFAULT_LANG = 'ja'

USE_FOLDER_AS_CATEGORY = True

#(This may not be reflected on some templates)
DISPLAY_CATEGORIES_ON_MENU = True

#Pages in content/pages are displayed in the primary navigation menu.(This may not be reflected on some templates)
#To exclude any contents in pages directory, add ':status: hidden' as metadata.
DISPLAY_PAGES_ON = True

DEFAULT_PAGINATION = False

#Set this to False when changed settings are not reflected
LOAD_CONTENT_CACHE = True

# Pygments configuration ------------------------------------------------------------------------------------------------

#Default settings of Pygments automatically applied to every code block
PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}


# Feed generation is usually not desired when developing ----------------------------------------------------------------
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll --------------------------------------------------------------------------------------------------------------
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget ---------------------------------------------------------------------------------------------------------
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
