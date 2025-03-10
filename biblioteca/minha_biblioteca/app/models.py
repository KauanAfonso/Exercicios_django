from django.db import models

# Create your models here.
class livros(models.Model):
    titulo = models.CharField(max_length=255),
    autor = models.CharField(max_length=100),
    data_de_publicacao = models.DateField(),

    def __str__(self):
        return self.titulo