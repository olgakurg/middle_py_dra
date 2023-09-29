
"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from re import DEBUG
from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv() 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1').split(',')

# Application definition
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# Password validation# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

include(
    'components/application_definition.py',
    'components/database.py',
    'components/password_validation.py',
    'components/internationalization.py',
    'components/static.py',
    'components/default_primary_key.py',
)

LOCALE_PATHS = ['movies/locale'] 

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',],
    'DEFAULT_PAGINATION_CLASS': 'movies.pagination.CustomPagination',
    'PAGE_SIZE': 50,
}
    
