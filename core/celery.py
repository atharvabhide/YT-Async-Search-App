from celery import Celery
from django.conf import settings
import os
from datetime import timedelta


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("tasks", broker=settings.CELERY_BROKER_URL, backend="rpc://")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "run-every-ten-seconds": {
        "task": "api.tasks.call_yt_search",
        "schedule": timedelta(seconds=10),
    }
}

app.autodiscover_tasks()
