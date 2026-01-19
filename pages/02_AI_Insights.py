import streamlit as st

# st.set_page_config(page_title="AI Insights", layout="wide")
st.title("🤖 Gemini AI 시장 인사이트")

st.info("이 페이지는 Gemini API를 활용하여 고도화된 데이터 해석을 제공하는 준비 단계입니다.")

st.subheader("🔍 주요 분석 타겟")
col1, col2 = st.columns(2)

with col1:
    st.write("#### ⚠️ 이상탐지 (Anomaly Detection)")
    st.write("- 주가의 급격한 변동이나 거래량 폭증 사례 분석")
    st.write("- 과거 패턴 기반의 특이점 도출")

with col2:
    st.write("#### 📝 뉴스 감성 분석 (Sentiment)")
    st.write("- 종목 관련 뉴스의 긍정/부정 판단")
    st.write("- AI 기반 요약 리포트 자동 생성")

st.divider()
st.write("현재 **Gemini 1.5 Flash** 모델 연동을 위한 백엔드 최적화가 진행 중입니다. 곧 실시간 AI 리포트 기능을 만나보실 수 있습니다.")