# Django settings for SKHReservationSystem project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sqlite3',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
import os
dirnames = os.path.dirname(globals()["__file__"])
MEDIA_ROOT = os.path.join(os.path.join(dirnames, 'Templates'), "Resources")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/resources/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b6sknjt_*7d+8v#)3@is9=+5h2u@=*fb8j6*o!psdgax7auxq_'

# List of callables that know how to import Templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'SKHReservationSystem.urls'

TEMPLATE_DIRS = (
	os.path.join(dirnames, 'Templates'),
)

FIXTURE_DIRS = (
	os.path.join(dirnames, 'Fixtures'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'SKHReservationSystem.Common',
    'SKHReservationSystem.Parking',
    'SKHReservationSystem.Update',
	'SKHReservationSystem.Sauna',

)

AUTH_PROFILE_MODULE = 'Common.Profile'
EMAILS={
	'staff': 'truongsinh.tran@gmail.com',
	'system': 'truongsinh.tran@gmail.com',
}
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "truongsinh.tran@gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
from itertools import cycle, izip
def decrypt (ss):
    key = cycle(SECRET_KEY)
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(ss, key))
EMAIL_HOST_PASSWORD = decrypt("\x1aYK\x03\x05]\x0c'")
