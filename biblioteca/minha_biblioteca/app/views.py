from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import livros
from .form import itemForm
from .filters import livroFilter

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


'''
função de login, tuilizando o login()
de django.contrib.auth

'''
def realizar_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)#cria um formulário de autenticação com os dados POST
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(f"Usuário {user.username} logado com sucesso.") 
            return redirect('livros')
        else:
            print('Erro no formulário:', form.errors)
    else:
        form = AuthenticationForm()
    return render(request, "login.html" , {"form": form})

def realizar_logout(request):
    logout(request)
    return redirect("livros")

'''
Estou chamando o filtro como metodo get e redenderizando ele
'''
@login_required #esse loader não deixara acessar sem logar
def visualizar_livros(request):
    filtro = livroFilter(request.GET, queryset=livros.objects.all())
    nome = request.user.username
    return render(request,  "livros.html", {'filtro':filtro , 'nome':nome})

'''
Função para criar um livro com base no ID
'''

@login_required
def criar_livro(request):
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("livros")
    else:
        form = itemForm()
        
    return render(request, "criar_livro.html" , {'form':form})


'''
Função para atualizar um livro com base no ID
'''
@login_required
def atualizar_livro(request, pk):
    id_livro = get_object_or_404(livros,pk=pk)
    if request.method == "POST":
        form = itemForm(request.POST, instance=id_livro) #cria uma instancia de um livro com id pego no get
        if form.is_valid():
            form.save()
            return redirect("livros")
    else:
        form = itemForm(instance=id_livro)
        
    return render(request, "atualizar_livro.html" , {'form':form})

'''
Função para deletar um livro com base no ID
'''

@login_required
def deletar_livro(request,pk):
    id_livro = get_object_or_404(livros, pk=pk)
    if request.method == "POST":
        id_livro.delete()
        return redirect("livros")
    return render(request, 'excluir_livro.html', {'livro':id_livro})


