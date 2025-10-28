# 1. 설치 (Streamlit 터미널이나 로컬에서 한 번만 실행)
# pip install matplotlib pandas numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 2. 예제 CSV 생성
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

# 3. CSV 불러오기
df = pd.read_csv("example_data.csv")

# 4. 데이터 기본 정보
print("\n=== 데이터 정보 ===")
print(df.info())

print("\n=== 기초 통계 ===")
print(df.describe())

print("\n=== 상위 5개 데이터 ===")
print(df.head())

# 5. 결측치 확인
print("\n=== 결측치 확인 ===")
print(df.isnull().sum())

# 6. 그룹별 통계
print("\n=== 국가별 평균 Life Expectancy ===")
print(df.groupby("Country")["LifeExpectancy"].mean())

# 7. 국가별 평균 GDP 시각화
avg_gdp = df.groupby("Country")["GDP"].mean().sort_values()
plt.figure(figsize=(10,6))
avg_gdp.plot(kind="bar", color="skyblue")
plt.title("국가별 평균 GDP")
plt.ylabel("GDP")
plt.xlabel("Country")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 8. GDP vs LifeExpectancy 산점도
plt.figure(figsize=(8,6))
plt.scatter(df["GDP"], df["LifeExpectancy"], c='orange')
plt.title("GDP vs Life Expectancy")
plt.xlabel("GDP")
plt.ylabel("Life Expectancy")
plt.grid(True)
plt.show()
