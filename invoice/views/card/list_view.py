from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from django.db.models import Sum, Count

from invoice.models import Card
from invoice.serializers.card import CardDetailSerializer
from invoice.paginations import CardStandardPagination

from accounts.permissions import TwoFactorsValidated, IsInternalUser

class CardListView(ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, TwoFactorsValidated, IsInternalUser]

    pagination_class = CardStandardPagination
    serializer_class = CardDetailSerializer
    queryset = Card.objects \
            .all() \
            .select_related('account') \
            .annotate(
                spent=Sum('purchases_card__value'),
                itens_count=Count('purchases_card__id')
            ) \
            .order_by('name') \

            