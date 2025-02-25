from django.shortcuts import render
from .models import Item
from .forms import ItemForm


def item_read(request):
    itens = Item.objects.all()
    return render(request, "item_read.html", {'itens': itens})

# Create your views here.
