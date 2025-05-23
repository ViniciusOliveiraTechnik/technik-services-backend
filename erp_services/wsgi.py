"""
WSGI config for erp_services project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv
load_dotenv() # Used to load all external and sensitve variables from .env

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_services.settings.development')

application = get_wsgi_application()
