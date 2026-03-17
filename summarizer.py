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
        transcript = YouTubeTranscriptApi.get_transcript(videoID)

        texts = []
        for t in transcript:
                texts.append(t["text"])

        return " ".join(texts)
