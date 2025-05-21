from invoice.serializers.purchase import PurchasesFilterSerializer
from invoice.services.purchase import PurchaseFilterService

class PurchaseListService:

    def __init__(self, context = None):
        
        self.context = context or {}

    def execute(self, data):

        serializer = PurchasesFilterSerializer(data=data, context=self.context)

        serializer.is_valid(raise_exception=True)

        validated = serializer.validated_data

        service = PurchaseFilterService(validated)

        return service.filter()