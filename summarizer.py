from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os, re

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


#Test api
def testCall():
        response = client.chat.completions.create(
                model = "gpt-4o-mini",
                messages = [{"role": "user", "content": "Say hello!"}]
        )

        print(response.choices[0].message.content)

#Get Youtube video IDs
def getVideoID(url : str) -> str:
        patterns = [
                r"youtu\.be/([^?&]+)",
                r"v=([^?&]+)"
        ]

        for p in patterns:
                match = re.search(p, url)
                if match: return match.group(1)
        raise ValueError("Invalid Youtube URL")

def getTranscript(url : str) -> str:
        videoID = getVideoID(url)
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(videoID)

        texts = []
        for t in transcript:
                texts.append(t.text)

        return " ".join(texts)


def summarize(url : str ) -> dict:
        transcript = getTranscript(url)

        transcript = transcript[:12000]

        prompt = f"""You are an expert at summarizing Youtube videos.
        Given this transcript, respond in this exact format:

        Summary:
        2-3 sentence plain-english summary.

        Key Points:
        - point one
        - point two 
        - point three

        Verdict:
        One sentence on who should watch this.
        
        TRANSCRIPT:
        {transcript}"""

        response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    url = input("Enter a YouTube URL: ")
    print(summarize(url))
