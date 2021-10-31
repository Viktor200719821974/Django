import django_filters as filters

from .models import UserModel

class UserFilter(filters.FilterSet):
    age_gt = filters.NumberFilter('profile', 'age__gt')
    age_lt = filters.NumberFilter('profile', 'age__lt')
    avatars_isnull = filters.BooleanFilter('profile', 'avatars__isnull')
    name_endswith = filters.CharFilter('profile', 'name__endSwith')
    surname_istartswith = filters.CharFilter('profile', 'surname__istartswith')

    class Meta:
        model = UserModel
        fields = ('age_gt', 'age_lt', 'avatars_isnull', 'name_endswith', 'surname_istartwith', 'phone')