from django.contrib import admin

from jwt_auth.models import OneTimeCode

# Register your models here.
admin.site.register(OneTimeCode)