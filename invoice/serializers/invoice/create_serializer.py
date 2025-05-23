from invoice.models import Invoice

from rest_framework import serializers

class InvoiceCreateSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = Invoice
        fields = ['invoice_date', 'bank']

    def validate_invoice_date(self, value):

        if Invoice.objects \
        .filter(
            invoice_date__month = value.month,
            invoice_date__year=value.year) \
        .only('id') \
        .exists():
            
            raise serializers.ValidationError(f'Já existe uma fatura cadastrada para {value.month}/{value.year}')
        
        return value    
