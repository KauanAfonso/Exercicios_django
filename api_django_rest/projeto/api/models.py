from django.db import models
from datetime import datetime,timedelta


'''

Teremos uma tabela para eventos e uma para 
categoria. Um evento pode ter uma e somente uma
categoria no sistema.

'''
#tabela categoria
class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_categoria

#Tabela evento
class Evento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data = models.DateField()
    horario = models.TimeField()
    local = models.CharField(max_length=255, default='')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nome: {self.nome}, Descricao: {self.nome}, Local {self.local}"
    
 
       
     
