import streamlit as st

st.title("상품개발요청 페이지")

subject = st.text_input("상품명 ")
content = st.number_input("상품금액 ")



# st.line_chart(char_data)