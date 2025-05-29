from accounts.models import Account
from accounts.utils import PermissionsUtil

class AccountDetailService:

    def __init__(self, context = None):

        self.context = context or {}

    def get_request_user(self):
        request = self.context.get('request', None)
        return getattr(request, 'user', None) if request else None

    def get_explicit_user(self):
        request = self.context.get('request', None)
        return getattr(request, 'explicit_user', None) if request else None

    def can_view_contacts(self, obj: Account) -> bool:

        request_user = self.get_request_user()

        permission_util = PermissionsUtil(request_user)

        if request_user:

            if request_user.id == obj.id or request_user.is_staff:

                return True

            if permission_util.check_internal():

                return True

        return False
    
    def can_view_sensitive(self, obj):

        request_user = self.get_request_user()
        explicit_user = self.get_explicit_user()

        if request_user:

            if request_user.id == obj.id or request_user.is_staff:

                return True

        if explicit_user:

            if explicit_user.id == obj.id:

                return True

        return False