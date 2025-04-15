from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Piloto, Carro
from .serializers import PilotoSerializer, CarroSerializer
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#Paginação
class PilotoPaginacao(PageNumberPagination):
    page_size = 5 #definindo quanto é o default de elementos
    page_size_query_param = 'page_size' # -> define pela url a qtd de elementos pegar
    max_page_size = 10 #definindo o maximo de elementos

#GET e POST -> essa classe herda listCreateAPiView que permite esses methodos
class PilotoListCreateAPIView(ListCreateAPIView):
    #queryset e serializer_class -> nomes reservados para isso
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPaginacao

    #descricao da api no swwaget
    @swagger_auto_schema(
            operation_description = "lista todos os pilotos de formula 1",
            responses={
                #repostas possiveis
                200:PilotoSerializer(many=True),
                400:"Error"
            },
            manual_parameters=[
                openapi.Parameter(
                    'nome',
                    openapi.IN_QUERY,
                    description='Filtrar pelo nome do piloto',
                    type=openapi.TYPE_STRING
                )
            ],
    )

    #Chamando a classe pai para a descricao ficar em cima do enpoint do swwager
    def get(self, request, *args, **kwargs ):
        return super().get(request, *args, **kwargs)
    

    #Fazendo descricao para o post
    @swagger_auto_schema(
            operation_description='Cria um novo piloto',
            request_body= PilotoSerializer,
            responses={
                201:PilotoSerializer,
                400:"ERROO"
            }
    )
    
    #Chamando a classe pai para a descricao ficar em cima do enpoint do swwager
    def post(self, request, *args, **kwargs ):
        return super().get(request, *args, **kwargs)
    
    

    #Filtrando por nome do piloto
    def get_queryset(self):
        queryset = super().get_queryset() #super chama a classe piloListCreateApiView, e chamando para ele o method 5get_queryset()
        nome = self.request.query_params.get('nome') #pegando o nome pelo url
        if nome:
            queryset = queryset.filter(nome__icontains=nome)#icontains -> ignorando variações ex: "joão", "João", "JOÃO"
        return queryset
    
    #criando uma validação
    def perform_create(self, serializer):
        if serializer.validated_data['equipe'] != "DS16" and serializer.validated_data['classificacao'] <=5: #somente se a equipe for ds16 pode ficar entre os 5
            raise serializers.ValidationError('Somente a DS16 deve ficar entre os 5')
        serializer.save()


class PilotoRetriveUpdateDestroyAPIview(RetrieveUpdateDestroyAPIView): #consultar , deletar e Selecionar
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field = 'pk' #Campo que será passado na url

    #----------------------------------------------------------------DELETE----------------------------------------
    @swagger_auto_schema(
            operation_description = "Exlcuir o piloto por id",
            responses={
                #repostas possiveis
                200:PilotoSerializer(many=True),
                404:"Not Found",
                400:"Error"
            }
    )

    #Chamando a classe pai para a descricao ficar em cima do enpoint do swwager
    def delete(self, request, *args, **kwargs ):
        return super().get(request, *args, **kwargs)
    


    #----------------------------------------------------------------GET----------------------------------------
    @swagger_auto_schema(
            operation_description = "Obter um piloto por id",
            responses={
                #repostas possiveis
                200:PilotoSerializer(many=True),
                404:"Not Found",
                400:"Error"
            }
    )

    #Chamando a classe pai para a descricao ficar em cima do enpoint do swwager
    def get(self, request, *args, **kwargs ):
        return super().get(request, *args, **kwargs)
    

    

    #----------------------------------------------------------------PUT----------------------------------------
    @swagger_auto_schema(
            operation_description = "Atualiza todos os dados de um piloto por id",
            request_body= PilotoSerializer,
            responses={
                #repostas possiveis
                200:PilotoSerializer(many=True),
                404:"Not Found",
                400:"Error"
            }
    )

    #Chamando a classe pai para a descricao ficar em cima do enpoint do swwager
    def put(self, request, *args, **kwargs ):
        return super().get(request, *args, **kwargs)
    



    #----------------------------------------------------------------PATCH----------------------------------------
    @swagger_auto_schema(
            operation_description = "Atualiza no minimo um dado de um piloto por id",
            request_body= PilotoSerializer,
            responses={
                #repostas possiveis
                200:PilotoSerializer(many=True),
                404:"Not Found",
                400:"Error"
            }
    )

    #Chamando a classe pai para a descricao ficar em cima do enpoint do swwager
    def patch(self, request, *args, **kwargs ):
        return super().get(request, *args, **kwargs)


#Fazendo para carros
class CarroListCreateAPIView(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer 

    
    def get_queryset(self):
        queryset = super().get_queryset()
        marca = self.request.query_params.get("marca")
        if marca:
            queryset = queryset.filter(marca__icontains=marca) 
        return queryset
