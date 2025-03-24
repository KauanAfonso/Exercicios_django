from django.shortcuts import render,redirect , get_object_or_404
from .models import *

#get
def mostrar_tarefa(request):
    tarefas = Tarefa.objects.all()#pegando todos os objetos da model
    return render(request, "index.html" , {'tarefas':tarefas})

#criando 
def criar_tarefa(request):
    if request.method == "POST":
        #pegando os valores dos campos do form do template
        descricao = request.POST.get('descricao')
        status = request.POST.get('status')

        #criando a terefa
        Tarefa.objects.create(descricao=descricao , status=status)

        return redirect("mostrar_tarefa")#redirecionando
    
    return render(request, "criar_tarefa.html")#renderizando

#Excluindo
def excluir_tarefa(tarefa_id):
    tarefa = get_object_or_404(Tarefa , id=tarefa_id)
    tarefa.delete()

    return redirect('mostrar_tarefa')

#Atualizando a tarefa
def atualizar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa , id=tarefa_id)
    if request.method == "POST":

        descricao = request.POST.get('descricao')
        status = request.POST.get('status')
        
        #se for vdd atuliza os valores e salva
        if descricao and status:

            tarefa.descricao = descricao
            tarefa.status = status

            tarefa.save()
    else:
        # Se algum campo não foi preenchido corretamente, mostrar uma mensagem de erro
        error_message = "Todos os campos precisam ser preenchidos!"
        return render(request, "atualizar_tarefa.html", {'tarefa': tarefa, 'error': error_message})
    redirect('mostrar_tarefa')
           
    return render(request, "atualizar_tarefa.html", {'tarefa': tarefa})