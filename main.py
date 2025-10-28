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
st.caption("파일: countriesMBTI_16types.csv — Altair 기반 인터랙티브 대시보드")

# -------------------------------
# 📂 데이터 불러오기
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 데이터 기본 검증
if "Country" not in df.columns:
    st.error("❌ 'Country' 열을 찾을 수 없습니다. CSV에 'Country' 열이 있어야 합니다.")
    st.stop()

# MBTI 열 자동 감지 (16가지 유형 중 존재하는 것만)
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
available_types = [t for t in mbti_types if t in df.columns]

# -------------------------------
# 🎯 사용자 선택
# -------------------------------
selected_type = st.selectbox(
    "분석할 MBTI 유형을 선택하세요 👇",
    available_types
)

# -------------------------------
# 📊 분석 및 시각화
# -------------------------------
st.subheader(f"🌟 {selected_type} 유형이 높은 국가 TOP 10")

# 상위 10개 국가 추출
top10 = df.nlargest(10, selected_type)[["Country", selected_type]].copy()
top10.columns = ["Country", "Score"]

# Altair 막대 그래프
chart = (
    alt.Chart(top10)
    .mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
    .encode(
        x=alt.X("Score:Q", title=f"{selected_type} 점수", sort="descending"),
        y=alt.Y("Country:N", title="국가", sort="-x"),
        color=alt.Color("Score:Q", scale=alt.Scale(scheme="blues")),
        tooltip=["Country", "Score"]
    )
    .properties(height=400)
    .interactive()
)

st.altair_chart(chart, use_container_width=True)

# -------------------------------
# 🧭 데이터 프리뷰
# -------------------------------
with st.expander("🔍 원본 데이터 보기"):
    st.dataframe(df)

st.markdown(
    """
    ---
    **Tip:** MBTI 유형을 바꿔가며 국가별 분포를 비교해 보세요!  
    데이터 값은 각 나라별 해당 MBTI 비율 혹은 점수로 해석할 수 있습니다.
    """
)
