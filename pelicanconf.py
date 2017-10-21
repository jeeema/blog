#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#Ref:docs.getpelican.com/en/latest/settings.html

from __future__ import unicode_literals

# METADATA ==============================================================================================================

AUTHOR = 'jeeema'
SITENAME = "jeeema's log"

DEFAULT_METADATA = {'status': 'draft'}

DEFAULT_LANG = 'ja'

USE_FOLDER_AS_CATEGORY = True

# APPEARANCE ============================================================================================================

#(This may not be reflected on some templates)
DISPLAY_CATEGORIES_ON_MENU = True
#Pages in content/pages are displayed in the primary navigation menu.(This may not be reflected on some templates)
#To exclude any contents in pages directory, add ':status: hidden' as metadata.
DISPLAY_PAGES_ON = True

SUMMARY_MAX_LENGTH = 50

# Pagination
DEFAULT_PAGINATION = True
DEFAULT_ORPHANS = 0

# Order of content
NEWEST_FIRST_ARCHIVES = True
REVERSE_CATEGORY_ORDER = False
ARTICLE_ORDER_BY = 'reversed-date'
PAGES_ORDER_BY = 'basename'

#Default settings of Pygments automatically applied to every reST code block.
PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}

# PATHS & URLs ==========================================================================================================

PATH = 'content'
OUTPUT_PATH  = 'output/'

PAGE_PATHS = ['pages/']
ARTICLE_PATHS = ['articles/']
STATIC_PATHS = ['images']

IGNORE_FILES = [ '.git', '__pycache__', '.#*']
#Files that shouldn't be deleted from the output directory.
OUTPUT_RETENTION = ['.git']

CACHE_CONTENT = True
CACHE_PATH = 'cache'
#Set this to False when changed settings are not reflected
LOAD_CONTENT_CACHE = True

SITEURL = ''
#Set this to true if you want document-relative URLs when developing
RELATIVE_URLS = True

SLUGIFY_SOURCE = 'basename'

# FEED ==================================================================================================================

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# TIME & DATE ===========================================================================================================

TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE = 'fs'

# BLOGROLL ==============================================================================================================

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# SOCIAL WIDGET =========================================================================================================

SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
