from invoice.serializers.purchase import PurchasesFilterSerializer
from invoice.services.purchase import PurchaseFilterService

class CardPurchasesService:

    def __init__(self, context = None):
        
        self.context = context or {}

    def execute(self, data, pk):

        serializer = PurchasesFilterSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        validated = serializer.validated_data

        extra_filters = {'card_id': pk}

        service = PurchaseFilterService(validated, extra_filters)

        return service.filter()