import pandas as pd

df = pd.read_csv("ecommerce dataset.csv")
print(df)

print("most expensive product :", df.loc[df["Price"].idxmax()])

print("cheapest product :", df.loc[df["Price"].idxmin()])

print("average rating :", df["Rating"].mean())

print("category-wise products :")
print(df.groupby("Category")["Product"].count())

df["Inventory_Value"] = df["Price"] * df["Quantity"]

print("total inventory value :", df["Inventory_Value"].sum())