import streamlit as st


def main():
    st.title("YouTube Video Grid")
    st.sidebar.header("Configuration")
    with st.sidebar.form(key="grid_reset"):
        n_cols = 5
        st.form_submit_button(label="Refresh grid")
    page_number = st.sidebar.number_input(
        "Page number:", min_value=1, value=1, max_value=5
    )
    st.sidebar.caption("Source: YouTube Data API")

    # Dummy data for demonstration
    videos = [
        {
            "snippet": {
                "title": f"Python Programming Tutorial {i}",
                "thumbnails": {"default": {"url": "https://via.placeholder.com/150"}},
            }
        }
        for i in range(1, 51)  # Total of 50 dummy videos
    ]

    # Pagination
    start_index = (page_number - 1) * n_cols
    end_index = min(len(videos), start_index + (n_cols * 2))
    videos_to_display = videos[start_index:end_index]

    # Display videos in grid layout
    n_rows = (len(videos_to_display) + n_cols - 1) // n_cols
    rows = [st.container() for _ in range(n_rows)]
    cols_per_row = [r.columns(n_cols) for r in rows]
    cols = [column for row in cols_per_row for column in row]

    for video_index, video in enumerate(videos_to_display):
        thumbnail_url = video["snippet"]["thumbnails"]["default"]["url"]
        cols[video_index].image(thumbnail_url, caption=video["snippet"]["title"])


if __name__ == "__main__":
    main()
