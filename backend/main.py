from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from summarizer import summarize, getTranscript
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_methods=["*"],
        allow_headers=["*"],
)

class summarizeRequest(BaseModel):
        url: str

class questionRequest(BaseModel):
        transcript: str
        question: str

@app.post("/summarize")

async def summarize_video(req: summarizeRequest):
        try:
                transcript = getTranscript(req.url)
                summary = summarize(req.url)
                return { "summary": summary, "transcript": transcript}
        except Exception as e:
                return { "error": str(e)}, 400
        
@app.post("/ask")
async def ask_question(req: questionRequest):
        response = client.chat.completions.create(
                model = "gpt-4o-mini",
                messages=[
                        {"role": "system", "content": f"Answer based only on this transcript: {req.transcript[:8000]}"},
                        {"role": "user", "content": req.question}
                ]
        )
        return { "answer": response.choices[0].message.content }

@app.get("/")
async def root():
        return { "status": "running" }