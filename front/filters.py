import django_filters

from django_filters import DateFilter,CharFilter
from .models import Record3

class OrderFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name='timestamp',lookup_expr='gte')
    end_date=DateFilter(field_name='timestamp',lookup_expr='lte')
    result=CharFilter(field_name='result',lookup_expr='icontains')
    class Meta:
        model=Record3
        fields='__all__'
        exclude =['name','timestamp','email']