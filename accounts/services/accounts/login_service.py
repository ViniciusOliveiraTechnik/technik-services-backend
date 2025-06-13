from accounts.serializers import AccountLoginSerializer

from jwt_auth.utils import JwtUtil, OTPUtil, QrCodeUtil

from rest_framework_simplejwt.tokens import RefreshToken

from datetime import timedelta

class AccountLoginService:

    def __init__(self, context = None):

        self.context = context or {}
        self.jwt_util = JwtUtil()
        self.otp_util = OTPUtil()

    def execute(self, data):

        serializer = AccountLoginSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user')
        
        refresh_token = RefreshToken.for_user(user)
        refresh_token.set_exp(lifetime=timedelta(minutes=15))

        if not user.is_authenticated:

            if not user.otp_secret:

                user.otp_secret = self.otp_util.generate_otp_secret()

                user.save()

            totp_uri = self.otp_util.get_totp_uri(user.otp_secret, user.email)

            qr_code = QrCodeUtil(totp_uri).generate()

            refresh_token['action'] = 'mfa_setup'

            return {'access_token': str(refresh_token.access_token), 'refresh_token': str(refresh_token), 'qr_code': qr_code}
        
        refresh_token['action'] = 'mfa_validate'

        return {'access_token': str(refresh_token.access_token), 'refresh_token': str(refresh_token)}
