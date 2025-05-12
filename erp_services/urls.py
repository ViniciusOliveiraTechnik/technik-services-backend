from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('invoice/', include('invoice.urls')),
    path('accounts/', include('accounts.urls')),
]
