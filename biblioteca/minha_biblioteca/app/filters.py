import django_filters 
from django_filters import CharFilter
from .models import livros

class livroFilter(django_filters.FilterSet):
    titulo = CharFilter(field_name="titulo", lookup_expr='icontains')

    class Meta:
        model = livros
        fields = ["titulo"]