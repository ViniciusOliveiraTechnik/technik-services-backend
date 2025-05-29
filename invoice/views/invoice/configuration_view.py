from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from django.db.models import Sum, Count

from accounts.permissions import IsInternalUser

from jwt_auth.permissions import IsTwoFactorsVerified

from invoice.models import Invoice
from invoice.serializers.invoice import InvoiceBaseSerializer

class InvoiceConfigurationView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsInternalUser, IsTwoFactorsVerified]

    serializer_class = InvoiceBaseSerializer 
    lookup_field = 'pk'

    def get_queryset(self):
        
        invoice_id = self.kwargs.get('pk')

        return Invoice.objects \
        .prefetch_related('purchases_invoice', 
                          'purchases_invoice__card', 
                          'purchases_invoice__card__account') \
        .annotate(
            amount=Sum('purchases_invoice__value'), 
            items=Count('purchases_invoice__id'), 
            accounts=Count('purchases_invoice__card__account_id'), 
            cards=Count('purchases_invoice__card_id')) \
        .filter(id=invoice_id)