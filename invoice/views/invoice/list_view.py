from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from django.db.models import Sum, Count

from accounts.permissions import IsInternalUser

from jwt_auth.permissions import MFAActive

from invoice.models import Invoice
from invoice.serializers.invoice import InvoiceBaseSerializer

class InvoiceListView(ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsInternalUser, MFAActive]

    serializer_class = InvoiceBaseSerializer

    def get_queryset(self):
        
        return Invoice.objects \
        .prefetch_related('purchases_invoice') \
        .annotate(
            amount=Sum('purchases_invoice__value'), 
            items=Count('purchases_invoice__id'),
            accounts=Count('purchases_invoice__card__account_id', distinct=True),
            cards=Count('purchases_invoice__card_id', distinct=True)) \
        .all()