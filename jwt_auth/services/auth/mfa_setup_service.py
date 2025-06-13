from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.exceptions import ValidationError

from accounts.models import Account

from jwt_auth.serializers.auth import AuthOtpSerializer
from jwt_auth.utils import JwtUtil, OTPUtil


class AuthMFASetupService:

    def __init__(self, context = None):
        
        self.context = context or {}
        self.jwt_util = JwtUtil()
        self.otp_util = OTPUtil()

    def execute(self, access_token, data):
        
        try:
            
            access_token = AccessToken(access_token)

            user_id = access_token.get('user_id')

            try:

                user = Account.objects.get(id=user_id)

                serializer = AuthOtpSerializer(data=data)

                serializer.is_valid(raise_exception=True)

                otp_code = serializer.validated_data.get('otp_code')

                if not self.otp_util.verify_otp(otp_code, user.otp_secret):

                    raise ValidationError({'auth': ['O código de autenticação é inválido ou expirado']})

                user.is_authenticated = True

                user.save()
                
                tokens = self.jwt_util.generate_tokens(user)

                return {'access_token': tokens['access_token'], 'refresh_token': tokens['refresh_token']}
            
            except Account.DoesNotExist:

                raise ValidationError({'account': ['Usuário não encontrado']})

        except TokenError:

            raise ValidationError({'token': ['O token de acesso é inválido ou expirado']})
