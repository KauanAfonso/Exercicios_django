from django.urls import path

from .views import *

urlpatterns = [
    path("", mostrar_tarefa, name="mostrar_tarefa"),
    path("criar", criar_tarefa, name="criar_tarefa")
]