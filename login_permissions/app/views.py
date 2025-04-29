from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import UsuarioSerializer, IngressoSerializer, LoginSerializer
from .permission import isGestor, isGestorOuDono
from rest_framework.permissions import IsAuthenticated
from .models import Ingresso, Usuario
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer



# Listagem e criação de usuários
class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    # Qualquer autenticado pode fazer GET, mas só gestor pode fazer POST
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [isGestor()]

# Detalhar, atualizar e deletar ingresso
class IngressoRUDAPI(RetrieveUpdateDestroyAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer
    permission_classes = [isGestorOuDono]
    lookup_field = 'pk'


#somente gestores podem criar ingresso e todos autenticados podem visualizar
class IngresolistCreateApiView(ListCreateAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

    def get_permission(self):
        if self.request.method == "GET":
            return [IsAuthenticated] #allownAny -> todos poderiam visualizar
        return [IsGestor()]
