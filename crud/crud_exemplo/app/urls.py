from django.urls import path
from . import views

urlpatterns = [
    path('',views.item_read, name='item_read'),

]