from accounts.serializers import PasswordForgotSerializer
from accounts.models import Account
from accounts.tasks import send_email_to_reset_password

from jwt_auth.tokens import ActionToken

class PasswordForgotService:

    def __init__(self, context = None):
        
        self.context = context or {}

    def execute(self, data):

        serializer = PasswordForgotSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')

        try:

            user = Account.objects.get(email=email)

            access_token = ActionToken(action='forgot_password').for_user(user)

            send_email_to_reset_password.delay(str(access_token), user.email)

        except Account.DoesNotExist:

            pass

        return {'message': 'Se as credenciais existirem, um link de restauração de senha será enviado à caixa de email'}