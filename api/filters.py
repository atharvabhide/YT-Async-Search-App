from django_filters import rest_framework as filters
from api.models import YTVideo


class YTVideoFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    published_at = filters.DateFromToRangeFilter(field_name='published_at')
    channel_title = filters.CharFilter(field_name='channel_title', lookup_expr='icontains')

    class Meta:
        model = YTVideo
        fields = ['title', 'published_at', 'channel_title']