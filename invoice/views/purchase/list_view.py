from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.permissions import IsInternalUser, TwoFactorsValidated

from invoice.services.purchase import PurchaseListService
from invoice.serializers.purchase import PurchaseBaseSerializer
from invoice.paginations.purchase import PurchaseStandardPagination

class PurchaseListView(ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    serializer_class = PurchaseBaseSerializer
    pagination_class = PurchaseStandardPagination

    def get_serializer_context(self):

        context = super().get_serializer_context()
        context['request'] = self.request
        context['request_user'] = self.request.user

        return context

    def get_queryset(self):
        
        data = self.request.query_params
        context = self.get_serializer_context()

        service = PurchaseListService(context)

        return service.execute(data)