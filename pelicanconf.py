#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#Ref:docs.getpelican.com/en/latest/settings.html(Some of the descriptions below are from here.)

from __future__ import unicode_literals

# METADATA ==============================================================================================================

AUTHOR = 'jeeema'
SITENAME = "jeeema's log"

DEFAULT_METADATA = {'status': 'draft'}

DEFAULT_LANG = 'ja'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'

# APPEARANCE ============================================================================================================

#(This may not be reflected on some templates)
DISPLAY_CATEGORIES_ON_MENU = True
#Pages in content/pages are displayed in the primary navigation menu.(This may not be reflected on some templates)
#To exclude any contents in pages directory, add ':status: hidden' as metadata.
DISPLAY_PAGES_ON = True

SUMMARY_MAX_LENGTH = 64

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

SITEURL = 'https://jeeema.netlify.com'
#Set this to true if you want document-relative URLs when developing
RELATIVE_URLS = True
#Use articles' file names to create their slugs without prepending their paths.
SLUGIFY_SOURCE = 'basename'
PATH = 'content'
OUTPUT_PATH  = 'output/'
#By setting this to True, the sources will be copied to OUTPUT_PATH
OUTPUT_SOURCES = False
IGNORE_FILES = ['.git', '__pycache__', '.#*']
#Files that shouldn't be deleted from the output directory.
OUTPUT_RETENTION = ['.git']

STATIC_PATHS = ['images']
#If set to true, creates hard(when the content and output directories are on the same device) or sym(otherwise) links to files instead of copying them
CREATE_STATIC_LINKS = False
#If set to True, and CREATE_STATIC_LINKS is False, copies only newer files than the files existing in output directory by comparing mtimes of each of them.
STATIC_CHECK_IF_MODIFIED = True

CACHE_CONTENT = True
CACHE_PATH = 'cache'
#'reader': caches the raw content and metadata returned by a reader
#'generator': caches the processed content. *This may conflict with some plugins and WITH_FUTURE_DATES*
#Controls how files are checked for modifications
CHECK_MODIFIED_METHOD = 'mtime'
#Set this to False when changed settings are not reflected
LOAD_CONTENT_CACHE = True

ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = 'articles/{category}/{lang}/{slug}.html'
ARTICLE_URL = '{category}/{lang}/{slug}.html'
ARTICLE_LANG_SAVE_AS = 'articles/{category}/{lang}/{slug}.html'
ARTICLE_LANG_URL = '{category}/{lang}/{slug}.html'

DRAFT_SAVE_AS = 'drafts/{category}/{lang}/{slug}.html'
DRAFT_URL = 'drafts/{category}/{lang}/{slug}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{category}/{lang}/{slug}.html'
DRAFT_LANG_URL = 'drafts/{category}/{lang}/{slug}.html'

PAGE_PATHS = ['pages']
PAGE_SAVE_AS = 'pages/{lang}/{slug}.html'
PAGE_URL = '{lang}/{slug}.html'
PAGE_LANG_SAVE_AS = 'pages/{lang}/{slug}.html'
PAGE_LANG_URL = '{lang}/{slug}.html'

ARTICLE_SAVE_AS = 'articles/{category}/{lang}/{slug}.html'
ARTICLE_URL = '{category}/{lang}/{slug}.html'
ARTICLE_LANG_SAVE_AS = 'articles/{category}/{lang}/{slug}.html'
ARTICLE_LANG_URL = '{category}/{lang}/{slug}.html'

# TIME & DATE ===========================================================================================================

TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'

# FEED ==================================================================================================================

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# BLOGROLL ==============================================================================================================

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# SOCIAL WIDGET =========================================================================================================

SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
