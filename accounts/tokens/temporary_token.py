from rest_framework_simplejwt.tokens import AccessToken

from datetime import timedelta

class TemporaryAccessToken(AccessToken):

    lifetime = timedelta(minutes=5)

    def __init__(self):
        super().__init__()

        self['2fa_verified'] = False
