from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from . import models
from .serializer import CategoriaSerializer, EventosSerializer, Evento_CategoriaSerializer


@api_view(["POST"])
def criar_evento(request):
        if request.method == "POST":
            serializer = EventosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def obter_eventos(request):
    try:
        evento = models.Evento.objects.all()
        serializer = Evento_CategoriaSerializer(evento ,many=True)
        return Response(serializer.data) #retornando todos os eventos
    except:
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def obter_evento_especifico(request,pk):
    try:
        evento = models.Evento.objects.get(pk=pk)
        serializer = Evento_CategoriaSerializer(evento, many=False)
        return Response(serializer.data)
    
    except models.Evento.DoesNotExist:
        return Response({"Erro": "não encontrado"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["DELETE"])
def excluir_evento(request,pk):
    try:
        evento = models.Evento.objects.get(pk=pk)
        evento.delete()
        return Response({"Reposta": "Evento Deletado com Sucesso!"})
    except models.Evento.DoesNotExist:
        return Response({"Erro": "não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(["PUT"])
def atulizar_evento(request,pk):
    if request.method == 'PUT':
        try:
            evento = models.Evento.objects.get(pk=pk)
            serializer = EventosSerializer(evento, data=request.data)
        except models.Evento.DoesNotExist:
            return Response({"Erro": "não encontrado"}, status=status.HTTP_404_NOT_FOUND)
             
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'mensagem': "algo deu erro"}, status=status.HTTP_400_BAD_REQUEST)