from django.urls import path
from . import views

urlpatterns = [
    path('logar', views.fazer_login),
    path("read/", views.obter_usuarios),
    path("create/", views.criar_usuario),
    path('put/<int:pk>', views.atualizar_pessoa),
    path('delete/<int:pk>', views.excluir_pessoa)
    
]
