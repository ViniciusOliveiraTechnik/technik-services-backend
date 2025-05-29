from accounts.models import Account
from accounts.serializers import AccountTwoFactorsSerializer
from accounts.utils import JWTUtil, OTPUtil

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError

from rest_framework.exceptions import ValidationError

class AccountTwoFactorsService:

    def __init__(self, context = None):
        
        self.context = context or {}
        self.jwt_util =JWTUtil()
        self.otp_util = OTPUtil()

    def execute(self, data, temporary_auth_token):

        serializer = AccountTwoFactorsSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        otp_code = serializer.validated_data.get('otp_code')
        
        try:
            
            temporary_auth_token = AccessToken(temporary_auth_token)

            user_id = temporary_auth_token.get('user_id')

            if not user_id:

                raise ValidationError({'validation': ['Não foi possível realizar a autenticação']})
            
            try:

                user = Account.objects.get(id=user_id)

                if not self.otp_util.verify_otp(otp_code, user.otp_secret):

                    raise ValidationError({'otp_code': ['O código de autenticação está incorreto ou expirado']})
                
                tokens = self.jwt_util.generate_tokens(user)

                return {'access_token': tokens['access'], 'refresh_token': tokens['refresh']}

            except Account.DoesNotExist:

                raise ValidationError({'not_found': ['Usuário não encontrado']})

        except TokenError as err:

            raise ValidationError({'token_error': [f'Não foi possível validar o token: {str(err)}']})