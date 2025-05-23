from invoice.models import Invoice
from invoice.serializers.invoice import InvoiceCreateSerializer, InvoiceBaseSerializer

from django.db.models import Sum, Count

class InvoiceCreateService:

    def __init__(self, context = None):
        
        self.context = context or {}

    def execute(self, data):

        serializer = InvoiceCreateSerializer(data=data, context=self.context)

        serializer.is_valid(raise_exception=True)

        invoice = serializer.save()

        invoice = Invoice.objects \
        .prefetch_related('purchases_invoice', 'purchases_invoice__card', 'purchases_invoice__card__account') \
        .annotate(
            amount=Sum('purchases_invoice__value'), 
            items=Count('purchases_invoice__id'),
            accounts=Count('purchases_invoice__card__account_id', distinct=True),
            cards=Count('purchases_invoice__card_id', distinct=True)) \
        .get(id=invoice.id)

        return InvoiceBaseSerializer(invoice, context=self.context).data