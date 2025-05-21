from rest_framework import serializers

from invoice.models import Card

class CardDetailSerializer(serializers.ModelSerializer):
    
    account_id = serializers.SerializerMethodField()
    account_name = serializers.SerializerMethodField()
    spent = serializers.SerializerMethodField()
    itens_count = serializers.SerializerMethodField()

    class Meta:

        model = Card
        fields = ['account_id', 'account_name', 'id', 'name', 'bank', 'spent', 'itens_count']
        read_only_fields = ['account_id', 'account_name', 'spent', 'itens_count', 'id']

    def get_account_id(self, obj):

        return obj.account.id
    
    def get_account_name(self, obj):

        return f'{obj.account.first_name} {obj.account.last_name}'
    
    def get_spent(self, obj):

        return obj.spent if obj.spent is not None else 0.0
    
    def get_itens_count(self, obj):

        return obj.itens_count if obj.itens_count is not None else 0