from accounts.serializers import AccountRegisterSerializer
from accounts.tasks import send_email_to_activate_account

from jwt_auth.utils import JwtUtil
from jwt_auth.tokens import ActionToken

class AccountRegisterService:

    def __init__(self, context = None):

        self.context = context or {}
        self.jwt_util = JwtUtil()
        
    def execute(self, data):

        serializer = AccountRegisterSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        
        action_token = ActionToken(action='activate_account').for_user(user)
        
        send_email_to_activate_account.delay(str(action_token), user.email)
        
        return {'message': 'Conta criada com sucesso!'}