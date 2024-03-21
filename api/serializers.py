from api.models import YTVideo
from rest_framework.serializers import ModelSerializer


class YTVideoSerializer(ModelSerializer):
    class Meta:
        model = YTVideo
        fields = "__all__"
