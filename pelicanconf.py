#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# import pelican_ga_pageview, pelican_cite_nice
# import hrk_theme

AUTHOR = 'Harper Kennington'
SITENAME = 'Harper Kennington'
COPYRIGHT = AUTHOR
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# FEED_ALL_ATOM = None
# AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
FA_SOCIAL = (
    # ('beaker', 'https://www.researchgate.net/profile/James_Kennington'),
)

SOCIAL = (
    ('github', 'https://github.com/HRKennington'),
    ('linkedin', 'https://www.linkedin.com/in/harper-kennington-78170a75/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme control
THEME = '/Users/jim/repos/professional/hrk-theme/hrk_theme' # hrk_theme.THEME_PATH

# Static home page
INDEX_SAVE_AS = 'blog.html'
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'


# CONTOL menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Blog','/blog'),
    ('CV','/pages/cv'),
    ('Publications','/pages/publications'),
    ('Research','/pages/research'),
)

BLOG_PAGE_IMAGE_HEADER = '../images/nyc.png'
ARTICLE_PAGE_IMAGE_HEADER = '../' + BLOG_PAGE_IMAGE_HEADER
SIDEBAR_DISPLAY = ['categories', 'tags']

PLUGIN_PATHS=[
    '/Users/jim/repos/professional/pelican-cite-nice',
    '/Users/jim/repos/professional/pelican-ga-pageview',
]

PLUGINS = [
    'pelican_cite_nice',
    # 'pelican_ga_pageview',
]

LOAD_CONTENT_CACHE = False

MATH_JAX = {'color':'blue'}

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DISQUS_SITENAME = 'hrkennington'
DISQUS_SITEURL = 'hrkennington.com'

# GOOGLE ANALYTICS
# GOOGLE_ANALYTICS = 'UA-135655259-1'
# GOOGLE_SERVICE_ACCOUNT = 'sitetracker@high-unity-233520.iam.gserviceaccount.com'
# GOOGLE_KEY_FILE = './client_private.p12'
# GA_START_DATE = '2019-01-01'
# GA_END_DATE = 'today'
# GA_METRIC = 'ga:pageviews'

# CITATIONS
PUBLICATIONS_SRC = 'content/references.bib'
