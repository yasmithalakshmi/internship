import pandas as pd
df = pd.read_csv(r"e-commerce.csv")
print(df)
#most expensive product
print(df['Price'].max())
#xheapest product
print(df['Price'].max())
#avg rate
print(df['Rating'].mean())
#category wise products
print(df.groupby('Category')['Product'].apply(list))
# Total inventory value (  Price × Quantity  ).
print(df['Price'].sum() * df['Quantity'].sum())