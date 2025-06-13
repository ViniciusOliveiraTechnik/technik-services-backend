from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from jwt_auth.permissions import MFAActive

from accounts.paginations import StandardResultsSetPagination
from accounts.serializers import AccountDetailSerializer
from accounts.models import Account

@method_decorator(cache_page(60 * 5), name='dispatch')
class AccountListView(ListAPIView):
    
    queryset = Account.objects.all().order_by('first_name')
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, MFAActive]
    serializer_class = AccountDetailSerializer
    pagination_class = StandardResultsSetPagination

    def get_serializer_context(self):
        
        context = super().get_serializer_context()
        context['request'] = self.request

        return context