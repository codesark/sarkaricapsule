from local_settings import *

BASE_DIR = BASE_DIR

SECRET_KEY = '_xg(&zd1f1!v!0%kqzb)ffxwvb5^swbanmztsnn#px6x&wm)f1'

TEMPLATE_DIR = TEMPLATE_DIR
STATIC_DIR = STATIC_DIR
MEDIA_DIR = MEDIA_DIR

DEBUG = DEBUG

SITE_ID = 1

ALLOWED_HOSTS = ALLOWED_HOSTS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'phonenumber_field',
    'django_summernote',
    'graphene_django',

    'locations',
    'organizations',
    'events',
    'news'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sarkaricapsule.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'sarkaricapsule.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = DATABASES


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-in'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR
# STATIC_ROOT = STATIC_DIR

if DEBUG:
    STATICFILES_DIRS = [STATIC_DIR, ]
else:
    STATIC_ROOT = STATIC_DIR

# Summernote editor configuration

import datetime
def summernote_custom_upload_to():
    return "inline/media/" + datetime.datetime.now().strftime("%Y/%m")

SUMMERNOTE_CONFIG = {
    # 'iframe': False,
    'attachment_upload_to': summernote_custom_upload_to(),
    'summernote': {
        # 'airMode': True,
        # 'width': '100%',
        'height': '300',
        # 'disableResizeEditor': False
    },
}


# Django Graphene -------
GRAPHENE = {
    'SCHEMA': 'sarkaricapsule.schema.schema'
}