import pandas as pd

from invoice.models import Card, Purchase
from invoice.serializers.purchase import PurchaseDetailSerializer

from rest_framework.exceptions import ValidationError

class ItauReaderUtil:

    def __init__(self, file, invoice_instance):
        
        self.file = file
        self.invoice_instance = invoice_instance
        self.card_cache = {}

    def get_card_object(self, name):
        
        card = self.card_cache.get(name)

        if not card:

            raise ValidationError({'card': f'O cartão {name} não existe'})
        
        return card

    def extract(self):

        dataframe = pd.read_excel(self.file)

        pattern_name = r'[A-Za-zÀ-ÿ\s\-]+FINAL\s+[0-9\*]+'

        invoice = dataframe.iloc[:, [0, 2, 10]].copy()
        invoice.columns = ['purchase_date', 'description', 'value']

        invoice['converted_purchase_date'] = pd.to_datetime(invoice['purchase_date'], format="%Y-%m-%d %H:%M:%S", errors='coerce')

        has_card_name = invoice['purchase_date'].astype(str).str.match(pattern_name, na=False)

        invoice['card'] = invoice['purchase_date'].where(has_card_name).str.extract(r'^([A-Za-zÀ-ÿ\s\-]+)\s-\sFINAL')[0].ffill()

        invoice = invoice[invoice['converted_purchase_date'].notna()].drop(columns='converted_purchase_date').reset_index(drop=True)
        
        invoice[['installment', 'installments']] = invoice['description'].str.extract(r'(\d{2})/(\d{2})').astype(float).astype('Int64')

        invoice['installment'] = invoice['installment'].fillna(1)
        invoice['installments'] = invoice['installments'].fillna(1)

        invoice['card'] = 'VINICIUS OLIVEIRA' # just dev

        # Creating cards cache to find the card reference in database

        self.card_cache = {card.name: card for card in Card.objects.filter(name__in=invoice['card'].unique())}

        invoice['card'] = invoice['card'].map(self.get_card_object)

        invoice['invoice'] = self.invoice_instance

        purchase_data = invoice.to_dict(orient='records')

        purchases = [Purchase(**purchase) for purchase in purchase_data]

        Purchase.objects.bulk_create(purchases)

        purchases_instances = Purchase.objects.filter(invoice=self.invoice_instance) \
        .select_related('card', 'invoice','card__account') \
        .only('id', 'description', 'value', 'purchase_date', 'installment', 'installments', 
              'invoice__invoice_date',
              'card__account__first_name', 'card__account__last_name')

        return PurchaseDetailSerializer(purchases_instances, many=True).data
