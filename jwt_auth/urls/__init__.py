from .tokens import urlpatterns as tokens_urls_patterns
from .two_factors import urlpatterns as two_factors_urls_patterns

urlpatterns = tokens_urls_patterns + two_factors_urls_patterns
