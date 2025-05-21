from django.db.models import Min, Max
from django.utils import timezone

from invoice.models import Purchase

class DateUtil:

    @staticmethod
    def get_min_max_date():

        today = timezone.now().date()

        range_date = Purchase.objects \
        .aggregate(
            min_date=Min('purchase_date'), 
            max_date=Max('purchase_date'))
        
        min_date = range_date.get('min_date', today)
        max_date = range_date.get('max_date', today)

        return min_date, max_date