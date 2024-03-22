from api.models import YTVideo
from rest_framework.serializers import ModelSerializer


class YTVideoSerializer(ModelSerializer):
    """
    Serializer class for YTVideo model

    Attributes:
        Meta (class): Meta class for YTVideoSerializer
    """

    class Meta:
        model = YTVideo
        fields = "__all__"
