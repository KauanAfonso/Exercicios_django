from django.db import models

# Create your models here.
class Postagem(models.Model):
    titlo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titlo
    
