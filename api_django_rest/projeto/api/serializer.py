from rest_framework import serializers
from . import models




#Serializer para categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Categoria
        fields = '__all__'
        
#Serializer para Eventos
class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Evento
        fields = "__all__"


#Junção dos dois serializers para retornar as informações diretas
class Evento_CategoriaSerializer(serializers.ModelSerializer):
    nome_categoria = serializers.CharField(source='id_categoria.nome_categoria') #fazendo o join
    class Meta:
        model = models.Evento
        fields = ['pk', 'nome', 'descricao', 'data' , 'horario', 'local', 'nome_categoria']
