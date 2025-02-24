from django.shortcuts import render
from .models import *

# Create your views here.
def mostrar_tarefa(request):
    tarefas = Tarefa.objects.all()
    return render(request, "index.html" , {'tarefas':tarefas})
