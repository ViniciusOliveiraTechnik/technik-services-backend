from rest_framework.permissions import BasePermission

class MFAActive(BasePermission):

    message = 'Autenticação de dois fatores pendente'

    def has_permission(self, request, view):

        access_token = request.auth

        return True if access_token and access_token.get('mfa_verified') else False