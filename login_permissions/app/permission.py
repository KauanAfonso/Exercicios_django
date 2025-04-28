from rest_framework.permissions import BasePermission


#Permissao se o usuario for o gestor
class isGestor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.colaborador == 'G'