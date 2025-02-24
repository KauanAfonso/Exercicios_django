from django.shortcuts import render,redirect , get_object_or_404
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

def excluir_tarefa(tarefa_id):
    tarefa = get_object_or_404(Tarefa , id=tarefa_id)
    tarefa.delete()

    return redirect('mostrar_tarefa')

def atualizar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa , id=tarefa_id)
    if request.method == "POST":

        descricao = request.POST.get('descricao')
        status = request.POST.get('status')

        if descricao and status:

            tarefa.descricao = descricao
            tarefa.status = status

            tarefa.save()
    # else:
    #     # Se algum campo não foi preenchido corretamente, mostrar uma mensagem de erro
    #     error_message = "Todos os campos precisam ser preenchidos!"
    #     return render(request, "atualizar_tarefa.html", {'tarefa': tarefa, 'error': error_message})
    redirect('mostrar_tarefa')
           
    return render(request, "atualizar_tarefa.html", {'tarefa': tarefa})