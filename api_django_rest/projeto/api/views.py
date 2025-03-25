from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from . import models
from .serializer import CategoriaSerializer, EventosSerializer, Evento_CategoriaSerializer
from .filter import Filtrar_Evento
from datetime import datetime,timedelta


'''
Funcão de criar evento, que é passado no corpo da requisição.
é passado para o serializer e se for valido é salvo. 

'''
@api_view(["POST"])
def criar_evento(request):
        if request.method == "POST":
            serializer = EventosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''

Funão que será capaz de obter todos os eventos, filtrar e ordenar.

'''
@api_view(["GET"])
def obter_eventos(request):
    try:
        filtro = Filtrar_Evento(request.query_params, queryset=models.Evento.objects.all()) #instanciando e passando o que foi passado na url
        #Pegando se houver na url e armazenando em uma variavel
        #se não ela recebe NONE
        limit = request.query_params.get('limit', None)
        order_by = request.query_params.get('ordering', None)
        proximo = request.query_params.get('proximos', None)
        #pegando todos os eventos
        eventos = models.Evento.objects.all()

        #Se tiver o filtro, então irá filtrar
        if filtro.is_valid():
            eventos = filtro.qs 
        
        if limit:
            try:
                limit = int(limit)#convertendo o limit como int
                eventos = models.Evento.objects.all()[:limit] #Os eventos são como listas, então cortará do começo da lista ao limit
            except:
                return Response({"Erro": "não encontrado"}, status=status.HTTP_400_BAD_REQUEST)
        
        if order_by:
            eventos = eventos.order_by('data') #ordenando pela data

        '''
        Proximo=TRUE -> calcula a data atual mais 7 dias
        '''
        if proximo:
            data_atual = datetime.now()
            data_futura = data_atual + timedelta(days=7) #Pegando a data atual e somando mais 7 dias
            eventos = eventos.filter(data__gte=data_atual, data__lte=data_futura) #filtra entre a data atual e a futura

        serializer = Evento_CategoriaSerializer(eventos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) #retornando todos os eventos
    except:
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    

'''
Obtendo um evento pelo Id específico
'''
@api_view(["GET"])
def obter_evento_especifico(request,pk):
    try:
        evento = models.Evento.objects.get(pk=pk) #pegando o ID
        serializer = Evento_CategoriaSerializer(evento, many=False) #many false pois só pega um valor
        return Response(serializer.data)
    
    except models.Evento.DoesNotExist:
        return Response({"Erro": "não encontrado"}, status=status.HTTP_404_NOT_FOUND)

'''
Deletar um evento por seu id
'''
@api_view(["DELETE"])
def excluir_evento(request,pk):
    try:
        evento = models.Evento.objects.get(pk=pk)#pegando o ID
        evento.delete()
        return Response({"Reposta": "Evento Deletado com Sucesso!"}) #Caso for um sucesso irá retornar essa mesnagem
    except models.Evento.DoesNotExist:
        return Response({"Erro": "não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
'''

Função para atualizar o evento por meio do id

'''
@api_view(["PUT"])
def atulizar_evento(request,pk):
    if request.method == 'PUT':
        try:
            evento = models.Evento.objects.get(pk=pk)
            serializer = EventosSerializer(evento, data=request.data) #serealizando o que foi passado no corpo da requisição
        except models.Evento.DoesNotExist:
            return Response({"Erro": "não encontrado"}, status=status.HTTP_404_NOT_FOUND) #Erro not found se não encontrar o id
             
    if serializer.is_valid():
        serializer.save()#salva se o serializer for correto
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'mensagem': "algo deu erro"}, status=status.HTTP_400_BAD_REQUEST)