from jwt_auth.utils import JwtUtil

class RefreshTokenService:

    def __init__(self, context = None):
        
        self.context = context or {}
        self.auth_util = JwtUtil()

    def execute(self, refresh_token):

        return self.auth_util.refresh(refresh_token)

