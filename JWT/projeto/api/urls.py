from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('logar/', views.logar_usuario, name='logar_usuario'),
    path('read', views.read, name='read')
]
