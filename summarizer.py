from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def testCall():
        response = client.chat.completions.create(
                model = "gpt-4o-mini",
                messages = [{"role": "user", "content": "Say hello!"}]
        )

        print(response.choices[0].message.content)


testCall()