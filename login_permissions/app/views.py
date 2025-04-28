from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializer import UsuarioSerializer
from .permission import isGestor
# Create your views here.
class UsuarioListCreateAPIView(ListCreateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [isGestor] #definindo que somente quem for gestor fará o post e get    