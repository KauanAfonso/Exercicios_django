from django.urls import path
from . import views

urlpatterns = [
    path("read/", views.obter_usuarios),
    path("create/", views.criar_usuario)
]
