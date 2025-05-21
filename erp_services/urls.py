from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoices/', include('invoice.urls')),
    path('accounts/', include('accounts.urls')),
]
