

"""
Django settings for whatznot project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nw#@u*$=rslp9dwexakq2=4r*kb@a%(f4nrb5jmk0jz=t8fgxx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['web-production-fcf2.up.railway.app']


CSRF_COOKIE_SECURE=False
CSRF_COOKIE_DOMAIN = 'web-production-fcf2.up.railway.app'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CORS_ORIGIN_ALLOW_ALL = True
CSRF_COOKIE_HTTPONLY = False
# Application definition
ALLOWED_ORIGINS = ['http://*', 'https://*']
CSRF_TRUSTED_ORIGINS = ALLOWED_ORIGINS.copy()
INSTALLED_APPS = [
    'material',
    'material.admin',
#    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'about',
    'froala_editor',
    'blog',
    'contact',
    'portfolios',
    'services',
    'home',

]


MATERIAL_ADMIN_SITE = {
    'HEADER':  ('Whatznot Technology'),  # Admin site header
    'TITLE':  ('whatznot'),  # Admin site title
    'FAVICON':  "imgs/logo/favicon.png",  # Admin site favicon (path to static should be specified)
    'MAIN_BG_COLOR':  'blue',  # Admin site main color, css color should be specified
    'MAIN_HOVER_COLOR':  'blue',  # Admin site main hover color, css color should be specified
    'PROFILE_PICTURE':  "imgs/logo/favicon.png",  # Admin site profile picture (path to static should be specified)
    'PROFILE_BG':  "imgs/logo/favicon.png",  # Admin site profile background (path to static should be specified)
    'LOGIN_LOGO':  "imgs/logo/favicon.png",  # Admin site logo on login page (path to static should be specified)
    'LOGOUT_BG':  "imgs/logo/favicon.png",  # Admin site background on login/logout pages (path to static should be specified)
    'SHOW_THEMES':  True,  #  Show default admin themes button
    'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE': True,  # Hide side navbar by default
    'SHOW_COUNTS': True, # Show instances counts for each model
    'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
       'portfolio': 'check_circle_outline',
        },
    'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
        'team_detail': 'groups',
        'faqs': 'edit',
        'group': 'groups',
        'user': 'person',
        'portfolio': 'collections',
        'author': 'hail',
        'blog': 'note_add',
        'cat': 'category',


    }
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'whatznot.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'whatznot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


