from core.celery import app
from api.utils import yt_search
import os
from dotenv import load_dotenv

load_dotenv()


@app.task
def call_yt_search():
    """
    Task to call the YouTube search API
    """
    result = yt_search(key=os.getenv("GOOGLE_API_KEY"), query="cricket", max_results=10)
    print(result, flush=True)
