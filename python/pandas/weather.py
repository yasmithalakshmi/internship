import pandas as pd

df = pd.read_csv("weather dataset.csv")
print(df)

print("average temperature :", df["Temperature"].mean())

print("hottest city :", df.loc[df["Temperature"].idxmax()])

print("coldest city :", df.loc[df["Temperature"].idxmin()])

print("cities above 35°C :")
print(df[df["Temperature"] > 35])

print("sort by rainfall :")
print(df.sort_values("Rainfall", ascending=False))