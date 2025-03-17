from django.urls import path
from . import views


urlpatterns = [
    path('carros/', views.read_carro), #não precisa por o name pois ele é para o template
    path('carros/<int:pk>', views.read_one_car),
]