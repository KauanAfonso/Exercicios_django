from django.shortcuts import render
from .models import Carro
from .serializer import CarroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


'''
Retornar todos os dados da api
'''
@api_view(["GET"])
def read_carro(request):
    carros = Carro.objects.all()
    serializer = CarroSerializer(carros, many=True) #
    return Response(serializer.data) #passar o serializar em json

'''
Pegar somente um carro da api pelo id
'''
@api_view(["GET"])
def  read_one_car(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
        serializer = CarroSerializer(carro, many=False)
        return Response(serializer.data)
    except Carro.DoesNotExist:
        return Response({'error': 'Car is not found'}, status=status.HTTP_404_NOT_FOUND) #retornando o erro e status 
    


@api_view(['POST'])
def create_car(request):
    if request.method == "POST":
        serializer = CarroSerializer(data=request.data , many=isinstance(request.data))#convertendo do json para o carro
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #indica o erro automaticamente


@api_view(['PUT'])
def uptade_car(request, pk):
    if request.method == "PUT":
        try:
            carro = Carro.objects.get(pk=pk)
            serializer = CarroSerializer(carro, data=request.data) #Passo o carro que quero e as informações do json
        except Carro.DoesNotExist:
            return Response({'error': 'Car is not found'}, status=status.HTTP_404_NOT_FOUND) #retornando o erro e status 
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #indica o erro automaticamente
        
@api_view(['DELETE'])
def delete_car(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
        return Response({'Error': "Car is not found"},status=status.HTTP_404_NOT_FOUND)
        
    carro.delete()
    return Response({"Mensagem":"Excluido com sucesso !"}, status=status.HTTP_200_OK)