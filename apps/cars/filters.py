import django_filters as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    year_gt = filters.NumberFilter('year', 'gt')
    year_lt = filters.NumberFilter('year', 'lt')
    park_name = filters.CharFilter('autopark', 'name__istartswith')
    color_exact = filters.CharFilter('color', '__exact')
    model_regex = filters.CharFilter('model', '__regex')

    class Meta:
        model = CarModel
        fields = ('year_gt', 'park_name', 'year', 'model', 'color', 'brand', 'model_regex', 'color_exact')





