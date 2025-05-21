from rest_framework.permissions import BasePermission

from accounts.utils import PermissionsUtil

class IsInternalUser(BasePermission):

    message = 'Você não tem acesso à serviços corporativos internos'

    def has_permission(self, request, view):

        return PermissionsUtil(request.user).check_internal()
