"""
For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of experimental and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# django-environ
# https://django-environ.readthedocs.io/en/latest/quickstart.html#quick-start

env = environ.Env()

ADMIN_URL = env.str("ADMIN_URL", default="admin/")

# Topical Index
# https://docs.djangoproject.com/en/5.0/ref/settings/#core-settings-topical-index

# Auth
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Core Settings
# https://docs.djangoproject.com/en/5.0/ref/settings/#core-settings

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# File Uploads
# https://docs.djangoproject.com/en/5.0/ref/settings/#file-uploads

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # Whitenoise
    # https://whitenoise.readthedocs.io/en/latest/django.html#using-whitenoise-with-django
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Globalization (i18n/l10n)
# https://docs.djangoproject.com/en/5.0/ref/settings/#globalization-i18n-l10n

LANGUAGE_CODE = env.str("LANGUAGE_CODE", default="en-us")
TIME_ZONE = env.str("TIME_ZONE", default="UTC")
USE_I18N = env.bool("USE_I18N", default=True)
USE_TZ = env.bool("USE_TZ", default=True)

# HTTP
# https://docs.djangoproject.com/en/5.0/ref/settings/#http

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # Whitenoise
    # https://whitenoise.readthedocs.io/en/latest/django.html#using-whitenoise-with-django
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

WSGI_APPLICATION = "project.wsgi.application"

# Static Files
# https://docs.djangoproject.com/en/5.0/ref/settings/#static-files

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = env.str("STATIC_URL", default="static/")

# Templates
# https://docs.djangoproject.com/en/5.0/ref/settings/#id11

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# URLs
# https://docs.djangoproject.com/en/5.0/ref/settings/#urls

ROOT_URLCONF = "project.urls"
