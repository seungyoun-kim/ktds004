from backend.search import search_similar_products
from backend.gpt import generate_text

def handle_query(product_name: str, cp_service: str):
    # 1. 유사 상품 검색
    similar = search_similar_products(product_name)
    docs = "\n\n".join(similar)

    # 2. 상품 비교 프롬프트 구성
    prompt = f"""
신규 상품명: {product_name}
제휴 서비스: {cp_service}
다음은 유사한 기존 상품 설명입니다:\n{docs}
이 정보들을 바탕으로 다음을 수행하세요:
- 동일한 제휴서비스에 해당하는 상품으로만 추출
- 상품코드 | 상품명 | 월정액 | 데이터용량 형식으로 표로 정리
- 유사 상품 3가지 가격 비교
- 유사 상품 3가지의 장단점 분석
"""
    return generate_text(prompt)