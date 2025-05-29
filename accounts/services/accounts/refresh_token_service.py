from rest_framework.exceptions import AuthenticationFailed, ValidationError

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

class AccountRefreshTokenService:

    def __init__(self, context = None):
        
        self.context = context or {}

    def execute(self, refresh_token):

        if not refresh_token:

            raise ValidationError({'refresh_token': ['Autenticação inválida. Faça o login novamente']})
        
        try:

            refresh_token = RefreshToken(refresh_token)

            return {'access_token': str(refresh_token.access_token)}
        
        except TokenError:

            raise ValidationError({'token': ['O refresh token está expirado ou é inválido']})