from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.exceptions import TokenError

from datetime import timedelta

class JwtUtil:

    @staticmethod
    def generate_tokens(user):

        refresh_token = RefreshToken.for_user(user)

        refresh_token.set_exp(lifetime=timedelta(days=30))

        refresh_token['mfa_verified'] = True

        return {'access_token': str(refresh_token.access_token), 'refresh_token': str(refresh_token)}
    
    @staticmethod
    def refresh(refresh_token):

        if not refresh_token:

            raise ValidationError({'refresh_token': ['Autenticação inválida. Faça o login novamente']})

        try:

            refresh_token = RefreshToken(refresh_token)

            return {'access_token': str(refresh_token.access_token)}
        
        except TokenError:

            raise ValidationError({'refresh_token': ['O refresh token é inválido ou expirado']})
