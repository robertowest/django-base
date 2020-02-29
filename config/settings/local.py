from .base import *

INSTALLED_APPS += [
    'apps.home',
]

DEBUG = True
ALLOWED_HOSTS = ['localhost']

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Tucuman'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
