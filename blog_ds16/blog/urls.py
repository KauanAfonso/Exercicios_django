from . import views
from django.urls import path

urlpatterns = [
    path('', views.listar_postagens, name='listar_postagens')
]
