from accounts.serializers import PasswordForgotRequestSerializer, PasswordForgotConfirmSerializer
from accounts.tokens import ActionToken
from accounts.models import Account
from accounts.tasks import send_email_to_reset_password, send_email_to_notify_password_change

from rest_framework.exceptions import NotFound, AuthenticationFailed

from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken, ExpiredTokenError

class PasswordForgotService:

    def __init__(self):
        pass

    def execute_request(self, data):

        serializer = PasswordForgotRequestSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')

        try:

            user = Account.objects.get(email=email)

            token = str(ActionToken(user, 'reset_password'))

            send_email_to_reset_password.delay(user.id, token)

        except Account.DoesNotExist:

            pass

        return {'message': 'Se as credenciais existirem, um link de restauração de senha será enviado à caixa de email'}
    
    def execute_confirm(self, data, token_param):

        if not token_param:

            raise AuthenticationFailed

        serializer = PasswordForgotConfirmSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data.get('password')

        try:

            token = UntypedToken(token_param)

            user_id = token.get('user_id')
            action = token.get('action')

            if action != 'reset_password':

                raise TokenError

            try:

                user = Account.objects.get(id=user_id)

                user.set_password(password)
                user.save()

                send_email_to_notify_password_change.delay(user.id)

                return {'message': 'Senha alterada com sucesso'}

            except Account.DoesNotExist:

                raise NotFound

        except (ExpiredTokenError, InvalidToken):

            raise InvalidToken