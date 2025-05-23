from rest_framework.exceptions import ValidationError

from invoice.models import Purchase

class PurchaseFilterService:

    def __init__(self, validated, extra_filters = None):

        self.extra_filters = extra_filters or {}
        self.validated = validated
        self.maped_filters = {
            'start_date': 'purchase_date__gte',
            'end_date': 'purchase_date__lte',
            'min_value': 'value__gte',
            'max_value': 'value__lte',
            'min_installment': 'installment__gte',
            'max_installment': 'installment__lte',
            'description': 'description__icontains',
            'account': 'card__account_id__in',
            'cards': 'card_id__in',
        }

    def get_maped_filters(self):
        
        kwargs_filters = {}

        for key, value in self.validated.items():

            if key in self.maped_filters and value:

                kwargs_filters[self.maped_filters[key]] = value
        
        return kwargs_filters

    def filter(self):

        default_filters = self.get_maped_filters()
        
        return Purchase.objects \
            .select_related('card', 'card__account', 'invoice') \
            .order_by('purchase_date') \
            .only(
                'id', 'description', 'value', 'purchase_date', 'installment', 'installments',
                'card__account__first_name', 'card__account__last_name',
                'invoice__invoice_date') \
            .filter(**self.extra_filters, **default_filters)
