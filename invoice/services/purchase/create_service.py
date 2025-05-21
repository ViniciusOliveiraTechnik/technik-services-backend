from invoice.utils.reader import ItauReaderUtil

class PurchaseCreateService:

    def __init__(self, file, invoice_instance, context=None, ):
    
        self.file = file
        self.invoice_instance = invoice_instance
        self.context = context or {}

        self.readers = {
            'Itaú': ItauReaderUtil(file=self.file, invoice_instance=self.invoice_instance)
        }

    def execute(self):

        return self.readers[self.invoice_instance.bank].extract()