from rest_framework.permissions import BasePermission

class IsTwoFactorsVerified(BasePermission):

    message = 'Autenticação de dois fatores pendente'

    def has_permission(self, request, view):

        access_token = request.auth

        return True if access_token and access_token.get('2fa_verified') else False