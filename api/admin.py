# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import YTVideo


@admin.register(YTVideo)
class YTVideoAdmin(admin.ModelAdmin):
    """
    Admin class for YTVideo model

    Attributes:
        list_display (tuple): List of fields to display in admin list view
        list_filter (tuple): List of fields to filter in admin list view
        date_hierarchy (str): Field to filter by date in admin list view
    """

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
