# Django settings for ajax_tut project.
import os
ROOT_PATH = os.path.dirname(__file__)

DEBUG =True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

## Changed
DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
## Changed
DATABASE_NAME = os.path.join(ROOT_PATH, 'notes.sqlite')

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True

## Changed
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')
#IMAGE_ROOT = os.path.join(ROOT_PATH, 'image/')
#MEDIA_ROOT='media'
## Changed
MEDIA_URL = 'http:/instasaic.com/media/'

## Changed but irrelevant
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^yyde2(soo^!3@5l7outx*&yu-i-0bz+4sm)0#mr6fz1js9=t@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'insta.urls'

TEMPLATE_DIRS = (
    ## Changed
    os.path.join(ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    ## changed
    'notes',
)
FLICKR_API_KEY='661a212bc7c6752f86e71ddd309265fb'
FLICKR_API_SECRET='974c8599dfaa285d'

