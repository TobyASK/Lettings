"""Django settings for OC Lettings project."""

import logging
import os
from pathlib import Path

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# .parent remonte de settings.py → oc_lettings_site/ → racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s',
)
# Accepte '1', 'true' ou 'yes' pour éviter les surprises de casse
DEBUG = os.getenv('DEBUG', 'True').lower() in {'1', 'true', 'yes'}

# La variable d'env contient une liste séparée par des virgules ;
# strip() filtre les espaces et élimine les entrées vides après split
ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
    if host.strip()
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oc_lettings_site.apps.OCLettingsSiteConfig',
    'lettings.apps.LettingsConfig',
    'profiles.apps.ProfilesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise doit être juste après SecurityMiddleware pour servir
    # les fichiers statiques sans passer par Django en production
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

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

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        ),
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

# Type de clé primaire par défaut pour les modèles sans pk explicite
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
# En production : CompressedStaticFilesStorage compresse les fichiers (gzip/brotli)
# pour réduire leur taille, sans générer de manifest strict qui bloquerait
# le build si le CSS référence des assets absents du repo.
STATICFILES_STORAGE = (
    'django.contrib.staticfiles.storage.StaticFilesStorage'
    if DEBUG else
    'whitenoise.storage.CompressedStaticFilesStorage'
)


LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

LOGGING = {
    'version': 1,  # seule valeur supportée par Django
    'disable_existing_loggers': False,  # conserve les loggers Django déjà créés au démarrage
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': LOG_LEVEL,
    },
}


SENTRY_DSN = os.getenv('SENTRY_DSN', '')
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        # 0.2 = 20 % des requêtes font l'objet d'un suivi de performance
        traces_sample_rate=float(
            os.getenv('SENTRY_TRACES_SAMPLE_RATE', '0.2')
        ),
        # Transmet les données utilisateur (IP, session) pour faciliter le débogage
        send_default_pii=True,
        environment=os.getenv('SENTRY_ENVIRONMENT', 'development'),
    )
    logging.getLogger(__name__).info('Sentry integration enabled')
