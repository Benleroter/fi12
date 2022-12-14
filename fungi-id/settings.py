"""
Django settings for fungi-id project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost','fungi-id.co.uk','www.fungi-id.co.uk','fungi-id-dev.eu-west-2.elasticbeanstalk.com','172.31.42.240','192.168.0.1','18.132.79.16','35.178.255.6','18.132.79.16']
                                                                                                          

# Application definition

INSTALLED_APPS = [
    'fungi.apps.FungiConfig',
    'users.apps.UsersConfig',
    'usersettings.apps.UserSettingsConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'health_check',
    'health_check.db',
    'health_check.cache', 
    'health_check.storage',
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

ROOT_URLCONF = 'fungi-id.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'fungi-id.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


if 'RDS_HOSTNAME' in os.environ:
    print('RDS_DB_NAME', os.environ.get('RDS_DB_NAME'))
    print('RDS_USERNAME', os.environ.get('RDS_USERNAME'))
    print('RDS_PASSWORD', os.environ.get('RDS_PASSWORD'))
    print('RDS_HOSTNAME', os.environ.get('RDS_HOSTNAME'))
    print('RDS_PORT', os.environ.get('RDS_PORT'))
 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('RDS_DB_NAME'),
            'USER': os.environ.get('RDS_USERNAME'),
            'PASSWORD': os.environ.get('RDS_PASSWORD'),
            'HOST': os.environ.get('RDS_HOSTNAME'),
            'PORT': os.environ.get('RDS_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
LOGIN_REDIRECT_URL = 'AllFungi-HomePage'
LOGIN_URL = 'login'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

#SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_COOKIE_AGE = 5
#SESSION_SAVE_EVERY_REQUEST = True

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
