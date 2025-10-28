import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="MBTI by Country Explorer", page_icon="🌎", layout="centered")

st.title("🌎 MBTI 유형별 국가 TOP 10 시각화")
st.caption("MBTI 분포 데이터를 업로드하면, 특정 유형이 높은 국가 TOP 10을 시각화합니다.")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요 (예: countriesMBTI_16types.csv)", type=["csv"])

if uploaded_file is None:
    st.info("👆 CSV 파일을 업로드하면 분석이 시작됩니다.")
    st.stop()

try:
    df = pd.read_csv(uploaded_file)
except Exception as e:
    st.error(f"❌ CSV 파일을 읽는 중 오류가 발생했습니다: {e}")
    st.stop()

if "Country" not in df.columns:
    st.error("❌ 'Country' 열을 찾을 수 없습니다.")
    st.stop()

# MBTI 열만 추출
mbti_types = [
    "INTJ","INTP","ENTJ","ENTP","INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ","ISTP","ISFP","ESTP","ESFP"
]
available_types = [t for t in mbti_types if t in df.columns]

if not available_types:
    st.error("❌ MBTI 유형 열을 찾을 수 없습니다.")
    st.stop()

# ✅ MBTI 열 숫자형으로 강제 변환
for col in available_types:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ✅ 데이터 검증 출력
st.write("데이터 타입 확인:", df[available_types].dtypes)
st.write("샘플 데이터 (상위 5행):", df.head())

selected_type = st.selectbox("분석할 MBTI 유형을 선택하세요 👇", available_types)

st.subheader(f"🌟 {selected_type} 유형이 높은 국가 TOP 10")

top10 = (
    df[["Country", selected_type]]
    .dropna()
    .sort_values(selected_type, ascending=False)
    .head(10)
    .copy()
)
top10.columns = ["Country", "Score"]

if top10["Score"].isnull().all() or top10["Score"].sum() == 0:
    st.warning("⚠️ 선택한 MBTI 유형의 유효한 수치 데이터가 없습니다. CSV를 확인하세요.")
    st.stop()

# ✅ Altair 그래프 — 숫자 범위에 맞춰 자동 스케일 조정
chart = (
    alt.Chart(top10)
    .mark_bar(size=25, cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
    .encode(
        x=alt.X("Score:Q", title=f"{selected_type} 비율(%)", scale=alt.Scale(domain=[0, top10["Score"].max() * 1.1])),
        y=alt.Y("Country:N", title="국가", sort="-x"),
        color=alt.Color("Score:Q", scale=alt.Scale(scheme="blues")),
        tooltip=["Country", "Score"]
    )
    .properties(height=400)
    .interactive()
)

# ✅ 값 라벨 표시 추가
text = chart.mark_text(align='left', baseline='middle', dx=3).encode(
    text=alt.Text('Score:Q', format='.2f')
)

st.altair_chart(chart + text, use_container_width=True)

with st.expander("🔍 원본 데이터 보기"):
    st.dataframe(df)

st.markdown(
    """
    ---
    **Tip:**  
    1️⃣ MBTI 유형을 바꿔가며 국가별 분포를 비교해 보세요.  
    2️⃣ CSV에는 'Country' 열과 MBTI 16유형(INTJ, ENFP 등) 열이 포함되어야 합니다.
    """
)
