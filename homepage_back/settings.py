"""
Django settings for homepage_back project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import boto3
import json
from botocore.exceptions import ClientError
from decouple import config
from pathlib import Path


# https://aws.amazon.com/developer/language/python/
def get_secret():

    secret_name = config('AWS_SECRET_NAME')
    region_name = "us-west-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    return get_secret_value_response['SecretString']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework'
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

ROOT_URLCONF = 'homepage_back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'homepage_back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'auth': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'auth',
        'USER': config('AUTH_DB_USER'),
        'PASSWORD': json.loads(get_secret())['password'],
        'HOST':  config('AUTH_DB_URL'),
        'PORT': '5432',
    },
    'recipes': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'recipes',
        'USER': config('RECIPE_DB_USER'),
        'PASSWORD': json.loads(get_secret())['password'],
        'HOST':  config('RECIPE_DB_URL'),
        'PORT': '5432',
    },
    'recipes_dev': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'receipe_db_dev', # NICE
        'USER': config('RECIPE_DB_DEV_USER'),
        'PASSWORD': json.loads(get_secret())['password'],
        'HOST':  config('RECIPE_DB_DEV_URL'),
        'PORT': '5432',
    },
    'hbl': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hbl',
        'USER': config('HBL_DB_USER'),
        'PASSWORD': json.loads(get_secret())['password'],
        'HOST': config('HBL_DB_URL'),
        'PORT': '5432'
    },
    'hbl_dev': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hbl',
        'USER': config('HBL_DB_DEV_USER'),
        'PASSWORD': json.loads(get_secret())['password'],
        'HOST': config('HBL_DB_DEV_URL'),
        'PORT': '5432'
    }
}
DATABASE_ROUTERS = ['recipes.dbrouters.AuthRouter', 'recipes.dbrouters.RecipesRouter', 'hbl.dbrouters.HblRouter']
if DEBUG:
    DATABASE_ROUTERS = ['recipes.dbrouters.AuthRouter', 'recipes.dbrouters.RecipesDevRouter', 'hbl.dbrouters.HblDevRouter']

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
