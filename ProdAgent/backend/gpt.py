import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# openai.azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
# openai.api_type = os.getenv('OPENAI_API_TYPE')
# openai.api_version = os.getenv('OPENAI_API_VERSION')

client = AzureOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("OPENAI_API_VERSION")
)

def generate_text(prompt: str) -> str:
    response = client.chat.completions.create(
        model="dev-gpt-4.1-mini",
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()