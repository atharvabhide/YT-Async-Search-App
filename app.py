import streamlit as st
import requests


def fetch_videos(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Failed to fetch videos: {e}")
        return {"results": [], "next": None, "previous": None}


def get_filters():
    with st.sidebar.form(key="grid_filters"):
        title_filter = st.text_input("Filter by Title:")
        channel_filter = st.text_input("Filter by Channel:")
        published_after_filter = st.date_input("Published After:", value=None)
        published_before_filter = st.date_input("Published Before:", value=None)
        st.form_submit_button(label="Apply Filters")

    filters = {}
    if title_filter:
        filters["title"] = title_filter
    if channel_filter:
        filters["channel_title"] = channel_filter
    if published_after_filter:
        filters["published_at_after"] = published_after_filter.isoformat()
    if published_before_filter:
        filters["published_at_before"] = published_before_filter.isoformat()

    return filters


def display_videos(videos):
    n_cols = 5
    n_rows = (len(videos) + n_cols - 1) // n_cols
    rows = [st.container() for _ in range(n_rows)]
    cols_per_row = [r.columns(n_cols) for r in rows]
    cols = [column for row in cols_per_row for column in row]

    for video_index, video in enumerate(videos):
        thumbnail_url = video["thumbnail_url"]
        cols[video_index].image(thumbnail_url, caption=video["title"])


def main():
    st.title("YouTube Video Grid")
    st.sidebar.header("Configuration")

    filters = get_filters()
    base_url = "http://127.0.0.1:8000/videos/"
    url = base_url + "?" + "&".join(f"{k}={v}" for k, v in filters.items())

    # Fetch initial data to get total pages
    initial_data = fetch_videos(url)
    total_pages = initial_data["count"] // 10

    # Create a select box for the page number
    page_number = st.sidebar.selectbox("Page Number", options=range(1, total_pages + 1))

    # Modify the url to include the page number
    url += f"&page={page_number}"

    # Fetch and display videos for the selected page
    data = fetch_videos(url)
    display_videos(data["results"])

    if st.sidebar.button("Refresh Videos"):
        # Refresh the videos for the selected page
        data = fetch_videos(url)
        display_videos(data["results"])


if __name__ == "__main__":
    main()
