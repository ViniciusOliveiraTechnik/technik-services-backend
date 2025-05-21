from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):

    message = 'Você não possui permissão para modificar esse cartão'

    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:

            return True
        
        return obj.account == request.user or request.user.is_staff