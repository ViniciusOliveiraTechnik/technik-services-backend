from invoice.models import Purchase
from invoice.utils.purchase import DetailUtil

from rest_framework import serializers

class PurchaseDetailSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.detail_util = DetailUtil(self.context.get('request_user'))

    account_name = serializers.SerializerMethodField()
    invoice_date = serializers.SerializerMethodField()

    description = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()

    class Meta:

        model = Purchase
        fields = ['id', 'account_name', 'description', 'value', 'purchase_date', 'invoice_date', 'installment', 'installments']

    def get_value(self, obj):
        
        value = obj.value

        if self.detail_util.show_sensitive(obj):

            return value

        return self.detail_util.mask_value(value)

    def get_description(self, obj):

        description = obj.description

        if self.detail_util.show_sensitive(obj):

            return description
        
        return self.detail_util.mask_description(description)

    def get_account_name(self, obj):

        return f'{obj.card.account.first_name} {obj.card.account.last_name}'
    
    def get_invoice_date(self, obj):

        return f"{obj.invoice.invoice_date.strftime('%Y/%m')}-{obj.card.account.first_name} {obj.card.account.last_name}"