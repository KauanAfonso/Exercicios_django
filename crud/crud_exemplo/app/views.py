from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

#Get dos itens
def item_read(request):
    itens = Item.objects.all()
    return render(request, "item_read.html", {'itens': itens})

# Criando um item
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)#pegando os daods enviados e enviando para o ItemForm como argumento
        if form.is_valid():
            form.save()#salva no banco 
            return redirect("item_read")
    else:
        form = ItemForm()
    return render(request, "itens_form.html", {'form': form})


'''
Função que atualiza um item por id

'''
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item) #criando uma instacia do item pego, para 'atualizar' ele.
        if form.is_valid():
            form.save()
            return redirect("item_read")
    else:
        form = ItemForm(instance=item)
    return render(request, "itens_form.html", {'form': form})


'''
Função para deletar um item por id

'''
def item_delete(request,pk):
    item = get_object_or_404(Item, pk=pk) #pegando o item especifico
    if request.method == "POST":
        item.delete()
        return redirect('item_read')
    return render(request,'confirmar_delete.html', {'item':item})    
