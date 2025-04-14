from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Pessoa
from .serializer import PessaoSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated #Verifica autenticacao


#Fazendo o get para pegar todos as pessoas
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obter_usuarios(request):
    #se methhod for get pegar todos os users
    if request.method == "GET":
        usuarios = Pessoa.objects.all()
        serializer = PessaoSerializer(usuarios, many=True)
        return Response({"Usuarios":serializer.data}, status=status.HTTP_200_OK)
    

#Fazendo o post de criar usuarios -> não utiliza o serializer de Pessoa
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def criar_usuario(request):
    
    #Pegando todos os dados dele via requisição
    username = request.data.get('username')
    password = request.data.get('password')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    numero_animais = request.data.get('numero_animais')
    

    #Verificando se as informações estão corretas para envio
    if not username or not password or not biografia or not telefone:
        return Response({'Erro': "Informações faltando"}, status=status.HTTP_400_BAD_REQUEST)
    
    #Verificando se user existe
    if Pessoa.objects.filter(username=username).exists():
        return Response({"ERRO: Usuário ja cadastrado"}, status=status.HTTP_409_CONFLICT)
    
    #Criando user
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

#Atualizando uma pessoa com PUT
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def atualizar_pessoa(request,pk):
    
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return Response("ERRO: Não encontrado", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PessaoSerializer(isinstance=pessoa, data=request.data) #Criando uma instancia da pessoa para lidar somente com ela e pegando os dados enviados
        if serializer.is_valid():
            serializer.save() #salvar no banco se for valido
            return Response({"Usuario atualizado": serializer.data}, status=status.HTTP_200_OK)
        
        return Response({'Erro': "Está faltando informações"}, status=status.HTTP_400_BAD_REQUEST)
        

#---------------EXCLUIR pessoa-------------------------
@api_view(["GET", 'DELETE']) #tive que pasar o get para delete funcionar 
@permission_classes([IsAuthenticated])
def excluir_pessoa(request,pk):
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return Response({f"ERRO: Não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    pessoa.delete() #Deleta pessoa 
    return Response({f"Usuario deletado: {pessoa}"}, status=status.HTTP_200_OK)


#-------------FAZER LOGIN---------------------------- 
@api_view(["POST"])
def fazer_login(request):
    
    #obtendo dados
    username = request.data.get('username')
    password = request.data.get('password')
    
    usuario = authenticate(username=username, password=password) #autenticando com um metodo proprio
    
    #Se o usuário logar
    if usuario:
        refresh=RefreshToken.for_user(usuario) #pegar o token
        return Response({f"acesso":str(refresh.access_token), "refresh": str(refresh)},  status=status.HTTP_200_OK) #retornar o token e refresh
    
    return Response({"Erro": "Usuário ou/e senha incorretas"}, status=status.HTTP_401_UNAUTHORIZED)#Tratativa de erro 