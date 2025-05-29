from rest_framework_simplejwt.tokens import Token

from datetime import timedelta

class ActionToken(Token):

    token_type = 'action'
    lifetime = timedelta(minutes=10)

    def __init__(self, user_id, action_type: str = ''):
        super().__init__()

        self['user_id'] = str(user_id)
        self['action_type'] = action_type