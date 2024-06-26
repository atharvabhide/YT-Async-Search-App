# Generated by Django 4.2.7 on 2024-03-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_ytvideo_next_page_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ytvideo",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Title"),
        ),
        migrations.AddIndex(
            model_name="ytvideo",
            index=models.Index(
                fields=["published_at"], name="yt_video_publish_6cf7f4_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="ytvideo",
            index=models.Index(fields=["title"], name="yt_video_title_1899c6_idx"),
        ),
    ]
