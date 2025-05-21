from invoice.models import Purchase

from rest_framework import serializers

class PurchaseDetailSerializer(serializers.ModelSerializer):

    account_name = serializers.SerializerMethodField()
    invoice_date = serializers.SerializerMethodField()

    class Meta:

        model = Purchase
        fields = ['id', 'account_name', 'description', 'value', 'purchase_date', 'invoice_date', 'installment', 'installments']

    def get_account_name(self, obj):

        return f'{obj.card.account.first_name} {obj.card.account.last_name}'
    
    def get_invoice_date(self, obj):

        return f"{obj.invoice.invoice_date.strftime('%Y/%m')}-{obj.card.account.first_name} {obj.card.account.last_name}"