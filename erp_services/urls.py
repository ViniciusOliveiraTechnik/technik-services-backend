from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('silk/', include('silk.urls', namespace='silk')),
    path('auth/', include('jwt_auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('financial/', include('invoice.urls')),

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
