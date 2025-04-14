from django.urls import path
from .views import PilotoListCreateAPIView, CarroListCreateAPIView

#chamando as classes das views 
urlpatterns = [
    path('piloto/', view=PilotoListCreateAPIView.as_view()), #.as_view() -> serve para converter a class como uma view
    path('carro/', view=CarroListCreateAPIView.as_view()),
]
