from django.shortcuts import render
from .models import Carro
from .serializer import CarroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(["GET"])
def read_carro(request):
    carros = Carro.objects.all()
    serializer = CarroSerializer(carros, many=True) #
    return Response(serializer.data) #passar o serializar em json

@api_view(["GET"])
def  read_one_car(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
        serializer = CarroSerializer(carro, many=False)
        return Response(serializer.data)
    except Carro.DoesNotExist:
        return Response({'error': 'Car is not found'}, status=status.HTTP_404_NOT_FOUND) #retornando o erro e status 