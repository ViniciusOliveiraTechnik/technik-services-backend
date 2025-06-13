from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError

from jwt_auth.serializers.auth import AuthOtpSerializer
from jwt_auth.utils import OTPUtil
from jwt_auth.utils import JwtUtil

from accounts.models import Account

class AuthMFAValidateService:

    def __init__(self, context = None):
        
        self.context = context or {}
        self.otp_util = OTPUtil()
        self.jwt_util = JwtUtil() 

    def execute(self, access_token, data):

        serializer = AuthOtpSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        otp_code = serializer.validated_data.get('otp_code')

        try:

            access_token = AccessToken(access_token)

            user_id = access_token.get('user_id')

            try:

                user = Account.objects.get(id=user_id)
                
                if not user.otp_secret:

                    raise ValidationError({'user': ['As configurações de dois fatores do usuário são inválidas']})

                if not self.otp_util.verify_otp(otp_code, user.otp_secret):

                    raise ValidationError({'otp_code': ['O código de autenticação é inválido ou expirado']})

                tokens = self.jwt_util.generate_tokens(user)

                return {'access_token': tokens['access_token'], 'refresh_token': tokens['refresh_token']}

            except Account.DoesNotExist:

                raise ValidationError({'user': ['Usuário não encontrado']})

        except TokenError:

            raise ValidationError({'token': ['O token de acesso é inválido ou expirado']})