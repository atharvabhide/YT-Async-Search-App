# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import YTVideo


@admin.register(YTVideo)
class YTVideoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "video_url",
        "published_at",
        "channel_title",
        "thumbnail_url",
        "next_page_token",
        "created_at",
        "updated_at",
    )
    list_filter = ("published_at", "created_at", "updated_at")
    date_hierarchy = "created_at"
