from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def mostrar_tarefa(request):
    tarefas = Tarefa.objects.all()
    return render(request, "index.html" , {'tarefas':tarefas})

def criar_tarefa(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        status = request.POST.get('status')

        Tarefa.objects.create(descricao=descricao , status=status)

        return redirect("mostrar_tarefa")
    
    return render(request, "criar_tarefa.html")