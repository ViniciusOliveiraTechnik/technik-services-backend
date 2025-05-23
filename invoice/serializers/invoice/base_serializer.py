from rest_framework import serializers

from invoice.models import Invoice

class InvoiceBaseSerializer(serializers.ModelSerializer):

    amount = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()
    accounts = serializers.SerializerMethodField()
    cards = serializers.SerializerMethodField()

    class Meta:

        model = Invoice
        fields = ['items', 'accounts', 'cards', 'amount', 'id', 'invoice_date', 'bank']
        extra_kwargs = {
            'invoice_date': {'required': True},
            'bank': {'required': True}
        }

    def validate_invoice_date(self, value):

        if Invoice.objects \
        .filter(
            invoice_date__month=value.month, 
            invoice_date__year=value.year) \
        .only('id') \
        .exists():
            
            raise serializers.ValidationError(f'Já há uma fatura com a data {value.month}/{value.year}')
        
        return value

    def get_amount(self, obj):

        return obj.amount if obj.amount else 0.0
    
    def get_items(self, obj):

        return obj.items if obj.items else 0
    
    def get_accounts(self, obj):

        return obj.accounts if obj.accounts else 0
    
    def get_cards(self, obj):

        return obj.cards if obj.cards else 0