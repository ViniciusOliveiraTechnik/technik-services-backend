from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken

class JWTSetupAuthentication(JWTAuthentication):

    expected_action = 'auth_setup'

    def authenticate(self, request):

        header = self.get_header(request)

        if not header:

            raise AuthenticationFailed('Não foi possível validar o cliente')
        
        raw_token = self.get_raw_token(header=header)

        try:

            validated_token = self.get_validated_token(raw_token)

        except InvalidToken:

            raise AuthenticationFailed('Token inválido ou expirado', code='invalid_token')

        action = validated_token.get('action')

        if action != self.expected_action:

            raise AuthenticationFailed('Token não autorizado para este recurso', code='unauthorized') 
        
        return self.get_user(validated_token), validated_token
