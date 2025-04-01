from django.db import models
from django.contrib.auth.models import AbstractUser
#classe para a atividade do dorival de CRUD
class Pessoa(AbstractUser):
    biografia = models.TextField()
    idade = models.IntegerField(null=True, blank=True)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField(null=True, blank=True)
    escolaridade = models.CharField(max_length=50, null=True, blank=True)
    numero_animais = models.IntegerField(null=True, blank=True)
    REQUIRED_FIELDS = [ "biografia", "telefone"]

    def __str__(self):
        return self.username
   

