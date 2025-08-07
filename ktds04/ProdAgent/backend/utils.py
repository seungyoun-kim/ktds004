import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

def extract_table_from_markdown(md_text: str) -> pd.DataFrame:
    try:
        lines = [line for line in md_text.splitlines() if '|' in line and not line.strip().startswith('|---')]
        table_str = '\n'.join(lines)
        df = pd.read_csv(io.StringIO(table_str), sep='|', engine='python')

        # 공백 열 제거 및 헤더 정리
        df = df.dropna(axis=1, how='all')
        df.columns = df.columns.str.strip()
        df = df.rename(columns=lambda x: x.strip())

        # 0번 인덱스가 헤더일 경우 제거
        df = df.drop(index=0, errors='ignore')
        return df.reset_index(drop=True)

    except Exception as e:
        st.error(f"테이블 추출 오류: {e}")
        return pd.DataFrame()
    
    

def draw_price_bar_chart(df: pd.DataFrame):
    
    if '상품명' not in df.columns or '월정액' not in df.columns:
        st.warning("상품명 또는 월정액 컬럼이 존재하지 않습니다.")
        return

    # 월정액 문자열 → 숫자 (ex: 33,000원 → 33000)
    # df['월정액'] = df['월정액'].str.replace(",", "").str.replace("원", "").astype(int)
    
    fig, ax = plt.subplots()
    ax.bar(df['상품명'], df['월정액'])
    ax.set_title("유사 상품 월정액 비교")
    ax.set_ylabel("금액 (원)")
    st.pyplot(fig)