from accounts.models import Account
from accounts.serializers import AccountTwoFactorsSerializer, AccountDetailSerializer
from accounts.utils import JWTHelper, OTPHelper

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, ExpiredTokenError

from rest_framework.exceptions import NotFound, ValidationError

class AccountTwoFactorsService:

    def __init__(self, context=None):
        
        self.context = context or {}
        self.jwt_helper =JWTHelper()
        self.otp_helper = OTPHelper()

    def execute(self, data, auth):

        serializer = AccountTwoFactorsSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        otp_code = serializer.validated_data.get('otp_code')

        try:

            temp_access = AccessToken(auth)
            user_id = temp_access.get('user_id')

            try:

                user = Account.objects.get(id=user_id)

                if not self.otp_helper.verify_otp(otp_code, user.otp_secret):

                    raise ValidationError

                tokens = self.jwt_helper.generate_tokens(user)

                response_data = AccountDetailSerializer(user, context=self.context).data

                return {'access': tokens['access'], 'refresh': tokens['refresh'], 'user': response_data} 

            except Account.DoesNotExist:

                raise NotFound

        except (ExpiredTokenError, InvalidToken):

            raise InvalidToken