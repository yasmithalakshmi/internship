import pandas as pd
data = { 
"Employee": ["A", "B", "C", "D", "E", "F"], 
"Department": ["IT", "HR", "IT", "Sales", "HR", "IT"], 
"Salary": [40000, 30000, 50000, 35000, 32000, 60000], 
"Experience": [2, 1, 4, 3, 2, 6] 
} 
df = pd.DataFrame(data)

print(df["Salary"]>40000)

print(df["Salary"].mean())

print(df["Salary"].max())

print(df.loc[df["Salary"].idxmax()])

print(df.groupby("Department")["Salary"].mean())

print(df["Department"].value_counts())

print(df[df["Experience"]>3])

df["AnnualSalary"] = df["Salary"] * 12
print(df)

    





