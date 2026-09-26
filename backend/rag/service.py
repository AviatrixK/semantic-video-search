from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_answer(query, context):

    prompt = f"""
You are a video question-answering assistant.

Answer the user's question using ONLY the provided transcript context.

If the answer cannot be found in the context, say:
"I couldn't find that information in the video."

Transcript context:
{context}

User question:
{query}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text