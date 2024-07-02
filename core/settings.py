from datetime import timedelta
from pathlib import Path
import os
import socket
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

hostname = socket.gethostname()
if hostname == '10.0.4.161 172.17.0.1':
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get("SQL_DATABASE"),
            'USER': os.environ.get("SQL_USER"),
            'PASSWORD': os.environ.get("SQL_PASSWORD"),
            'HOST': os.environ.get("SQL_HOST"),
            'PORT': os.environ.get("SQL_PORT"),
        }
    }

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    "127.0.0.1",
]


INSTALLED_APPS = [
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "debug_toolbar",
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'drf_spectacular_sidecar',

    'user',
    'product',
    'client',
    'sale',
    'dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'utils.middlewares.DoesNotExistMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:1337"]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get("SQL_DATABASE"),
#         'USER': os.environ.get("SQL_USER"),
#         'PASSWORD': os.environ.get("SQL_PASSWORD"),
#         'HOST': os.environ.get("SQL_HOST"),
#         'PORT': os.environ.get("SQL_PORT"),
#     }
# }

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


# LANGUAGE_CODE = 'ru'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = False

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=3),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Tel Zone API',
    'DESCRIPTION': 'Shopping center',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
}
