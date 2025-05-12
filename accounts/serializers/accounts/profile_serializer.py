from rest_framework import serializers

from accounts.utils import PhoneHelper, CPFHelper
from accounts.models import Account

from typing import Any

class AccountProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = Account
        exclude = ['password', 'hashed_cpf', 'encrypted_cpf', 'otp_secret']

    def _verify_existent_field(self, field: str, value: Any) -> bool:

        if not field or not value:
            raise ValueError('Os parâmetros devem ser passados corretamente')
        
        return Account.objects.filter(**{field: value}).exists()
    
    def validate_cpf(self, value):

        helper = CPFHelper()

        try:
            helper.validate(value)

        except ValueError:
            raise serializers.ValidationError('O CPF inserido é inválido ou não existe')

        normalized_cpf = helper.normalize(value)

        hashed_cpf = helper.create_hash(normalized_cpf)
        
        query = Account.objects.filter(cpf_hash=hashed_cpf)

        if self.instance:
            
            query = query.exclude(id=self.instance.id)

        if query.exists():

            raise serializers.ValidationError('As credenciais inseridas são inválidas')

        return normalized_cpf

    def validate_email(self, value):

        email = str(value).strip()
        
        query = Account.objects.filter(email=email)

        if self.instance:

            query = query.exclude(id=self.instance.id)

        if query.exists():

            raise serializers.ValidationError('Já há uma conta vinculada à este email')
        
        return email
    
    def validate_phone_number(self, value):
    
        phone_number = str(value).strip()

        phone_number_region = self.initial_data.get('phone_number_region', 'BR')

        phone_helper = PhoneHelper(default_region=phone_number_region)

        normalized_phone = phone_helper.normalize(phone_number)

        query = Account.objects.filter(phone_number=normalized_phone)

        if self.instance:

            query = query.exclude(id=self.instance.id)

        if query.exists():

            raise serializers.ValidationError('Já há uma conta vinculada à este contato')

        return normalized_phone