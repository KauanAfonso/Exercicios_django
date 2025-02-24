from django.db import models


class Tarefa(models.Model):

    escolha = [
        ("PENDENTE" ,"PENDENTE"),
        ("CONCLUIDA", "CONCLUIDA"),
        ("A FAZER", "A FAZER"),
    ]
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=escolha)


    def __str__(self):
        return self.descricao





# Create your models here.
