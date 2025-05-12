from rest_framework.permissions import BasePermission

from accounts.utils import PermissionsHelper

class IsInternalUser(BasePermission):

    message = 'Você não tem acesso à serviços corporativos internos'

    def has_permission(self, request, view):

        return PermissionsHelper(request.user).check_internal()
