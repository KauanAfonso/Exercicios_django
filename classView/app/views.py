from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Piloto, Carro
from .serializers import PilotoSerializer, CarroSerializer
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

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
