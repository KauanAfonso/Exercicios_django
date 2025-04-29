from django.db import models
from django.contrib.auth.models import AbstractUser

#empresa
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)

#usuario 
class Usuario(AbstractUser):
    apelido = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    genero = models.CharField(max_length=100, choices=(('M', 'Masculino') ,("F", "Feminino") , ("N", "Prefiro não informar")), null=True, blank=True)

    escolha_funcao = (
        ("G", "Getor"),
        ("C", "Colaborador"),
        ("E" , "Estagiario"),
        ("A", "Aprendiz"),
        ('M', "Meio Oficial")
    )

    colaborador = models.CharField(max_length=1, choices=escolha_funcao, default='M')

    REQUIRED_FIELDS = ['colaborador']

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)

#ingressos -> um usuario pod ter muitos ingressos
class Ingresso(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
