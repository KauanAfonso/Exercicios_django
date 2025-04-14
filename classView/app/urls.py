from django.urls import path
from .views import PilotoListCreateAPIView

#chamando as classes das views 
urlpatterns = [
    path('piloto/', view=PilotoListCreateAPIView.as_view()) #.as_view() -> serve para converter a class como uma view
]
