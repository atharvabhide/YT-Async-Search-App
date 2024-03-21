import requests
from api.serializers import YTVideoSerializer
from api.models import YTVideo


def yt_search(key, query, max_results=10):
    try:
        page_token = (
            YTVideo.objects.last().next_page_token if YTVideo.objects.last() else None
        )
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "q": query,
            "type": "video",
            "order": "date",
            "publishedAfter": "2023-01-01T00:00:00Z",
            "key": key,
            "part": "snippet",
            "maxResults": max_results,
            "pageToken": page_token if page_token else "",
        }
        response = requests.get(url, params=params).json()
        print(response.keys(), flush=True)
        for item in response["items"]:
            item = {
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"],
                "video_url": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                "published_at": item["snippet"]["publishedAt"],
                "channel_title": item["snippet"]["channelTitle"],
                "thumbnail_url": item["snippet"]["thumbnails"]["default"]["url"],
                "next_page_token": response.get("nextPageToken", None),
            }
            serializer = YTVideoSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors, flush=True)
        return {"success": "Data saved successfully"}
    except Exception as e:
        return {"error": str(e)}
