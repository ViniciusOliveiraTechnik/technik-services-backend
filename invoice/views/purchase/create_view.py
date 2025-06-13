from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from invoice.serializers.purchase import PurchaseBaseSerializer
from invoice.models import Purchase

from accounts.permissions import IsInternalUser

from jwt_auth.permissions import MFAActive

class PurchaseCreateView(CreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsInternalUser, MFAActive, IsAuthenticated]

    serializer_class = PurchaseBaseSerializer

    def get_serializer_context(self):
    
        context = super().get_serializer_context()

        context['request'] = self.request
        context['request_user'] = self.request.user

        return context

    def get_queryset(self):
        
        return Purchase.objects \
        .select_related('card', 'card__account', 'invoice') \
        .only('card', 'invoice', 'description', 'value', 'purchase_date', 'installment', 'installments',
              'card__account__first_name', 'card__account__last_name',
              'invoice__invoice_date') \
        .all()

