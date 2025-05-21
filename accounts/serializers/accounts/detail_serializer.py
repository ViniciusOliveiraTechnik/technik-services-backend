from rest_framework import serializers

from accounts.utils import PhoneUtil, CPFUtil
from accounts.models import Account

class AccountDetailSerializer(serializers.ModelSerializer):

    cpf = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()

    class Meta:

        model = Account
        exclude = ['password', 'otp_secret', 'hashed_cpf', 'encrypted_cpf', 'user_permissions', 'groups', 'is_superuser', 'last_login', 'is_staff']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        from accounts.services import AccountDetailService

        self.service = AccountDetailService(context=self.context)

    def get_cpf(self, obj: Account) -> str:
        """
        Get the masked CPF of the user.

        Args:
            obj (Account): The user instance.
        
        Returns:
            str: The masked CPF if the user is staff or the same user, otherwise returns a placeholder.
        """
        cpf_Util = CPFUtil()

        cpf = cpf_Util.decrypt(obj.encrypted_cpf)

        if self.service.can_view_sensitive(obj):

            return cpf_Util.mask(cpf) if cpf else 'Sem registro'
        
        return '***.***.***-**'
    
    def get_phone_number(self, obj: Account) -> str:
        """
        Get the masked phone number of the user.

        Args:
            obj (Account): The user instance.
        
        Returns:
            str: The masked phone number if the user is staff or the same user, otherwise returns a placeholder.
        """
        phone_Util = PhoneUtil()

        if not obj.phone_number:

            return 'Sem registro'

        if self.service.can_view_contacts(obj):

            return phone_Util.mask(obj.phone_number)
        
        return f'{obj.phone_number[:3]} *********{obj.phone_number[-2:]}'