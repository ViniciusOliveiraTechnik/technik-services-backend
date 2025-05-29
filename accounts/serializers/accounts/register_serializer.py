# from django.contrib.auth.password_validation import validate_password
# from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework import serializers

from accounts.utils import PhoneUtil, CPFUtil
from accounts.models import Account

from typing import Any, Dict

class AccountRegisterSerializer(serializers.ModelSerializer):

    cpf = serializers.CharField(required=True, write_only=True, min_length=11, max_length=14)
    repeat_password = serializers.CharField(required=True, write_only=True, min_length=10)

    class Meta:

        model = Account
        fields = ['first_name', 'last_name', 'email', 'password', 'repeat_password', 'phone_number', 'cpf']

        extra_kwargs = {

            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'password': {'required': True, 'write_only': True, 'min_length': 10},
            'phone_number': {'required': True}

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        from accounts.services import AccountRegisterService
        self.service = AccountRegisterService()

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate the input data for user registration.

        Args:
            data (Dict[str, Any]): The input data to validate.
        
        Returns:
            Dict[str, Any]: The validated data.
        
        Raises:
            serializers.ValidationError: If any validation fails.
        """
        if data["password"] != data["repeat_password"]:

            raise serializers.ValidationError('As senhas devem coincidir')

        phone_number = str(data.get('phone_number')).strip()
        phone_number_region = str(data.get('phone_number_region', 'BR')).strip()

        if not phone_number:

            raise serializers.ValidationError('As credenciais de contato não foram passadas corretamente')

        phone_Util = PhoneUtil(default_region=phone_number_region)
        
        normalized_phone = phone_Util.normalize(phone_number)

        if self.service.check_exists('phone_number', normalized_phone):

            raise serializers.ValidationError('O número de contato não pode ser cadastrado')
        
        data['phone_number'] = phone_number

        return data

    def validate_email(self, value: str) -> str:
        """
        Validate the email field to ensure it is unique.

        Args:
            value (str): The email address to validate.

        Returns:
            str: The validated email address.
        
        Raises:
            serializers.ValidationError: If the email address already exists.
        """
        value = str(value).strip()

        if self.service.check_exists('email', value):

            raise serializers.ValidationError('Não foi possível concluir o cadastro com os dados fornecidos')
        
        return value

    def validate_cpf(self, value: str) -> str:
        """
        Validate the CPF field to ensure it is unique.

        Args:
            value (str): The CPF to validate.
        
        Returns:
            str: The validated CPF.
        
        Raises:
            serializers.ValidationError: If the CPF already exists.
        """
        value = str(value).strip()

        cpf_Util = CPFUtil()

        if not cpf_Util.validate(value):

            raise serializers.ValidationError('CPF inválido')

        normalized_cpf = cpf_Util.normalize(value)

        hashed_cpf = cpf_Util.create_hash(normalized_cpf)

        if self.service.check_exists('hashed_cpf', hashed_cpf):

            raise serializers.ValidationError('Não foi possível concluir o cadastro com os dados fornecidos')
        
        return normalized_cpf

    # def validate_password(self, value: str) -> str:
    #     """
    #     Validate password complexity.
    #     """
    #     value = str(value).strip()

    #     user_data = {
    #         'first_name': self.initial_data.get('first_name', ''),
    #         'last_name': self.initial_data.get('last_name', ''),
    #         'email': self.initial_data.get('email', '')
    #     }

    #     if not any(user_data.values()):
    #         raise serializers.ValidationError("Nome, sobrenome ou email não foram fornecidos corretamente.")

    #     user = Account(**user_data)

    #     try:

    #         validate_password(password=value, user=user)

    #     except DjangoValidationError as err:

    #         raise serializers.ValidationError(err.messages)
        
    #     return value

    def create(self, validated_data: Dict[str, Any]):

        return self.service.create(validated_data)