from . import views
from django.urls import path


#Aqui fica as urls do site
urlpatterns = [
    path('', views.visualizar_livros, name='livros'),
    path("login/", views.realizar_login, name="login" ),
    path("logout/", views.realizar_logout, name='logout'),
    path('criar/' , views.criar_livro, name='criar_livro'),
    path('editar/<int:pk>' , views.atualizar_livro, name='atualizar_livro'),
    path('excluir/<int:pk>', views.deletar_livro, name="excluir_livro" ),

]
