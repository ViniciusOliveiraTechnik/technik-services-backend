from accounts.serializers.password import PasswordForgotConfirmSerializer
from accounts.models import Account

from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError

class PasswordForgotConfirmService:

    def __init__(self, context = None):
        
        self.context = context or {}

    def execute(self, data, access_token):

        serializer = PasswordForgotConfirmSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data.get('password')

        try:

            access_token = AccessToken(access_token)

            action = access_token.get('action')

            if action != 'forgot_password':

                raise ValidationError({'token': ['O token fornecido não tem acesso a este serviço']})

            user_id = access_token.get('user_id')

            try:

                user = Account.objects.get(id=user_id)

                user.set_password(password)

                user.save()

                return {'message': 'Senha alterada com sucesso!'}

            except Account.DoesNotExist:

                raise ValidationError({'user': ['Usuário não encontrado']})

        except TokenError as err:

            raise ValidationError({'token': ['O token de acesso é inválido ou expirado']})