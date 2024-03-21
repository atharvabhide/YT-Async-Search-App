from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


class YTVideo(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, verbose_name="ID"
    )
    title = models.CharField(
        max_length=200, blank=False, null=False, verbose_name="Title"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    video_url = models.URLField(
        max_length=200, blank=False, null=False, verbose_name="Video URL"
    )
    published_at = models.DateTimeField(
        blank=False, null=False, verbose_name="Published At"
    )
    channel_title = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Channel Title"
    )
    thumbnail_url = models.URLField(
        max_length=200, blank=False, null=False, verbose_name="Thumbnail URL"
    )
    next_page_token = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Next Page Token"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        db_table = "yt_video"
        verbose_name = _("YouTube Video")
        verbose_name_plural = _("YouTube Videos")
        ordering = ["-published_at"]
        indexes = [
            models.Index(fields=["published_at"]),
            models.Index(fields=["title"]),
        ]

    def __str__(self):
        return f"{self.title} by {self.channel_title} at {self.published_at}"
