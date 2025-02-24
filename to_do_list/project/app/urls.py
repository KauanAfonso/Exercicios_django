from django.urls import path
from .views import mostrar_tarefa

urlpatterns = [
    path("", mostrar_tarefa, name="mostrar_tarefa"),
]