# Django settings for cakeshop project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

# Absolute path to the directory of this file (settings.py)
import os
<<<<<<< HEAD
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
=======
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
>>>>>>> e7b3e983fdde1af8b66d44db66c381a26aa829b8

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ssdb',                      # Or path to database file if using sqlite3.
        'USER': 'ssdbuser',                      # Not used with sqlite3.
        'PASSWORD': 'ssdbuserpwd',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
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
TIME_ZONE = 'Asia/Calcutta'

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

<<<<<<< HEAD
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''
=======
LOGIN_URL = "/adminlogin/"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT,'media')
>>>>>>> e7b3e983fdde1af8b66d44db66c381a26aa829b8

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
<<<<<<< HEAD
MEDIA_URL = ''
=======
MEDIA_URL = '/media/'
>>>>>>> e7b3e983fdde1af8b66d44db66c381a26aa829b8

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
<<<<<<< HEAD
STATIC_ROOT = os.path.join(PROJECT_PATH, 'sitestatic')
=======
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'sitestatic')
>>>>>>> e7b3e983fdde1af8b66d44db66c381a26aa829b8

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
<<<<<<< HEAD
    os.path.join(PROJECT_PATH, 'static'),
=======
    os.path.join(PROJECT_ROOT, 'static'),
>>>>>>> e7b3e983fdde1af8b66d44db66c381a26aa829b8
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

<<<<<<< HEAD
# Make this unique, and don't share it with anybody.
SECRET_KEY = '7w0+0n%)w62iuz9apih!vubugppv+9nf3y911h^-p&^coh0$)l'
=======
#FILE_UPLOAD_HANDLERS = (
#    'django.core.files.uploadhandler.MemoryFileUploadHandler',
#    'django.core.files.uploadhandler.TemporaryFileUploadHandler'
#)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'okeij2uz-4v=t*=&ch*)o5)ljnwus6%vq_8d(@a7_ah02+2k*n'
>>>>>>> e7b3e983fdde1af8b66d44db66c381a26aa829b8

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
<<<<<<< HEAD
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
=======
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
>>>>>>> e7b3e983fdde1af8b66d44db66c381a26aa829b8
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'cakeshop.urls'

WSGI_APPLICATION = 'cakeshop.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
<<<<<<< HEAD
    os.path.join(PROJECT_PATH, 'templates')
=======
    os.path.join(PROJECT_ROOT, 'templates'),
>>>>>>> e7b3e983fdde1af8b66d44db66c381a26aa829b8
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
<<<<<<< HEAD
    'django.contrib.staticfiles',
    'cakeshop.apps.admin'
=======
    'django.contrib.staticfiles',  
    'cakeshop.apps.admin',
    'cakeshop.apps.client',
    'cakeshop.csmodels',
    'cakeshop.services',
>>>>>>> e7b3e983fdde1af8b66d44db66c381a26aa829b8
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
