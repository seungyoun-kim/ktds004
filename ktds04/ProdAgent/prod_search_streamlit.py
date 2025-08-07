import os
import streamlit as st
import pandas as pd
from backend.agent import handle_query
from backend.utils import extract_table_from_markdown, draw_price_bar_chart

st.set_page_config(layout="wide")
st.title("상품 개발 지원 Assistant")

product_name = st.text_input("신규 상품명을 입력하세요")
cp_service = st.text_input("제휴 서비스를 입력하세요")
similar_count = st.text_input("비교 갯수를 입력하세요. 미입력시 3개로 설정됩니다", value="3")

# 버튼 클릭 시 분석 시작
if st.button("분석 시작"):
    # 입력값 검증
    if not product_name or not cp_service or not similar_count:
        st.warning("모든 항목을 입력해주세요.")
    else:
        with st.spinner("분석 중입니다..."):
            result = handle_query(product_name, cp_service, similar_count)
            st.markdown(result)

            # 테이블 추출 + 그래프 표시
            df = extract_table_from_markdown(result)

            # 테이블이 비어있지 않은 경우에만 그래프 그리기
            if not df.empty:
                st.subheader("유사 상품 월정액 그래프")
                # 그래프 그리기
                draw_price_bar_chart(df)
            else:
                # 유사 상품 데이터가 없을 경우 경고 메시지 표시
                st.warning("유사 상품 데이터가 없습니다. 다른 상품명을 입력해보세요.")
            
            # 결과 표시
            st.success("분석 완료되었습니다.")

# # ? Azure App Service 호환을 위한 실행 코드 추가
# if __name__ == "__main__":
#     port = int(os.environ.get("WEBSITES_PORT", 8000))  # Azure App Service가 허용하는 포트
#     st.run(host="0.0.0.0", port=port)