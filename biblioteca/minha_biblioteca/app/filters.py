import django_filters 
from django_filters import *
from .models import livros
from django import forms

class livroFilter(django_filters.FilterSet):
    titulo = CharFilter(field_name="titulo", lookup_expr='icontains')
    autor = CharFilter(field_name="autor", lookup_expr='icontains')
    data_de_publicacao = DateFilter(field_name="data_de_publicacao", lookup_expr='exact', widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = livros
        fields = '__all__'