import openai

import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
from dotenv import load_dotenv

from langchain_openai import AzureChatOpenAI

load_dotenv()

model = AzureChatOpenAI(model='dev-gpt-4.1-mini')

# model = AzureChatOpenAI(
#     deployment_name='dev-gpt-4.1-mini',
#     api_version='2023-05-15'
# )

response = model.invoke("삼성전자의 파운드리 사업에 대해서 알려줘")

print(response.content)