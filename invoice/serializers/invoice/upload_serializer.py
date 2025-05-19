from rest_framework import serializers

from invoice.models import Invoice

ALLOWED_TYPES = [

    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",  # .xlsx
    "application/vnd.ms-excel",  # .xls
    "text/csv"  # .csv
    
]

class InvoiceUploadSerializer(serializers.Serializer):

    file = serializers.FileField(required=True)
    invoice_date = serializers.DateField(required=True)
    bank = serializers.CharField(required=True)

    def validate_file(self, value):

        content_type = value.content_type

        if content_type not in ALLOWED_TYPES:

            raise serializers.ValidationError(f'O tipo do arquivo não é compatível. Tipos compatíveis: {', '.join(ALLOWED_TYPES)}')
        
        if value.size > 10 * 1024 * 1024:

            raise serializers.ValidationError('O tamanho do arquivo não pode ultrapassar 10MB')
        
        return value
    
    def validate_invoice_date(self, value):

        current_invoice = Invoice.objects.filter(
            invoice_date__year=value.year, 
            invoice_date__month=value.month)

        if current_invoice.exists():
            
            current_invoice.delete()
    
        return value
    
    def validate_bank(self, value):

        bank_choices = Invoice.BankChoices.values

        if value not in bank_choices:

            raise serializers.ValidationError(f'O banco {value} não é um banco válido. Bancos aceitos: {', '.join(bank_choices)}')
        
        return value
    
    def create(self, validated_data):

        file = validated_data.pop('file')

        invoice = Invoice.objects.create(**validated_data)

        return invoice

