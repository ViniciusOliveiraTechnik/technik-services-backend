from invoice.serializers.card import CardCreateSerializer, CardDetailSerializer
from invoice.models import Card

from django.db.models import Sum, Count


class CardCreateService:

    def __init__(self, context = None):
        
        self.context = context or {}

    def execute(self, data):

        serializer = CardCreateSerializer(data=data, context=self.context)

        serializer.is_valid(raise_exception=True)

        card = serializer.save()

        card = Card.objects \
        .select_related('account') \
        .annotate(
            spent=Sum('purchases_card__value'),
            itens_count=Count('purchases_card__id')) \
        .get(id=card.id)

        return CardDetailSerializer(card, context=self.context).data