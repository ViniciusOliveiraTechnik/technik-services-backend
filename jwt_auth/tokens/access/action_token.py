from rest_framework_simplejwt.tokens import AccessToken

from datetime import timedelta

class ActionToken(AccessToken):

    lifetime = timedelta(minutes=15)

    def __init__(self, token = None, verify = True, action = ""):
        super().__init__(token, verify)

        self['action'] = action