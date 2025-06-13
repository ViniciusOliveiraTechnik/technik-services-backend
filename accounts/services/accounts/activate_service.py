from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken

from accounts.models import Account

class AccountActivateService:

    def __init__(self, context = None):
        
        self.context = context or {}

    def execute(self, access_token):
        
        try:

            access_token = AccessToken(access_token)

            user_id = access_token.get('user_id')

            try:

                user = Account.objects.get(id=user_id)

                if user.is_activated:

                    return {'message': 'Essa conta já está ativa'}

                user.is_activated = True

                user.save()

                return {'message': 'Conta ativada com sucesso!'}

            except Account.DoesNotExist:

                raise ValidationError({'user': ['Usuário não encontrado']})

        except TokenError:

            raise ValidationError({'token': ['O token de acesso é inváldo ou expirado']})