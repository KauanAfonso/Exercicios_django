from .models import Pessoa
from rest_framework import serializers

class PessaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['username', 'email', 'biografia', 'endereco', 'escolaridade', 'telefone', 'numero_animais'] #Campos que quero para o json
