from rest_framework import serializers

from django.utils import timezone
from django.db.models import Min, Max

from invoice.models import Purchase
from invoice.utils.purchase import DateUtil

class PurchasesFilterSerializer(serializers.Serializer):

    start_date = serializers.DateField(required=False, format='%Y-%m-%d')
    end_date = serializers.DateField(required=False, format='%Y-%m-%d')
    card_name = serializers.CharField(required=False, max_length=50, allow_blank=True)

    def validate(self, attrs):
        
        util = DateUtil()

        min_date, max_date = util.get_min_max_date()

        start_date = attrs.get('start_date', min_date)
        end_date = attrs.get('end_date', max_date)

        if end_date < start_date:

            raise serializers.ValidationError('A data final não pode ser menor que a data inical')
        
        return attrs