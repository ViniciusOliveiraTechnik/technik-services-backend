from accounts.models import Account

from jwt_auth.utils.two_factors import OTPUtil

from rest_framework.exceptions import NotFound, NotAuthenticated

class AccountRefreshOtpService:

    def __init__(self):
        
        self.Util = OTPUtil()

    def execute(self, pk):
        
        try:

            user = Account.objects.get(id=pk)
            
            user.otp_secret = self.Util.generate_otp_secret()
            user.save(update_fields=['otp_secret'])

            return {'message': 'Chave de autenticação atualizada com sucesso'}

        except Account.DoesNotExist:

            raise NotFound