from django.urls import path
from .views import PilotoListCreateAPIView, CarroListCreateAPIView, PilotoRetriveUpdateDestroyAPIview
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

#Informações gerais da api
schema_view = get_schema_view(
    openapi.Info(
        title="API da Formula 1",
        default_version='v1',
        description="APi de pilotos e carros da Formula 1"

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

#chamando as classes das views 
urlpatterns = [
    path('piloto/', view=PilotoListCreateAPIView.as_view()), #.as_view() -> serve para converter a class como uma view
    path('piloto/<int:pk>/', view=PilotoRetriveUpdateDestroyAPIview.as_view()),
    path('carro/', view=CarroListCreateAPIView.as_view()),
    path('doc/', view= schema_view.with_ui('swagger', cache_timeout=8)) #Chamando o schema que retorna o swwager
]
