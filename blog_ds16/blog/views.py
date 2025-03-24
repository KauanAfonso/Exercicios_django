from django.shortcuts import render
from .models import Postagem
# Create your views here.

#Essa view será responsável por listar as postagens
def listar_postagens(request):
    postagens = Postagem.objects.all().order_by('-data')#ordenando por data
    return render(request, 'blog/kauan.html', {'postagens': postagens})
