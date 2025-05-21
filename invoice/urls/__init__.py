from .invoice import urlpatterns as invoice_patterns
from .card import urlpatterns as card_patterns


urlpatterns = invoice_patterns + card_patterns