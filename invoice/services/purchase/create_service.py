from invoice.utils import ItauReaderHelper

class PurchaseCreateService:

    def __init__(self, file, invoice_instance, context=None, ):
    
        self.file = file
        self.invoice_instance = invoice_instance
        self.context = context or {}

        self.readers = {
            'Itaú': ItauReaderHelper(file=self.file, invoice_instance=self.invoice_instance)
        }

    def execute(self):

        return self.readers[self.invoice_instance.bank].extract()