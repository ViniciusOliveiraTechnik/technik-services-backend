from rest_framework import serializers

from accounts.utils import PhoneHelper, CPFHelper
from accounts.models import Account

class AccountDetailSerializer(serializers.ModelSerializer):

    cpf = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()

    class Meta:

        model = Account
        exclude = ['password', 'otp_secret', 'hashed_cpf', 'encrypted_cpf', 'user_permissions', 'groups', 'is_superuser', 'last_login', 'is_staff']

    def get_cpf(self, obj: Account) -> str:
        """
        Get the masked CPF of the user.

        Args:
            obj (Account): The user instance.
        
        Returns:
            str: The masked CPF if the user is staff or the same user, otherwise returns a placeholder.
        """
        from accounts.services import AccountDetailService

        service = AccountDetailService(self.context)

        cpf_helper = CPFHelper()

        cpf = cpf_helper.decrypt(obj.encrypted_cpf)

        if service.can_view_sensitive(obj):

            return cpf_helper.mask(cpf) if cpf else 'Sem registro'
        
        return '***.***.***-**'
    
    def get_phone_number(self, obj: Account) -> str:
        """
        Get the masked phone number of the user.

        Args:
            obj (Account): The user instance.
        
        Returns:
            str: The masked phone number if the user is staff or the same user, otherwise returns a placeholder.
        """
        from accounts.services import AccountDetailService

        service = AccountDetailService(self.context)

        phone_helper = PhoneHelper()

        if not obj.phone_number:

            return 'Sem registro'

        if service.can_view_contacts(obj):

            return phone_helper.mask(obj.phone_number)
        
        return f'{obj.phone_number[:3]} *********{obj.phone_number[-2:]}'