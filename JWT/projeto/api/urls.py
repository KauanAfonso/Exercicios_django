from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_usuario, name='criar_usuario'),
]
