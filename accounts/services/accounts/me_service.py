from accounts.serializers import AccountDetailSerializer

class AccountMeService:

    def __init__(self, context = None):
        
        self.context = context or {}

    def execute(self, user):
        
        return AccountDetailSerializer(user, context=self.context).data