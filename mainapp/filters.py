import django_filters
from .models import Property


class PropertyFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    deal = django_filters.ChoiceFilter(choices=Property.CHOICES)
    province = django_filters.ChoiceFilter(choices=Property.PROVINCE_CHOICE)

    class Meta:
        model = Property
        fields = ['deal', 'province']
