from rest_framework.exceptions import ValidationError

from .cpf_util import CPFUtil

class AccountUtil:

    def __init__(self, account = None):
        
        self.account = account
        self.cpf_util = CPFUtil()

    def get_object(self, pk):

        from accounts.models import Account

        try:

            return Account.objects.get(id=pk)

        except Account.DoesNotExist:

            raise ValidationError({'account': ['Usuário não encontrado']})
        
    def check_exists(self, field, value):

        from accounts.models import Account

        return Account.objects \
        .filter(**{field: value}) \
        .only('id') \
        .exists()

    def create(self, validated_data):

        from accounts.models import Account

        cpf = validated_data.pop('cpf')

        password = validated_data.pop('password')

        del validated_data['same_password']

        user = Account(**validated_data)

        user.encrypted_cpf = self.cpf_util.encrypt(cpf)

        user.hashed_cpf = self.cpf_util.create_hash(cpf)

        user.set_password(password)

        user.save()

        return user


