from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from api.models import YTVideo
from api.serializers import YTVideoSerializer


class YTVideoListView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request):
        videos = YTVideo.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(videos, request)
        serializer = YTVideoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
