"""
Django settings for Cienciometrico project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from django.contrib.messages import constants as messages
import os

from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sauj+%4^8oj#(w%7+9x-@9^b03^yxicq=ez)7c-h@@j84t)%v-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'apps.Ambito_Investigativo',
    'apps.Bitacora',
    'apps.Grado_Competencia',
    'apps.Intereses_Formativos',
    'apps.Linea_Investigacion',
    'apps.Palabra_clave',
    'apps.Ponencia',
    'apps.Privilegios',
    'apps.Sub_Lin_Investigacion',
    'apps.Unidad_Investigacion',
    'apps.Unidades_Investigacion',
    'apps.pais',
    'apps.zona',
    'apps.provincia',
    'apps.canton',
    'apps.universidad',
    'apps.campus',
    'apps.facultad',
    'apps.carrera',
    'apps.Investigador',
    'apps.Articulos_Cientificos',
    'apps.investigaciones',
    'apps.datosprofesionales',
    'apps.Formacion_Academica',
    'apps.Formacion_Complementaria',
    'apps.Evento',
    'apps.otrasinvestigaciones',
    'apps.participacioneventos',
    'apps.Proyectos',
    'apps.perfiles',
    'apps.inicio',
    'apps.Libro',
    'apps.Revista',
    'apps.Publicaciones',
    'apps.roles',
    'apps.capacitacion',
    'apps.baseDatos',
    'apps.palabraClave',
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

ROOT_URLCONF = 'Cienciometrico.urls'

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

WSGI_APPLICATION = 'Cienciometrico.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cienciometrico',
        'USER': 'postgres',
        'PASSWORD': 'drex',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

LOGIN_REDIRECT_URL= reverse_lazy('inicio:logeo')
LOGOUT_REDIRECT_URL= reverse_lazy('iniciop:principal')


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'cienciometricoutc@gmail.com'
EMAIL_HOST_PASSWORD = 'cienciometricoUTC2017'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
