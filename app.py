import streamlit as st
import os
from dotenv import load_dotenv

# 환경 변수 로드 (사용자 성함 등)
load_dotenv()
my_name = os.getenv('MY_NAME', '관리자')

st.set_page_config(
    page_title=f"{my_name}의 AI 금융 분석 플랫폼",
    page_icon="📈",
    layout="wide"
)

# 메인 헤더
st.title("📈 AI-Powered Financial Analytics")
st.subheader(f"Welcome, {my_name}!")

st.divider()

# 서비스 소개 섹션
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🤖 Gemini AI와 함께하는 스마트한 투자 분석")
    st.info("""
    본 플랫폼은 **Gemini 1.5 Flash** 모델의 기술적 지원을 받아 구축된 지능형 금융 데이터 분석 도구입니다. 
    사용자는 복잡한 설정 없이 상장사 데이터를 실시간으로 조회하고, AI가 제안하는 기술적 분석 지표를 확인할 수 있습니다.
    """)
    
    st.write("#### ✅ 핵심 제공 기능")
    st.write("- **실시간 주가 데이터 수집**: KRX 상장사 전체 종목 지원")
    st.write("- **기술적 분석 지표**: 이동평균선(MA20, MA60) 자동 계산 및 시각화")
    st.write("- **데이터 인터랙션**: 분석 결과의 엑셀 추출 및 세부 데이터 확인")

with col2:
    st.write("#### 🛠 Tech Stack")
    st.code("""
- Language: Python
- Library: Streamlit, Pandas
- Data: FinanceDataReader
- AI Engine: Gemini 1.5 Flash
    """, language="markdown")

st.divider()
st.caption("왼쪽 사이드바의 메뉴를 통해 상세 분석 기능을 이용해 보세요.")