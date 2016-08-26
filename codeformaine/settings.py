"""
Django settings for our codeformaine project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from datetime import date
import os
import sys
gettext = lambda s: s

from configurations import Configuration, values


class Common(Configuration):

    # You'll likely want to add your own auth model.
    ADMINS =  (
        ('Colin Powell', 'colin.powell@gmail.com'),
    )
    MANAGERS = ADMINS

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, os.path.join(BASE_DIR, 'codeformaine/apps'))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    ALLOWED_HOSTS = ['.codeformaine.org']

    PUBLIC_ROOT = values.Value(os.path.join(BASE_DIR, 'public'))
    STATIC_ROOT = os.path.join(PUBLIC_ROOT.setup('PUBLIC_ROOT'), 'static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "codeformaine/static"),
    )

    MEDIA_ROOT = os.path.join(PUBLIC_ROOT.setup('PUBLIC_ROOT'), 'media')
    MEDIA_URL = "/media/"
    ADMIN_MEDIA_PREFIX = "/static/admin/"

    AWS_ACCESS_KEY_ID=values.Value('thiswontgetyouanywhere')
    AWS_SECRET_ACCESS_KEY=values.Value('thiswontgetyouanywhere')
    AWS_HEADERS = {'ExpiresDefault': 'access plus 30 days',
                   'Cache-Control': 'max-age=86400', }

    DEFAULT_BUCKET_PATH = "cfm-media"
    AWS_DEFAULT_DOMAIN = ""
    AWS_STORAGE_BUCKET_NAME = DEFAULT_BUCKET_PATH

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    DEFAULT_FROM_EMAIL = "Code for Maine <info@codeformaine.org>"
    SERVER_EMAIL = "Code for Maine <info@codeformaine.org>"
    EMAIL_SUBJECT_PREFIX = '[Code for Maine] '
    CONTACT_EMAIL_SUBJECT = "New Message from Code for Maine.org"


    # Application definition

    INSTALLED_APPS = (

        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.admin',
        'django.contrib.staticfiles',
        'django.contrib.redirects',
        'django.contrib.sitemaps',
        'django.contrib.humanize',
        'cms',
        'menus',
        'sekizai',
        'treebeard',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.github',
        'allauth.socialaccount.providers.google',
        'django_extensions',
        'floppyforms',
        'avatar',
        'bootstrap3',
        'markdown_deux',

        'easy_thumbnails',
        'filer',
        'cmsplugin_filer_file',
        'cmsplugin_filer_folder',
        'cmsplugin_filer_image',
        'cmsplugin_filer_teaser',
        'cmsplugin_filer_video',
        'djangocms_picture',
        'djangocms_file',
        'djangocms_link',
        'djangocms_video',
        'djangocms_googlemap',
        'djangocms_snippet',
        'djangocms_text_ckeditor',
        'djangocms_flash',
        'aldryn_search',

        'storages',
        'robots',
        'django_nose',
        'typogrify',
        'brigade',
    )

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [ os.path.join(BASE_DIR, "codeformaine/templates") ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.template.context_processors.request',
                    'django.contrib.messages.context_processors.messages',
                    'sekizai.context_processors.sekizai',
                    'cms.context_processors.cms_settings',
                ],
            },
        },
    ]

    MIDDLEWARE_CLASSES = [
        'cms.middleware.utils.ApphookReloadMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
        'cms.middleware.toolbar.ToolbarMiddleware',
        'cms.middleware.language.LanguageCookieMiddleware',
        'cms.middleware.page.CurrentPageMiddleware',
        'cms.middleware.user.CurrentUserMiddleware',
        'cms.middleware.toolbar.ToolbarMiddleware',
        'cms.middleware.language.LanguageCookieMiddleware',
    ]

    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        #'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        #'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    TEXT_HTML_SANITIZE = False
    CKEDITOR_SETTINGS = {
        'language': '{{ language }}',
        'skin': 'moono',
        'toolbar_CMS': [
                ['Bold', 'Italic', 'Underline', 'Strike'],
                [
                    'NumberedList',
                    'BulletedList',
                    'Outdent',
                    'Indent',
                    '-',
                    'JustifyLeft',
                    'JustifyCenter',
                    'JustifyRight',
                    'JustifyBlock'
                ],
                ['Link', 'Unlink'],
                ['cmsplugins', '-', 'ShowBlocks'],
                ['Styles'],
                ['RemoveFormat', 'Source'],
            ],
    }

    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )
    AUTH_PROFILE_MODULE = 'brigade.Worker'

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "brigade.backends.EmailOrUsernameModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",)

    ROOT_URLCONF = 'codeformaine.urls'

    WSGI_APPLICATION = 'codeformaine.wsgi.application'

    DATABASES = values.DatabaseURLValue('sqlite:///{0}'.format(
        os.path.join(BASE_DIR, 'codeformaine.sqlite3'),
        environ=True))

    NEVERCACHE_KEY = values.Value('Klkjsdfzx*JLSDFLKJSe89230aps=as.sdffslkxvl')

    CACHES = values.CacheURLValue('dummy://')
    # set env variable DJANGO_CACHCES=memcached://127.0.0.1:11211 to use Memcached

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/

    LANGUAGE_CODE = 'en'

    CMS_PERMISSION = True

    CMS_PLACEHOLDER_CONF = {}

    CMS_TEMPLATES = (
        ('default.html', 'Default'),
        ('homepage.html', 'Homepage'),
    )

    CMS_LANGUAGES = {
        ## Customize this
        'default': {
            'public': True,
            'hide_untranslated': False,
            'redirect_on_fallback': True,
        },
        1: [
            {
                'public': True,
                'code': 'en',
                'hide_untranslated': False,
                'name': gettext('en'),
                'redirect_on_fallback': True,
            },
        ],
    }
    BROKER_URL = values.Value('redis://localhost:6379/0')
    CELERY_RESULT_BACKEND=values.Value('djcelery.backends.database:DatabaseBackend')
    CELERY_TIMEZONE = values.Value('UTC')
    CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

    from datetime import timedelta

    CELERYBEAT_SCHEDULE = {
        'check-git-repos': {
            'task': 'honey.tasks.check_git_repos',
            'schedule': timedelta(seconds=60),
            'args': ()
        },
    }


    TIME_ZONE = 'America/New_York'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    SITE_ID = 1

    ALLOWED_HOSTS = values.Value('*')

    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

    PROJECT_DIRNAME = BASE_DIR.split(os.sep)[-1]

    CACHCES='djangopylibmc://127.0.0.1:11211'

    # Account activations automatically expire after this period
    ACCOUNT_ACTIVATION_DAYS = 7

    LOGIN_EXEMPT_URLS = ['', '/',
                         '/accounts/login/',
                         'login',
                         '/accounts/signup/']

    LOGIN_URL = '/accounts/login/'
    LOGIN_REDIRECT_URL = '/dashboard/'
    LOGOUT_URL = '/accounts/logout/'

    TINYMCE_DEFAULT_CONFIG = {
        'theme': "advanced",
        'plugins': "table,paste,pasteword,searchreplace,fullscreen",
        'theme_advanced_buttons1': 'bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect',
        'theme_advanced_buttons2': 'cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor',
        'theme_advanced_buttons3': 'tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,fullscreen',
        'theme_advanced_toolbar_location': "top",
        'theme_advanced_toolbar_align': 'left',
        'theme_advanced_resizing': 'true',
        'theme_advanced_statusbar_location': 'bottom',
        'theme_advanced_resize_horizontal': 'true',
        'height': '380',
        'width': '100%'
    }


    ACCOUNT_ACTIVATION_DAYS = 7

    ALDRYN_SEARCH_REGISTER_APPHOOK = True
    HAYSTACK_ROUTERS = ['aldryn_search.router.LanguageRouter',]
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
            'STORAGE': 'file',
            'POST_LIMIT': 128 * 1024 * 1024,
            'INCLUDE_SPELLING': True,
            'BATCH_SIZE': 100,
        },
    }

    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOG_LEVEL = os.getenv('DJANGO_LOG_LEVEL', 'INFO')
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt' : "%d/%b/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'mail_admins': { 'class': 'django.utils.log.AdminEmailHandler' },
            'console': { 'level': 'DEBUG',
                         'class': 'logging.StreamHandler',
                         'formatter': 'simple' },
            'null': { 'class': 'logging.NullHandler', },
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'django': {
                'handlers': ['console'],
                'level': LOG_LEVEL,
                'propagate': True,
            },
            'downloads': {
                'handlers': ['console'],
                'level': LOG_LEVEL,
                'propagate': True,
            }
        }
    }

class Dev(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    DATABASES = values.DatabaseURLValue('sqlite:///{0}'.format(
        os.path.join(Common.BASE_DIR, 'db.sqlite3'),
        environ=True))

    SECRET_KEY = 'notasecretatall'

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    #INSTALLED_APPS = Common.INSTALLED_APPS + ('debug_toolbar',)


class Stage(Common):
    DEBUG = True

    SECRET_KEY = values.SecretValue()

    EMAIL_HOST = values.Value('localhost')
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.Value()
    EMAIL_USE_TLS = values.BooleanValue(False)

    Common.LOGGING['handlers']['sentry'] = { 'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler', }
    Common.LOGGING['loggers'] = {
            '': {
                'handlers': ['sentry'],
                'level': Common.LOG_LEVEL,
                'propagate': True,
            }
    }


class Prod(Common):
    """
    The in-production settings.
    """
    DEBUG = False

    SECRET_KEY = values.SecretValue()

    CACHCES='djangopylibmc://127.0.0.1:11211'

    EMAIL_HOST = values.Value()
    EMAIL_HOST_USER = values.Value()
    EMAIL_HOST_PASSWORD = values.Value()
    EMAIL_PORT = values.Value()
    EMAIL_USE_TLS = values.BooleanValue(True)

    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + [
        'smart_cache_control.middleware.SmartCacheControlMiddleware',]

    Common.LOGGING['handlers']['sentry'] = { 'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler', }
    Common.LOGGING['loggers'] = {
        'django.db.backends': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['sentry'],
            'level': 'WARNING',
            'propagate': True,
        },
        '': {
            'handlers': ['sentry'],
            'level': 'WARNING',
            'propagate': True,
        },
        'downloads': {
            'handlers': ['sentry'],
            'level': 'INFO',
            'propagate': True,
        },
        'resource_library': {
            'handlers': ['sentry'],
            'level': 'WARNING',
            'propagate': True,
        },
        'sermons': {
            'handlers': ['sentry'],
            'level': 'WARNING',
            'propagate': True,
        }
    }

    DSN_VALUE = values.Value()

    # If we're on production, connect to Sentry
    RAVEN_CONFIG = {
        'dsn': DSN_VALUE.setup('DSN_VALUE'),
    }

    INSTALLED_APPS = Common.INSTALLED_APPS + (
        'raven.contrib.django.raven_compat',)
