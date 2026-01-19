import streamlit as st
import os
from dotenv import load_dotenv

# 1. 반드시 최상단에 위치해야 함 (코드 문제의 90%가 여기서 발생)
st.set_page_config(
    page_title="AI 금융 분석 플랫폼",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 환경 변수 로드
load_dotenv()
my_name = os.getenv('MY_NAME', '관리자')

# 3. 메인 헤더
st.title("📈 AI-Powered Financial Analytics")
st.subheader(f"Welcome, {my_name}!")

st.divider()

# 4. 서비스 소개 (메인 화면 내용)
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🤖 Gemini AI와 함께하는 스마트한 투자 분석")
    st.info("""
    본 플랫폼은 **Gemini 1.5 Flash** 모델의 기술적 지원을 받아 구축된 지능형 금융 데이터 분석 도구입니다. 
    왼쪽 사이드바 메뉴를 통해 상세 기능을 이용해 보세요.
    """)
    
    st.write("#### ✅ 제공 기능")
    st.write("- **01 주가 분석**: 실시간 데이터 시각화 및 기술적 지표")
    st.write("- **02 AI 인사이트**: Gemini 기반 시장 리포트 (준비 중)")

with col2:
    st.write("#### 🛠 Tech Stack")
    st.code("- Streamlit\n- Pandas\n- Gemini API", language="markdown")

st.divider()
st.caption("사이드바가 보이지 않는다면 왼쪽 상단의 '>' 버튼을 눌러주세요.")