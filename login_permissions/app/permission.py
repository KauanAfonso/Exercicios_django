from rest_framework.permissions import BasePermission


#Permissao se o usuario for o gestor
class isGestor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.colaborador == 'G'
    
#Permissão para um objeto em especifico
class isGestorOuDono(BasePermission):
    def has_object_permi(self,request,view,obj):
        if request.user.colaborador == 'G':
            return True
        return obj.usuario == request.user