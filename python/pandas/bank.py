import pandas as pd

df = pd.read_csv("bank dataset.csv")
print(df)

print("highest balance :", df.loc[df["Balance"].idxmax()])

print("lowest balance :", df.loc[df["Balance"].idxmin()])

print("customers with loans above 5 lakh :")
print(df[df["Loan"] > 500000])

print("city-wise customers :")
print(df.groupby("City")["Customer_ID"].count())

print("total balance :", df["Balance"].sum())
 