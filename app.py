import streamlit as st
import base64

# Configuration and Setup
st.set_page_config(page_title="VDK GPT", layout="wide")

# Helper Functions
def load_css():
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def render_video_thumbnail(video_id, title):
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"
    return f"""
    <div class="video-thumbnail" onclick="selectVideo('{video_id}')">
        <img src="{thumbnail_url}" alt="{title}">
        <p>{title}</p>
    </div>
    """

# Main App
def main():
    load_css()

    # Session State
    if 'selected_video' not in st.session_state:
        st.session_state.selected_video = None

    # Main Page
    if not st.session_state.selected_video:
        st.title("VDK GPT")
        
        videos = [
            ("UvNNCdSHZ_A", "Jain Philosophy: An Introduction"),
            ("8mxDiefPrcc", "Challenges of Parenting"),
            ("fbgKj0myUOk", "The Art of Letting Go"),
            ("ALuyrcNfNRM", "Why Dr. Ambedkar is Great?"),
            ("ISRQ7djT3uw", "Sikkim Youth Convention 2023")
        ]

        cols = st.columns(3)
        for idx, (video_id, title) in enumerate(videos):
            with cols[idx % 3]:
                st.markdown(render_video_thumbnail(video_id, title), unsafe_allow_html=True)

        st.markdown("""
        <script>
        function selectVideo(videoId) {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: videoId}, '*');
        }
        </script>
        """, unsafe_allow_html=True)

    # Video Interaction Page
    else:
        video_id = st.session_state.selected_video
        st.markdown(f"""
        <iframe width="100%" height="500" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["Summarize", "Quiz Me", "Ask any Doubt"])

        with tab1:
            st.subheader("Summarize")
            st.text_area("Summary will appear here")

        with tab2:
            st.subheader("Quiz Me")
            st.write("Quiz questions will appear here")

        with tab3:
            st.subheader("Ask any Doubt")
            st.text_input("Enter your question")
            st.button("Ask")

        if st.button("Back to Videos"):
            st.session_state.selected_video = None
            st.rerun()

if __name__ == "__main__":
    main()
