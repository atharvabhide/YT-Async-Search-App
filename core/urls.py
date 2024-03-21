from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


schema_view = get_schema_view(
    openapi.Info(
        title="YT Async Search App",
        default_version="v1",
        url="http://localhost:8080/",
        description="YT Async Search App API Documentation",
    ),
    public=True,
)


class Home(generics.RetrieveAPIView):
    def get(self, request):
        return Response(
            {"message": "Welcome to YT Async Search App"}, status=status.HTTP_200_OK
        )

    def get_serializer(self):
        pass

    def get_seralizer(self):
        pass


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("", include("api.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
