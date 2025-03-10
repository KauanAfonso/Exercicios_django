from . import views
from django.urls import path

urlpatterns = [
    path('', views.visualizar_livros, name='livros'),
    path('criar/' , views.criar_livro, name='criar_livro'),
    path('editar/<int:pk>' , views.atualizar_livro, name='atualizar_livro'),
    path('excluir<int:pk>', views.deletar_livro, name="excluir_livro" ),
]
