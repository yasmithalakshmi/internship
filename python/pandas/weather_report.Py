import pandas as pd
df = pd.read_csv(r"weather report.csv")
print(df)
# avg temp
print(df['Temperature'].mean())
#hottest city
print(df['Temperature'].max())
#coldest city
print(df['Temperature'].min())
#city above 35 c
print(df['Temperature'] > 35)
#sort by rainfall
print(df.sort_values(by='Rainfall', ascending=False))