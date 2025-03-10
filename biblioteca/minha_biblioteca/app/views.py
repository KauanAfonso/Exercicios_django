from django.shortcuts import render,redirect, get_object_or_404
from .models import livros
from .form import itemForm
from .filters import livroFilter
# Create your views here.

def visualizar_livros(request):
    todos_livros = livros.objects.all()
    return render(request, 'livros.html', {'livros': todos_livros})

def criar_livro(request):
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("livros")
    else:
        form = itemForm()
        
    return render(request, "criar_livro.html" , {'form':form})

def atualizar_livro(request, pk):
    id_livro = get_object_or_404(livros,pk=pk)
    if request.method == "POST":
        form = itemForm(request.POST, instance=id_livro) #esse instance irá
        if form.is_valid():
            form.save()
            return redirect("livros")
    else:
        form = itemForm(instance=id_livro)
        
    return render(request, "atualizar_livro.html" , {'form':form})


def deletar_livro(request,pk):
    id_livro = get_object_or_404(livros, pk=pk)
    if request.method == "POST":
        id_livro.delete()
        return redirect("livros")
    return render(request, 'excluir_livro.html', {'livro':id_livro})

def filtrar(request):
    filtro = livroFilter(request.GET, queryset=livros.objects.all())
    return render(request, "filtrar_livro.html", {'filtro':filtro})