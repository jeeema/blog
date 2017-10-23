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
#Alphabetically
REVERSE_CATEGORY_ORDER = False
#The newest article comes first.
ARTICLE_ORDER_BY = 'reversed-date'
#Alphabetically
PAGES_ORDER_BY = 'basename'

# Theme
THEME = 'pelican-themes/nice-blog'
#Destination directory in OUTPUT_PATH where Pelican will place the files collected from THEME_STATIC_PATHS.
THEME_STATIC_DIR ='theme'
#A list of static theme paths to be copied
THEME_STATIC_PATHS = ['static']

#Default settings of Pygments automatically applied to every reST code block
PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}

# PATHS & URLs ==========================================================================================================

SITEURL = 'https://jeeema.netlify.com'
#Set this to true if you want document-relative URLs when developing.
RELATIVE_URLS = True
#Uses articles' file names to create their slugs without prepending their paths.
SLUGIFY_SOURCE = 'basename'
PATH = 'content'
OUTPUT_PATH  = 'output/'
#If set to True, copies the content sources to OUTPUT_PATH.
OUTPUT_SOURCES = False
IGNORE_FILES = ['.git', '__pycache__', '.#*']
DELETE_OUTPUT_DIRECTORY = True
#Files that shouldn't be deleted from OUTPUT_PATH
OUTPUT_RETENTION = ['.git']

STATIC_PATHS = ['images']
#If this is set to False, content source files found in STATIC_PATHS wil be copied in addition to static files.
STATIC_EXCLUDE_SOURCES = True
#If set to True, creates hard(when the content and output directories are on the same device) or sym(otherwise) links to files instead of copying them.
CREATE_STATIC_LINKS = False
#If set to True, and CREATE_STATIC_LINKS is False, copies only newer files than the ones existing in output directory by comparing mtimes of each of them.
STATIC_CHECK_IF_MODIFIED = True

CACHE_CONTENT = True
CACHE_PATH = 'cache'
#To ignore and regenrate the whole cache so that the modifications to the settings will be reflected without fail, disable this or pass the '--ignore-cache' option to Pelican.
LOAD_CONTENT_CACHE = True
#If there are any mods to the settings file, ignores the cache automatically when Pelican is running in autoreload mode.
AUTORELOAD_IGNORE_CACHE = True
#'reader': caches the raw content and metadata returned by a reader
#'generator': caches the processed content (faster than reader). But this may conflict with some plugins and WITH_FUTURE_DATES.
CONTENT_CACHING_LAYER = 'reader'
#Controls how files are checked for mods.
#Another way to check for mods is to use the hashlib module, which is more reliable than mtime.
#Note that even when the cache is used, all the output is always written, so the mtime of each generated HTML file will always change.
CHECK_MODIFIED_METHOD = 'mtime'
#If this list if not empty, only output files with their paths in this are written. The paths can be specified using '--write-selected' option, which acceptsa comma-seperated list of multiple output paths.
WRITE_SELECTED = []

ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = 'articles/{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_LANG_SAVE_AS = 'articles/{category}/{slug}.html'
ARTICLE_LANG_URL = '{lang}/{category}/{slug}.html'

DRAFT_SAVE_AS = 'drafts/{category}/{slug}.html'
DRAFT_URL = 'drafts/{category}/{slug}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{category}/{slug}.html'
DRAFT_LANG_URL = '{lang}/drafts/{category}/{slug}.html'

PAGE_PATHS = ['pages']
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = '{lang}/{slug}.html'

# TIME & DATE ===========================================================================================================

TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
#If set to False, content with dates in the future will get a default status of `draft`.
WITH_FUTURE_DATES = False

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
