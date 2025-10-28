import pandas as pd
import numpy as np

# 1. 예제 CSV 생성
np.random.seed(42)

num_rows = 100
data = {
    "Country": np.random.choice(["Korea", "USA", "Japan", "Germany", "France"], num_rows),
    "Year": np.random.randint(2000, 2025, num_rows),
    "Population": np.random.randint(1_000_000, 150_000_000, num_rows),
    "GDP": np.random.randint(10_000, 1_000_000, num_rows),
    "LifeExpectancy": np.random.uniform(50, 90, num_rows).round(1)
}

df = pd.DataFrame(data)
df.to_csv("example_data.csv", index=False)
print("CSV 파일 생성 완료!")

# 2. CSV 불러오기
df = pd.read_csv("example_data.csv")

# 3. 데이터 기본 정보 확인
print("\n=== 데이터 정보 ===")
print(df.info())

print("\n=== 기초 통계 ===")
print(df.describe())

print("\n=== 상위 5개 데이터 ===")
print(df.head())

# 4. 결측치 확인
print("\n=== 결측치 확인 ===")
print(df.isnull().sum())

# 5. 그룹별 통계 (Country 기준)
print("\n=== 국가별 평균 Life Expectancy ===")
print(df.groupby("Country")["LifeExpectancy"].mean())

# 6. 판다스로 시각화: 국가별 평균 GDP
print("\n=== 국가별 평균 GDP 시각화 ===")
avg_gdp = df.groupby("Country")["GDP"].mean().sort_values()
avg_gdp.plot(kind="bar", title="국가별 평균 GDP", ylabel="GDP", xlabel="Country")

# 7. 판다스로 시각화: GDP vs LifeExpectancy 산점도
print("\n=== GDP vs Life Expectancy 시각화 ===")
df.plot.scatter(x="GDP", y="LifeExpectancy", title="GDP vs Life Expectancy")
