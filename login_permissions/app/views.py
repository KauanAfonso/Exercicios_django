from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import UsuarioSerializer, IngressoSerializer
from .permission import IsGestor, IsGestorOuDono
from rest_framework.permissions import IsAuthenticated
from .models import Ingresso, Usuario

# Listagem e criação de usuários
class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    # Qualquer autenticado pode fazer GET, mas só gestor pode fazer POST
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]

# Detalhar, atualizar e deletar ingresso
class IngressoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer
    permission_classes = [IsGestorOuDono]
    lookup_field = 'pk'
