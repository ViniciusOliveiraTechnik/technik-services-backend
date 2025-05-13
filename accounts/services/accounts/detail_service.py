from accounts.models import Account
from accounts.utils import PermissionsHelper

class AccountDetailService:

    def __init__(self, context=None):

        self.context = context or {}

    def _get_request_user(self):

        request = self.context.get('request')

        return getattr(request, 'user', None)

    def can_view_contacts(self, obj: Account) -> bool:

        request_user = self._get_request_user()

        explicit_user = self.context.get('explicit_user')
        
        if request_user:

            if request_user.id == obj.id or request_user.is_staff:

                return True

            if PermissionsHelper(request_user).check_internal():

                return True

        if explicit_user and explicit_user.id == obj.id:

            return True
        
        return False
    
    def can_view_sensitive(self, obj: Account) -> bool:

        request_user = self._get_request_user()

        explicit_user = self.context.get('explicit_user')

        if request_user:

            if request_user.id == obj.id or request_user.is_staff:

                return True
        
        if explicit_user and explicit_user.id == obj.id:

            return True
        
        return False