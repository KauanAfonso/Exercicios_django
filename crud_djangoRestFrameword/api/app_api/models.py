from django.db import models

# Create your models here.
class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    qtdRodas = models.PositiveBigIntegerField()
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=255)
    escolhas_combustivel = (

        ('GASOLINA', "Gasolina"),
        ("ETANOL", 'Etanol'),
        ("GNV", 'Gas'),
        ("ELETRICO" , "Eletrico"),
        ("ALCOOL", 'Alcool'),
        ('DIESEL', 'Diesel'),
        
        )
    combustivel = models.CharField(max_length=255, choices=escolhas_combustivel)

    def __str__(self):
        return self.nome

    

