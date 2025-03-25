from .models import Evento
import django_filters


class Filtrar_Evento(django_filters.FilterSet):

    categoria = django_filters.CharFilter(field_name='id_categoria__nome_categoria', lookup_expr='icontains') #filtrar o nome da categoria pego pela FK
    data = django_filters.CharFilter(field_name='data', lookup_expr='exact')
    
    class Meta:
        model: Evento
        fields  = ['categoria', 'data']