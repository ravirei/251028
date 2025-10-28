import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="데이터 분석 & 시각화", layout="wide")

st.title("예제 데이터 분석 & 시각화 앱")

# 1. 예제 데이터 생성
np.random.seed(42)
num_rows = 100
df = pd.DataFrame({
    "Country": np.random.choice(["Korea","USA","Japan","Germany","France"], num_rows),
    "Year": np.random.randint(2000, 2025, num_rows),
    "Population": np.random.randint(1_000_000, 150_000_000, num_rows),
    "GDP": np.random.randint(10_000, 1_000_000, num_rows),
    "LifeExpectancy": np.random.uniform(50, 90, num_rows).round(1)
})

st.write("### 데이터 상위 5행 확인", df.head())

# 2. 데이터 기본 정보
st.write("### 데이터 요약 정보")
st.write(df.describe())

# 3. 결측치 확인
st.write("### 결측치 확인")
st.write(df.isnull().sum())

# 4. 국가별 평균 Life Expectancy
st.write("### 국가별 평균 Life Expectancy")
st.write(df.groupby("Country")["LifeExpectancy"].mean())

# 5. 국가별 평균 GDP 시각화 (Bar Chart)
st.write("### 국가별 평균 GDP")
avg_gdp = df.groupby("Country")["GDP"].mean()
st.bar_chart(avg_gdp)

# 6. GDP vs LifeExpectancy 산점도
st.write("### GDP vs Life Expectancy")
st.scatter_chart(df[["GDP","LifeExpectancy"]])
