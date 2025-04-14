from rest_framework import serializers
from .models import Piloto, Carro

class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'