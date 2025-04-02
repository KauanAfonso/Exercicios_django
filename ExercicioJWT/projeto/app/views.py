from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import Pessoa
from .serializer import PessaoSerializer

# Create your views here.
@api_view(['GET'])
def obter_usuarios(request):
    if request.method == "GET":
        usuarios = Pessoa.objects.all()
        serializer = PessaoSerializer(usuarios, many=True)
        return Response({"Usuarios":serializer.data}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def criar_usuario(request):
    
    username = request.data.get('username')
    password = request.data.get('password')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    numero_animais = request.data.get('numero_animais')
    
    if not username or not password or not biografia or not telefone:
        return Response({'Erro': "Informações faltando"}, status=status.HTPP_400_BAD_REQUEST)
        
    if Pessoa.objects.filter(username=username).exists():
        return Response({"ERRO: Usuário ja cadastrado"}, status=status.HTTP_409_CONFLICT)
    
    pessoa = Pessoa.objects.create_user(
        username=username,
        password=password,
        biografia = biografia,
        idade = idade,
        telefone = telefone,
        endereco = endereco,
        escolaridade = escolaridade,
        numero_animais = numero_animais,
        email= f'{username}@kauan.com'
    )

    return Response(f"Usuário criado: {pessoa}", status=status.HTTP_201_CREATED)


