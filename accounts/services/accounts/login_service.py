from accounts.serializers import AccountLoginSerializer, AccountDetailSerializer
from accounts.tokens import AuthenticationToken
from accounts.utils import OTPUtil, generate_totp_qrcode

class AccountLoginService:

    def __init__(self, context=None):

        self.context = context or {}

    def execute(self, data):

        Util = OTPUtil()

        serializer = AccountLoginSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user')

        temp_token = AuthenticationToken.for_user(user)

        if not user.otp_secret:
            
            user.otp_secret = Util.generate_otp_secret()
            user.save()

        totp_uri = Util.get_totp_uri(user.otp_secret, user.email)

        qr_code = generate_totp_qrcode(totp_uri)

        self.context['explicit_user'] = user

        response_data = AccountDetailSerializer(user, context=self.context).data

        return {'access': str(temp_token), 'qr_code': qr_code, 'user': response_data}