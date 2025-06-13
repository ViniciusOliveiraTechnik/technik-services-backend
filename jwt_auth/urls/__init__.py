from .tokens import urlpatterns as tokens_urls_patterns
from .auth import urlpatterns as two_factors_urls_patterns

urlpatterns = tokens_urls_patterns + two_factors_urls_patterns
