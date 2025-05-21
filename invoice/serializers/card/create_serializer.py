from rest_framework import serializers

from accounts.models import Account

from invoice.models import Card

class CardCreateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Card
        fields = ['account', 'name', 'bank']

    def validate_account(self, value):

        return value
    
    def validate_name(self, value):

        return str(value).strip()
    
    def validate_bank(self, value):

        bank_choices = Card.BankChoices.values

        normalized_value = str(value).strip()

        if normalized_value not in bank_choices:

            raise serializers.ValidationError(f'O banco "{normalized_value}" não está na lista dos bancos permitidos. Bancos: {', '.join(bank_choices)}')

        return normalized_value