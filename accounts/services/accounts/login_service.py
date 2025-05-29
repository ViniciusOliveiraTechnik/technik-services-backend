from accounts.serializers import AccountLoginSerializer
from accounts.tokens import TemporaryAccessToken

from accounts.utils import QrCodeUtil

from jwt_auth.utils.two_factors import OTPUtil

class AccountLoginService:

    def __init__(self, context = None):

        self.context = context or {}
        self.otp_util = OTPUtil()

    def execute(self, data):

        serializer = AccountLoginSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user')
        
        temp_token = TemporaryAccessToken.for_user(user)
        
        if not user.otp_secret:
            
            user.otp_secret = self.otp_util.generate_otp_secret()
            user.save()

        totp_uri = self.otp_util.get_totp_uri(user.otp_secret, user.email)

        qr_code_util = QrCodeUtil(totp_uri)

        qr_code_img = qr_code_util.generate()

        return {'access_token': str(temp_token), 'qr_code': qr_code_img}