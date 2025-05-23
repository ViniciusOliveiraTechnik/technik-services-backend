from .invoice import urlpatterns as invoice_patterns
from .card import urlpatterns as card_patterns
from .purchases import urlpatterns as purchases_patterns

urlpatterns = invoice_patterns + card_patterns + purchases_patterns
