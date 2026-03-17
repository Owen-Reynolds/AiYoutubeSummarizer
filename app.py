import streamlit as st
from summarizer import summarize

st.set_page_config(
        page_title = "YT Summarizer",
        layout = "centered"
)

st.title("Youtube Video Summarizer")
st.caption("Paste any Youtube URL and get a summary in seconds")

url = st.text_input("Youtube URL", placeholder="https://youtube.com/watch?v=...")

if st.button("Summarize", type="primary"):
        if not url:
                st.warning("Please enter a URL")
        else:
                with st.spinner("Reading transcript and summarizing..."):
                        try:
                                result = summarize(url)
                                st.success("Done!")
                                st.markdown(result)
                        except Exception as e:
                                st.error(f"Error: {e}")