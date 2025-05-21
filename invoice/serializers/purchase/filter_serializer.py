from rest_framework import serializers

from invoice.utils.purchase import DateUtil

class PurchasesFilterSerializer(serializers.Serializer):

    start_date = serializers.DateField(required=False, format='%Y-%m-%d')
    end_date = serializers.DateField(required=False, format='%Y-%m-%d')
    min_value = serializers.DecimalField(required=False, max_digits=10, decimal_places=4)
    max_value = serializers.DecimalField(required=False, max_digits=10, decimal_places=4)
    min_installment = serializers.IntegerField(required=False)
    max_installment = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)

    def validate(self, attrs):
        
        date_util = DateUtil()

        min_date, max_date = date_util.get_min_max_date()

        start_date = attrs.get('start_date', min_date)
        end_date = attrs.get('end_date', max_date)

        if end_date < start_date:

            raise serializers.ValidationError('A data final não pode ser menor que a data inical')

        attrs['start_date'] = start_date
        attrs['end_date'] = end_date

        return attrs