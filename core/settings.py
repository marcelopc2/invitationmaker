"""
Django settings for core project.
Configurado para soportar tanto entornos de Desarrollo como de Producción
mediante variables de entorno (.env).
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno desde .env
load_dotenv(BASE_DIR / '.env')


# ===========================================================
# SEGURIDAD
# ===========================================================

SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-insecure-key-only-for-dev')

DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 'yes')

# En desarrollo puede ser '*'. En producción, lista tu dominio real.
_allowed_hosts_env = os.environ.get('ALLOWED_HOSTS', '')
ALLOWED_HOSTS = [h.strip() for h in _allowed_hosts_env.split(',') if h.strip()] or ['localhost', '127.0.0.1']


# ===========================================================
# APLICACIONES
# ===========================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'invitaciones',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# ===========================================================
# BASE DE DATOS
# ===========================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ===========================================================
# VALIDACIÓN DE CONTRASEÑAS
# ===========================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ===========================================================
# INTERNACIONALIZACIÓN
# ===========================================================

LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ===========================================================
# ARCHIVOS ESTÁTICOS Y MEDIA
# ===========================================================

STATIC_URL = '/static/'

# En producción: `python manage.py collectstatic` copiará todo aquí
# Nginx/Apache sirve esta carpeta directamente
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ===========================================================
# CONFIGURACIONES ADICIONALES DE PRODUCCIÓN
# ===========================================================

if not DEBUG:
    # Forzar HTTPS (activar en producción)
    # SECURE_SSL_REDIRECT = True
    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SECURE = True
    # SECURE_HSTS_SECONDS = 31536000
    pass


# ===========================================================
# OTROS
# ===========================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
