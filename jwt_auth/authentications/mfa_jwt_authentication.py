from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken


class MFAJWTAuthentication(JWTAuthentication):

    expected_action = ['mfa_validate', 'mfa_setup']

    def authenticate(self, request):
        
        header = self.get_header(request)

        if not header:

            raise AuthenticationFailed('Invalid client', code='unauthorized')
        
        raw_token = self.get_raw_token(header)

        try:

            validated_token = self.get_validated_token(raw_token)

        except InvalidToken:

            raise AuthenticationFailed('Invalid or expired token', code='unauthorized')

        action = validated_token.get('action')

        if action not in self.expected_action:

            raise AuthenticationFailed('This tokens is not compatible', code='unauthorized')
        
        return self.get_user(validated_token), validated_token