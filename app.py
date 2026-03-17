import streamlit as st
from backend.summarizer import summarizeStream, getTranscript
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(
        page_title = "YT Summarizer",
        layout = "centered"
)

st.title("Youtube Video Summarizer")
st.caption("Paste any Youtube URL and get a summary in seconds")

if "transcript" not in st.session_state:
        st.session_state.transcript = None

url = st.text_input("Youtube URL", placeholder="https://youtube.com/watch?v=...")

if st.button("Summarize", type="primary"):
        if not url:
                st.warning("Please enter a URL")
        else:
                with st.spinner("Reading transcript and summarizing..."):
                        try:
                                st.session_state.transcript = getTranscript(url)
                                st.write_stream(summarizeStream(url))
                                st.success("Done!")
                                st.video(url)
                        except Exception as e:
                                st.error(f"Error: {e}")

#Q&A Section
if st.session_state.transcript:
        st.divider()
        st.subheader("Ask a question about this video")
        question = st.text_input("Your Question", placeholder="What did they say about...?")

        if st.button("Ask"):
                if question:
                        with st.spinner("Thinking..."):
                                response = client.chat.completions.create(
                                        model = "gpt-4o-mini",
                                        messages = [
                                                {"role": "system", "content": f"Answer questions based only on this transcript: {st.session_state.transcript[:8000]}"},
                                                {"role": "user", "content": question} 
                                        ]
                                )

                                st.markdown(response.choices[0].message.content)
