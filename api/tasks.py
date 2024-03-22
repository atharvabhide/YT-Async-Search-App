from core.celery import app
from api.utils import yt_search
import os


@app.task
def call_yt_search():
    result = yt_search(
        key=os.environ["GOOGLE_API_KEY"], query="cricket", max_results=10
    )
    print(result, flush=True)
