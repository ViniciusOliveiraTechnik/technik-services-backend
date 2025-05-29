from rest_framework_simplejwt.tokens import AccessToken

from datetime import timedelta

class TemporaryToken(AccessToken):

    lifetime = timedelta(minutes=5)

    def __init__(self, token = None, verify = True):
        super().__init__(token, verify)

        self['2fa_verified'] = False