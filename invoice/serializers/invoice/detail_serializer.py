from rest_framework import serializers

from django.db import models

from accounts.utils import time_performance

from invoice.models import Invoice, Purchase

class InvoiceDetailSerializer(serializers.ModelSerializer):

    amount = serializers.SerializerMethodField()
    itens_count = serializers.SerializerMethodField()

    class Meta:

        model = Invoice
        fields = '__all__'

    @time_performance(detail_name='Obter total da fatura')
    def get_amount(self, obj):  

        return Purchase.objects \
              .filter(invoice_id=obj.id) \
              .aggregate(amount=models.Sum('value')) \
              .get('amount') or 0.0
    
    @time_performance(detail_name='Obter total de itens da fatura')
    def get_itens_count(self, obj):

        return Purchase.objects \
              .filter(invoice_id=obj.id) \
              .count()