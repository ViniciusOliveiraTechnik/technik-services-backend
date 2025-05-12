from rest_framework.permissions import BasePermission

class TwoFactorsValidated(BasePermission):

    message = 'Autentificação de dois fatores pendente'

    def has_permission(self, request, view):
        
        token = request.auth

        return token and token.get('2fa_verified', False) is True