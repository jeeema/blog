#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#Ref:docs.getpelican.com/en/latest/settings.html

from __future__ import unicode_literals

AUTHOR = 'jeeema'
SITENAME = "jeeema's log"
SITEURL = ''

DEFAULT_METADATA = {'status': 'draft'}

DEFAULT_LANG = 'ja'

USE_FOLDER_AS_CATEGORY = True
#(This may not be reflected on some templates)
DISPLAY_CATEGORIES_ON_MENU = True
#Pages in content/pages are displayed in the primary navigation menu.(This may not be reflected on some templates)
#To exclude any contents in pages directory, add ':status: hidden' as metadata.
DISPLAY_PAGES_ON = True

SUMMARY_MAX_LENGTH = 50

DEFAULT_PAGINATION = True


#Default settings of Pygments automatically applied to reST every code block.
PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}

# Paths & URLs ----------------------------------------------------------------------------------------------------------

PATH = 'content/'
OUTPUT_PATH  = 'output/'

PAGE_PATHS = ['pages/']
ARTICLE_PATHS = ['articles/']
STATIC_PATHS = ['images']

IGNORE_FILES = ['.git', '__pycache__']
#Files that shouldn't be deleted from the output directory.
OUTPUT_RETENTION = {'.git'}

CACHE_CONTENT = True
CACHE_PATH = 'cache'
#Set this to False when changed settings are not reflected
LOAD_CONTENT_CACHE = True

SLUGIFY_SOURCE = 'basename'

#Uncomment this if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Feed generation is usually not desired when developing ----------------------------------------------------------------

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Time & Date -----------------------------------------------------------------------------------------------------------

TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE = 'fs'

# Blogroll --------------------------------------------------------------------------------------------------------------
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget ---------------------------------------------------------------------------------------------------------
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
