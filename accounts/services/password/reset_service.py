from accounts.serializers import PasswordResetSerializer
from accounts.utils import AccountUtil

class PasswordResetService:

    def __init__(self):
        
        self.account_util = AccountUtil()

    def execute(self, data, pk):

        user = self.account_util.get_object(pk)

        serializer = PasswordResetSerializer(user, data=data)

        serializer.is_valid(raise_exception=True)

        new_password = serializer.validated_data.get('new_password')

        user.set_password(new_password)

        user.save()
        
        return {'message': 'Senha alterada com sucesso'}
