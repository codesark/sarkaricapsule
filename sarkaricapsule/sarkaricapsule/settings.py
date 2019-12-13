
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', '_xg(&zd1f1!v!0%kqzb)ffxwvb5^swbanmztsnn#px6x&wm)f1')

TEMPLATE_DIR = os.environ.get('TEMPLATE_DIR', os.path.join(BASE_DIR, 'templates'))
STATIC_DIR = os.environ.get('STATIC_DIR', os.path.join(BASE_DIR, 'static'))

MEDIA_DIR = os.environ.get('MEDIA_DIR', os.path.join(BASE_DIR, 'media'))

DEBUG = int(os.environ.get('DEBUG', 1))

SITE_ID = 1

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(" ")

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
    # 'storages',

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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('PG_DATABASE', 'sarkaricapsule'),
#         'USER': os.environ.get('PG_USER', 'sarkaricapsule_user'),
#         'PASSWORD': os.environ.get('PG_PASSWORD', 'dbpass001'),
#         'HOST': os.environ.get('PG_HOST', '127.0.0.1'),
#         'PORT': int(os.environ.get('PG_PORT', '5432')),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", 'django.db.backends.postgresql_psycopg2'),
        "NAME": os.environ.get("SQL_DATABASE", 'sarkaricapsule'),
        "USER": os.environ.get("SQL_USER", 'sarkaricapsule_user'),
        "PASSWORD": os.environ.get("SQL_PASSWORD", 'dbpass001'),
        "HOST": os.environ.get("SQL_HOST", '127.0.0.1'),
        "PORT": os.environ.get("SQL_PORT", '5432'),
    }
}

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

# AWS_DEFAULT_ACL = None
# AWS_S3_SIGNATURE_VERSION = 's3v4'
# AWS_S3_CUSTOM_DOMAIN = 'static.sarkaricapsule.com'
# AWS_ACCESS_KEY_ID = 'RXRUYCPHL3VV366WKD7Y'
# AWS_SECRET_ACCESS_KEY = '7ZVCOSVTpUWk5UAh4wEFfXCnZrFmIcmRIn9D66KU1Xc'
# AWS_STORAGE_BUCKET_NAME = 'sarkaricapsule'
# AWS_S3_ENDPOINT_URL = 'https://betabrains.sgp1.digitaloceanspaces.com'
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'

# STATICFILES_DIRS = [
#     STATIC_DIR,
# ]
# # AWS_S3_ENDPOINT_URL='static.sarkaricapsule.com'
# STATIC_URL = '%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
# # STATIC_URL = '%s/%s/' % ('https://static.sarkaricapsule.com', AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
