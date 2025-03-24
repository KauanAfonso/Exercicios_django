from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('criar_evento/', views.criar_evento),
    path('eventos/', views.obter_eventos),
    path('eventos/<int:pk>', views.obter_evento_especifico),
    path('eventos/deletar/<int:pk>', views.excluir_evento),
    path('eventos/atualizar/<int:pk>', views.atulizar_evento),
]