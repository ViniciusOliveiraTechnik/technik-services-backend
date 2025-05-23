import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_services.settings.development')

app = Celery('erp_services')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

