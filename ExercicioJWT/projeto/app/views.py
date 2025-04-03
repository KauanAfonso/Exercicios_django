from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Pessoa
from .serializer import PessaoSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

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

@api_view(['DELETE', "PUT"])
def atualizar_pessoa(request,pk):
    
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return Response("ERRO: Não encontrado", status=status.HTTP_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PessaoSerializer(pessoa, many=False)
        return Response({f"Usuario atualizado": serializer.data}, status.HTTP_200_OK )
        


@api_view(['DELETE', 'GET'])
@permission_classes([IsAuthenticated])
def excluir_pessoa(request,pk):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return Response({f"ERRO: Não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    pessoa.delete()
    return Response({f"Usuario deletado: {pessoa}"}, status=status.HTTP_200_OK)
    
@api_view(["POST"])
def fazer_login(request):
    
    username = request.data.get('username')
    password = request.data.get('password')
    
    usuario = authenticate(username=username, password=password)
    
    if usuario:
        refresh =RefreshToken.for_user(usuario)
        return Response({f"acesso":str(refresh.access_token), "refresh": str(refresh)},  status=status.HTTP_200_OK)
    else:
        return Response({"Erro": "Usuário ou/e senha incorretas"}, status=status.HTTP_401_UNAUTHORIZED)#Tratativa de erro 