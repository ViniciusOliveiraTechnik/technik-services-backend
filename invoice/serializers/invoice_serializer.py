from rest_framework import serializers

from invoice.models import Invoice, Card

import mimetypes

class InvoiceUploadSerializer(serializers.Serializer):

    file = serializers.FileField(allow_empty_file=False)

    def validate_file(self, value):

        max_size_mb = 2
        
        if value.size > max_size_mb * 1024 * 1024:
            
            raise serializers.ValidationError(f"Arquivo muito grande. O tamanho máximo é {max_size_mb}MB.")

        valid_mimetypes = ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'text/csv']
        file_mime, _ = mimetypes.guess_type(value.name)

        if file_mime not in valid_mimetypes:
            
            raise serializers.ValidationError(f"Tipo de arquivo não suportado ({file_mime}). Tipos permitidos: {', '.join(valid_mimetypes)}")

        return value

class InvoiceDataSerializer(serializers.ModelSerializer):

    account = serializers.PrimaryKeyRelatedField(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:

        model = Invoice
        fields = '__all__'

    def validate(self, attrs):

        installment = attrs.get('installment', None)
        installments = attrs.get('installments', None)

        if not installment or not installments:
            
            raise serializers.ValidationError('Os valores associados à parcelas devem ser preenchidos corretamente')
        
        if installment > installments:

            raise serializers.ValidationError('O valor da parcela deve ser menor que o valor de parcelas')

        card_name = attrs.get('card')

        try:

            card_obj = Card.objects.select_related('account').get(name__iexact=card_name, is_active=True)
            
            attrs['account'] = card_obj.account

        except Card.DoesNotExist:
            
            raise serializers.ValidationError({'card': f'Cartão com nome "{card_name}" não encontrado.'})

        return attrs