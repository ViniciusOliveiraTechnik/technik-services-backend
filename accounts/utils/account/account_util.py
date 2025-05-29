from rest_framework.exceptions import ValidationError

class AccountUtil:

    def __init__(self, account = None):
        
        self.account = account

    def get_object(self, pk):

        from accounts.models import Account

        try:

            return Account.objects.get(id=pk)

        except Account.DoesNotExist:

            raise ValidationError({'account': ['Usuário não encontrado']})