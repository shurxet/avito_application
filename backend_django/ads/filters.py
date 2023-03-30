from django_filters import rest_framework as filters
from ads.models.ad import Ad


class AdFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
