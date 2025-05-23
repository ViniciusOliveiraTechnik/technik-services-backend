from invoice.models import Purchase, Card, Invoice
from invoice.utils.purchase import DetailUtil

from rest_framework import serializers

class PurchaseBaseSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.detail_util = DetailUtil(self.context.get('request_user'))

    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all(), required=True, write_only=True)
    card = serializers.PrimaryKeyRelatedField(queryset=Card.objects.all(), required=True, write_only=True)

    account_name = serializers.SerializerMethodField()
    invoice_date = serializers.SerializerMethodField()

    class Meta:
        model = Purchase
        fields = ['id', 'account_name', 'card', 'invoice', 'description', 'value', 'purchase_date', 'invoice_date', 'installment', 'installments']
        extra_kwargs = {
            'description': {'required': True},
            'value': {'required': True},
            'purchase_date': {'required': True},
            'installment': {'required': True},
            'installments': {'required': True},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.detail_util = DetailUtil(self.context.get('request_user'))

    def get_account_name(self, obj):

        return f'{obj.card.account.first_name} {obj.card.account.last_name}'

    def get_invoice_date(self, obj):

        return f"{obj.invoice.invoice_date.strftime('%Y/%m')}-{obj.card.account.first_name} {obj.card.account.last_name}"

    def to_representation(self, instance):

        representation = super().to_representation(instance)

        if not self.detail_util.show_sensitive(instance):

            representation['value'] = self.detail_util.mask_value(representation['value'])
            representation['description'] = self.detail_util.mask_description(representation['description'])

        return representation