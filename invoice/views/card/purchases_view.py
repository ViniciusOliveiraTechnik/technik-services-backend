from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from invoice.serializers.purchase import PurchaseDetailSerializer
from invoice.services.card import CardPurchasesService
from invoice.paginations.card import CardStandardPagination
from invoice.permissions import IsOwnerOrAdmin

from accounts.permissions import TwoFactorsValidated, IsInternalUser

class CardPurchasesView(ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [TwoFactorsValidated, IsInternalUser, IsAuthenticated, IsOwnerOrAdmin]

    serializer_class = PurchaseDetailSerializer
    pagination_class = CardStandardPagination
    lookup_field = 'pk'

    def get_serializer_context(self):

        context = super().get_serializer_context()
        context['request'] = self.request
        context['request_user'] = self.request.user

        return context
    
    def get_queryset(self):

        pk = self.kwargs.get('pk')
        data = self.request.query_params
        context = self.get_serializer_context()

        service = CardPurchasesService(context)

        return service.execute(data, pk)