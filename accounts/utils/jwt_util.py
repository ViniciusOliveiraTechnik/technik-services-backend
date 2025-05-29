from datetime import timedelta

from rest_framework_simplejwt.tokens import RefreshToken

class JWTUtil:

    def __init__(self):
        pass

    def generate_tokens(self, user):

        refresh = RefreshToken.for_user(user)
        refresh.set_exp(lifetime=timedelta(days=30))

        refresh['email'] = user.email
        refresh['2fa_verified'] = True

        return {'refresh': str(refresh), 'access': str(refresh.access_token)}
