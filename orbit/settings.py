"""
Django settings for orbit project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.contrib.messages import constants as messages


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x&fhq*148b(@&u5f5h7(sg#e6u5sv_=g@c8#i)+k)tyejee)i&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = ('127.0.0.1',)


# APP CONFIGURATION
# ------------------------------------------------------------------------------

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'ckeditor',
    'debug_toolbar'
]

LOCAL_APPS = [
    'accounts',
    'authentication',
    'events',
    'pages',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'orbit.urls'

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'orbit.wsgi.application'


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ACCOUNTS / AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

ACCOUNTS_DISABLE_SIGNUP = False

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'accounts.Account'

# Any authentication required pages will redirect here to authenticate
LOGIN_URL = 'authentication:signin'

# The default post authentication redirect url
LOGIN_REDIRECT_URL = 'dashboard:dashboard'

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Sydney'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# MESSAGES CONFIGURATION
# ------------------------------------------------------------------------------

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# STATIC CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# CKEDITOR CONFIGURATION
# ------------------------------------------------------------------------------

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'height': '70vh',
        'extraPlugins': ','.join([
            'tableresize',
        ]),
        'removePlugins': ','.join([
            'flash',
        ]),
        'toolbar': 'toolbar',
        'toolbar_toolbar': [
            {
                'name': 'styles',
                'items': ['Styles', 'Format', 'Font', 'FontSize']
            },
            {
                'name': 'insert',
                'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley']
            },
            {
                'name': 'colors',
                'items': ['TextColor', 'BGColor']
            },
            {
                'name': 'fontstyles',
                'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript']
            },
            {
                'name': 'list',
                'items': ['BulletedList', 'NumberedList']
            },
            {
                'name': 'justify',
                'items': ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']
            },
            {
                'name': 'indent',
                'items': ['Outdent', 'Indent']
            },
            {
                'name': 'links',
                'items': ['Link', 'Unlink', 'Anchor']
            },
        ],
    }
}
