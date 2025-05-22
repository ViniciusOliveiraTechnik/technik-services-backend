from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.permissions import IsInternalUser, TwoFactorsValidated

from invoice.models import Purchase
from invoice.serializers.purchase import PurchaseBaseSerializer

class PurchaseConfigurationView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsInternalUser, TwoFactorsValidated, IsAuthenticated]

    serializer_class = PurchaseBaseSerializer

    lookup_field = 'pk'

    def get_serializer_context(self):

        context = super().get_serializer_context()

        context['request'] = self.request
        context['request_user'] = self.request.user

        return context

    def get_queryset(self):
        
        purchase_id = self.kwargs.get('pk')

        return Purchase.objects \
        .select_related('card', 'card__account', 'invoice') \
        .only('description', 'value', 'purchase_date', 'installment', 'installments',
              'card__account__first_name', 'card__account__last_name',
              'invoice__invoice_date') \
        .filter(id=purchase_id)
