# app.py

import streamlit as st
from backend.agent import handle_query

st.set_page_config(page_title="상품 개발 지원 Assistant")
st.title("상품 개발 지원 Assistant")
 
product_name = st.text_input("신규 상품명을 입력하세요")
cp_service = st.text_input("제휴 서비스를 입력하세요")

if st.button("분석 시작"):
    if not product_name or not cp_service:
        st.warning("모든 항목을 입력해주세요.")
    else:
        with st.spinner("AI가 분석 중입니다..."):
            result = handle_query(product_name, cp_service)
            st.success("완료되었습니다!")
            st.markdown(result)
