from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from api.models import YTVideo
from api.serializers import YTVideoSerializer
from api.filters import YTVideoFilter
from rest_framework.response import Response


class YTVideoListView(ListAPIView):
    serializer_class = YTVideoSerializer
    pagination_class = PageNumberPagination
    filterset_class = YTVideoFilter

    def get(self, request):
        queryset = YTVideo.objects.all()
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
