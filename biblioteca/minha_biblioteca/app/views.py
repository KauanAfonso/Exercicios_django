from django.shortcuts import render,redirect, get_object_or_404
from .models import livros
from .form import itemForm
from .filters import livroFilter
# Create your views here.

'''

Estou chamando o filtro como metodo get e redenderizando ele

'''
def visualizar_livros(request):
    filtro = livroFilter(request.GET, queryset=livros.objects.all())
    return render(request,  "livros.html", {'filtro':filtro})

'''
Função para criar um livro com base no ID
'''
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
def deletar_livro(request,pk):
    id_livro = get_object_or_404(livros, pk=pk)
    if request.method == "POST":
        id_livro.delete()
        return redirect("livros")
    return render(request, 'excluir_livro.html', {'livro':id_livro})


