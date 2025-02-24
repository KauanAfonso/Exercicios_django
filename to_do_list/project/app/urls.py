from django.urls import path

from .views import *

urlpatterns = [
    path("", mostrar_tarefa, name="mostrar_tarefa"),
    path("criar", criar_tarefa, name="criar_tarefa"),
    path("excluir_tarefa/<int:tarefa_id>", excluir_tarefa, name="excluir_tarefa")
]