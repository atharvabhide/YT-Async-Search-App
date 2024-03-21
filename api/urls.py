from django.urls import path
from api.views import YTVideoListView


urlpatterns = [
    path("videos/", YTVideoListView.as_view(), name="yt_video_list"),
]
