# Create your models here.
from django.db import models

#Banco de dados com tabela para item
class Item(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Itens"