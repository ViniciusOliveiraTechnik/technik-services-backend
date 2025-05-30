from rest_framework import serializers

from accounts.models import Account
from accounts.utils import AccountUtil, CPFUtil, PhoneUtil

class AccountRegisterSerializer(serializers.ModelSerializer):

    cpf = serializers.CharField(required=True, write_only=True, min_length=11, max_length=14)
    same_password = serializers.CharField(required=True, min_length=10)

    class Meta:

        model = Account
        fields = ['first_name', 'last_name', 'email', 'password', 'same_password', 'phone_number', 'cpf']

        extra_kwargs = {

            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'password': {'required': True, 'write_only': True, 'min_length': 10},
            'phone_number': {'required': True},

        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.account_util = AccountUtil()

    def validate_email(self, value):

        email = str(value).strip()

        if  self.account_util.check_exists('email', email):

            raise serializers.ValidationError('Este email é inválido')
        
        return email
    
    def validate_cpf(self, value):

        secure_error = 'O CPF inserido é inválido'

        cpf_util = CPFUtil()

        cpf = cpf_util.normalize(value)

        hashed_cpf = cpf_util.create_hash(cpf)

        if self.account_util.check_exists('hashed_cpf', hashed_cpf):

            raise serializers.ValidationError(secure_error)

        if not cpf_util.validate(cpf):

            raise serializers.ValidationError(secure_error)
        
        return cpf
    
    def validate(self, attrs):
        
        ### Password Verification ###

        password = str(attrs.get('password')).strip()

        same_password = str(attrs.get('same_password')).strip()

        if password != same_password:

            raise serializers.ValidationError('As senhas devem coincidir')

        ### Phone Number Verification ###

        secure_error = 'O número de contato é inválido'

        phone_number = str(attrs.get('phone_number')).strip()
        
        phone_number_region = str(attrs.get('phone_number_region', 'BR')).strip()

        if not phone_number:

            raise serializers.ValidationError(secure_error)

        phone_util = PhoneUtil(phone_number_region)

        phone_number = phone_util.normalize(phone_number)

        if self.account_util.check_exists('phone_number', phone_number):

            raise serializers.ValidationError(secure_error)
        
        attrs['phone_number'] = phone_number

        ### Returning Attrs ###

        return attrs
    
    def create(self, validated_data):
                
        return self.account_util.create(validated_data)

    Account.objects.filter(phone_number="+5519998122294")

