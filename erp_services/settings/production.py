# my_project/settings/production.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 31536000

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'), conn_max_age=1800),
}