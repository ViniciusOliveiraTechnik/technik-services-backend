from rest_framework.permissions import BasePermission

class IsActive(BasePermission):

    message = 'Sua conta não está ativa. Ative-a para acessar este recurso'

    def has_permission(self, request, view):
        
        if request.user.is_active:

            return True
        
        return False