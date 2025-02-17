from django.shortcuts import render
from .models import Postagem
# Create your views here.

def listar_postagens(request):
    postagens = Postagem.objects.all().order_by('-data')
    return render(request, 'blog/kauan.html', {'postagens': postagens})
