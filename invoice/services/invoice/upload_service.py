from invoice.serializers.invoice import InvoiceUploadSerializer
from invoice.models import Invoice

class InvoiceUploadService:

    def __init__(self, context=None):
        
        self.context = context or {}

    def execute(self, data):

        serializer = InvoiceUploadSerializer(data=data, context=self.context)

        serializer.is_valid(raise_exception=True)

        return [serializer.save(), serializer.validated_data.get('file')]

