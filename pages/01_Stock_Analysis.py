import streamlit as st
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import koreanize_matplotlib
import datetime
from io import BytesIO

# 기본 설정1
# st.set_page_config(page_title="Technical Analysis", layout="wide")
st.title("🔍 주가 기술적 분석 엔진")

# --- 함수 정의 ---
@st.cache_data
def get_krx_company_list() -> pd.DataFrame:
    try:
        url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'
        df_listing = pd.read_html(url, header=0, flavor='bs4', encoding='EUC-KR')[0]
        df_listing = df_listing[['회사명', '종목코드']].copy()
        df_listing['종목코드'] = df_listing['종목코드'].apply(lambda x: f'{x:06}')
        return df_listing
    except Exception as e:
        st.error(f"상장사 명단 로드 실패: {e}")
        return pd.DataFrame(columns=['회사명', '종목코드'])

def get_stock_code(company_name: str) -> str:
    if company_name.isdigit() and len(company_name) == 6:
        return company_name
    company_df = get_krx_company_list()
    codes = company_df[company_df['회사명'] == company_name]['종목코드'].values
    if len(codes) > 0: return codes[0]
    else: raise ValueError(f"'{company_name}'을 찾을 수 없습니다.")

# --- 사이드바 입력 구역 ---
with st.sidebar:
    st.header("분석 설정")
    company_name = st.text_input('종목명 또는 코드 입력')
    today = datetime.datetime.now()
    jan_1 = datetime.date(today.year, 1, 1)
    selected_dates = st.date_input('조회 날짜', (jan_1, today))
    confirm_btn = st.button('분석 시작')

# --- 메인 로직 ---
if confirm_btn:
    if not company_name:
        st.warning("조회할 회사 이름을 입력하세요.")
    else:
        try:
            with st.spinner('데이터 분석 중...'):
                stock_code = get_stock_code(company_name)
                start_date = selected_dates[0].strftime("%Y%m%d")
                end_date = selected_dates[1].strftime("%Y%m%d")
                price_df = fdr.DataReader(stock_code, start_date, end_date)

            if price_df.empty:
                st.info("해당 기간의 주가 데이터가 없습니다.")
            else:
                st.subheader(f"[{company_name}] 분석 리포트")
                
                # 지표 계산
                price_df['MA20'] = price_df['Close'].rolling(window=20).mean()
                price_df['MA60'] = price_df['Close'].rolling(window=60).mean()

                # 시각화
                fig, ax = plt.subplots(figsize=(12, 5))
                price_df['Close'].plot(ax=ax, grid=True, color='red', label='종가')
                price_df['MA20'].plot(ax=ax, label='20일선', linestyle='--')
                price_df['MA60'].plot(ax=ax, label='60일선', linestyle='--')
                ax.set_title(f"{company_name} 주가 추이", fontsize=15)
                ax.legend()
                st.pyplot(fig)

                # 데이터 테이블 및 엑셀 다운로드
                with st.expander("데이터 상세 보기"):
                    st.dataframe(price_df.tail(10), use_container_width=True)
                    output = BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        price_df.to_excel(writer, index=True)
                    st.download_button(label="📥 엑셀 다운로드", data=output.getvalue(), file_name=f"{company_name}.xlsx")
        except Exception as e:
            st.error(f"오류 발생: {e}")