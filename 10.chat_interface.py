import openai
import streamlit as st
import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로딩
load_dotenv()
  
# openai 기본 설정 (명확하게 지정)
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
DEPLOYMENT_NAME = "dev-gpt-4.1-mini"

def get_openai_client(message):
    
    try:
        response = openai.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=message,
            temperature=0.4,
        )
        return response.choices[0].message.content
    
    except Exception as e:
        st.error(f"Error connection to OpenAI: {e}")
        return None
    
# Streamlit UI 설정
st.title("Chat Interface with OpenAI")
st.write("OPENAI 모델에게 무엇이든 물어보세요.")

# 세션 상태 초기화 (채팅메시지의 초기화)
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 채팅 메세지의 표시
for massage in st.session_state.messages:
    st.chat_message(massage["role"]).write(massage["content"])


# 사용자 입력 받기
if prompt := st.chat_input("질문을 입력하세요:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # OpenAI 모델에 메시지 전달
    response = get_openai_client(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
 
