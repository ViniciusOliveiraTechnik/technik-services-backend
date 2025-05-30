from rest_framework_simplejwt.tokens import AccessToken

from datetime import timedelta

class ActionToken(AccessToken):

    lifetime = timedelta(minutes=30)

    def __init__(self, action, user_id):
        super().__init__()

        self['action'] = action
        self['user_id'] = user_id