from invoice.utils.reader import ItauReaderUtil
from invoice.serializers.purchase import PurchaseBaseSerializer

class PurchaseBulkCreateService:

    def __init__(self, file, invoice_instance, context = None):
        
        self.context = context or {}
        self.file = file
        self.invoice_instance = invoice_instance

        self.readers = {
            'Itaú': ItauReaderUtil(file=file, invoice_instance=invoice_instance),
        }

    def execute(self):

        queryset = self.readers[self.invoice_instance.bank].extract()

        return PurchaseBaseSerializer(queryset, many=True, context=self.context).data