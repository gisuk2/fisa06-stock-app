import streamlit as st  # 1. 스트림릿 임포트

# 2. 반드시!!!! 모든 실행 코드보다 위에 위치해야 함
st.set_page_config(
    page_title="AI 금융 분석 플랫폼",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 3. 그 다음 나머지 라이브러리 임포트 및 실행
import os
from dotenv import load_dotenv

load_dotenv()
my_name = os.getenv('MY_NAME', '관리자')

# --- 이하 메인 UI 로직 ---
st.title("📈 AI-Powered Financial Analytics")
st.subheader(f"Welcome, {my_name}!")

st.divider()

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("### 🤖 Gemini AI와 함께하는 스마트한 투자 분석")
    st.info("왼쪽 사이드바 메뉴를 통해 상세 분석 기능을 이용해 보세요.")
    
with col2:
    st.write("#### 🛠 Tech Stack")
    st.code("- Streamlit\n- Pandas\n- Gemini API", language="markdown")

st.divider()
st.caption("사이드바가 안 보인다면 화면 왼쪽 상단의 '>' 버튼을 눌러주세요.")