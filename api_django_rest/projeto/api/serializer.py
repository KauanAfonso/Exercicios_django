from rest_framework import serializers
from . import models



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Categoria
        fields = '__all__'

class EventosSerializer(serializers.ModelSerializer):
    # categoria = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Evento
        fields = "__all__"

class Evento_CategoriaSerializer(serializers.ModelSerializer):
    nome_categoria = serializers.CharField(source='id_categoria.nome_categoria') #fazendo o join
    class Meta:
        model = models.Evento
        fields = ['nome', 'descricao', 'data' , 'horario', 'local', 'nome_categoria']
