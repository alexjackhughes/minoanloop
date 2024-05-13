from openai import OpenAI
import pinecone
import numpy as np
import os

from dotenv import load_dotenv
load_dotenv()

# openai.organization = os.getenv("OPENAI_ORGANIZATION_ID")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)
# client(default_organization=os.getenv("OPENAI_ORGANIZATION_ID"))

model = os.environ.get("CHAT_MODEL")

def generate_completion(prompt, messages=None):
  if messages is None:
      messages = [
          {"role": "system", "content": "You are an expert linguist and translator of ancient losts texts, and answer all sorts of questions concisely and helpfully."},
          {"role": "user", "content": "Who won the world series in 2020?"},
          {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
          {"role": "user", "content": prompt}
      ]

  response = client.chat.completions.create(model=model,
  messages=messages)

  return response.choices[0].message.content