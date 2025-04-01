from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import UsuarioDS16
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
def criar_usuario(request):
    
    #Obtendo os dados do json
    username = request.data.get('username')
    password = request.data.get('password')
    edv = request.data.get("EDV")
    born_date = request.data.get('data_nascimento')
    father = request.data.get('padrinho'),    
    surname = request.data.get("apelido")

    #Verificando se os dados obrigatorios foram passados corretamente.
    if not username or not password or not edv or not born_date:
        return Response({'Erro': "Campos obrigatorios imcompletos"}, status=status.HTTP_400_BAD_REQUEST)
    
    #verificando usuario ja existe
    if UsuarioDS16.objects.filter(username=username).exists():
        return Response({'Erro': f"username {username} já existe"}, status=status.HTTP_400_BAD_REQUEST)
    
    #Verificando se o EDV ja existe
    if UsuarioDS16.objects.filter(edv=edv).exists():
        return Response({'Erro': f'EDV {edv} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    #Criando seu usuário
    usuario = UsuarioDS16.objects.create_user(
        username=username,
        password=password,
        edv=edv,
        data_nascimento = born_date,
        padrinho = father,
        apelido = surname,
        email = f"{username}@boh.com" #cadastrando com a extensão 

    )
    #Retornando sucesso se o usuário for criado caso de tudo certo.
    return Response({"Mensagem": f"O usuario {username} foi criado com sucesso"}, status=status.HTTP_201_CREATED)


#logar 
@api_view(['POST'])
def logar_usuario(request):
    
    #pegando os dados do user
    username = request.data.get('username')
    password = request.data.get('password')

    #autenticando
    usuario = authenticate(username=username, password=password)

    #se usuario for verdadeiro, cria um novo token de acesso
    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({"acesso": str(refresh.access_token), 'refresh':str(refresh)}, status=status.HTTP_200_OK)#retornando o token de acesso e o o refresh do msm caso for expiradp
    else:
        return Response({"Erro": "Usuário ou/e senha incorretas"}, status=status.HTTP_401_UNAUTHORIZED)#Tratativa de erro 
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read(resquest):
    return Response({"Mensagem": "Ola DS16"}, status=status.HTTP_200_OK)

'''

{

"username":"Dorival cleber",
"password":"123",
"EDV": 12377,
"data_nascimento":"2024-06-15"

}

'''