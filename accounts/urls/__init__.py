from .accounts import urlpatterns as accounts_urls
from .password import urlpatterns as password_urls

urlpatterns = accounts_urls + password_urls
