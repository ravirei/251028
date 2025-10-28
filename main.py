import streamlit as st
import pandas as pd
import altair as alt

# -------------------------------
# 🌍 기본 설정
# -------------------------------
st.set_page_config(
    page_title="MBTI by Country Explorer",
    page_icon="🌎",
    layout="centered"
)

st.title("🌎 MBTI 유형별 국가 TOP 10 시각화")
st.caption("MBTI 분포 데이터를 업로드하면, 특정 유형이 높은 국가 TOP 10을 시각화합니다.")

# -------------------------------
# 📂 CSV 업로드
# -------------------------------
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요 (예: countriesMBTI_16types.csv)", type=["csv"])

if uploaded_file is None:
    st.info("👆 CSV 파일을 업로드하면 분석이 시작됩니다.")
    st.stop()

# 데이터 읽기
try:
    df = pd.read_csv(uploaded_file)
except Exception as e:
    st.error(f"❌ CSV 파일을 읽는 중 오류가 발생했습니다: {e}")
    st.stop()

# -------------------------------
# 🔎 기본 검증
# -------------------------------
if "Country" not in df.columns:
