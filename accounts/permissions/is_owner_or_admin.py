from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):

    message = "Você não possui permissões para editar este usuário"

    def has_object_permission(self, request, view, obj):

        # Only allow GET, HEAD and OPTIONS methods
        if request.method in SAFE_METHODS:

            return True 
        
        return obj == request.user or request.user.is_staff