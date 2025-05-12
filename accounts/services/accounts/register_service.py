from accounts.serializers import AccountRegisterSerializer, AccountDetailSerializer
from accounts.utils import OTPHelper
from accounts.models import Account

from typing import Dict, Any

class AccountRegisterService:

    def __init__(self, context=None):

        self.context = context or {}
        
    def execute(self, data):

        helper = OTPHelper()

        serializer = AccountRegisterSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        user.otp_secret = helper.generate_otp_secret()
        user.save()

        self.context['explicit_user'] = user

        return AccountDetailSerializer(user, context=self.context).data
    
    def create(self, validated_data: Dict[str, Any]):

        cpf = validated_data.pop('cpf')
        password = validated_data.pop('password')

        user = Account(**validated_data)

        user.set_password(password)
        user.set_cpf(cpf)

        user.save()

        return user
    
    def check_exists(self, field: str, value: Any):

        return Account.objects.filter(**{field: value}).exists()