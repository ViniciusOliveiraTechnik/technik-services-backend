from django.contrib import admin
from invoice.models import Card, Purchase, Invoice

admin.site.register([Card, Purchase, Invoice])