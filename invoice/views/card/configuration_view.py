from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from django.db.models import Sum, Count

from invoice.models import Card
from invoice.permissions import IsOwnerOrAdmin
from invoice.serializers.card import CardDetailSerializer
from invoice.paginations.card import CardStandardPagination

from accounts.permissions import IsInternalUser

from jwt_auth.permissions import IsTwoFactorsVerified

class CardConfigurationView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsTwoFactorsVerified, IsInternalUser, IsOwnerOrAdmin]

    pagination_class = CardStandardPagination
    serializer_class = CardDetailSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        
        card_id = self.kwargs.get('pk')

        return Card.objects \
               .select_related('account') \
               .annotate(
                    spent=Sum('purchases_card__value'),
                    itens_count=Count('purchases_card__id'),
               ) \
               .only(
                   'account__id',
                   'account__first_name',
                   'account__last_name'
                   ) \
               .filter(id=card_id)