import pandas as pd
data = { 
"Name": ["A", "B", "C", "D", "E", "F"], 
"City": ["Rajahmundry", "Hyderabad", "Chennai", 
"Hyderabad", "Rajahmundry", "Chennai"], 
"Department": ["IT", "HR", "IT", "Finance", "IT", "HR"], 
"Salary": [25000, 40000, 35000, 45000, 50000, 30000], 
"Experience": [1, 3, 2, 5, 6, 2] 
} 
df = pd.DataFrame(data)
print(df)

print(df["Salary"]>35000)

print(df["City"]=="Hyderabad")

print(df[(df["City"]=="Hyderabad") & (df["Salary"]>35000)])
#  Sort employees by salary from highest to lowest.
print(df.sort_values("Salary", ascending=False))

print(df["Salary"].mean())

print(df.groupby("Department")["Salary"].mean())

print(df.groupby("Department")["Salary"].max())

print(df["City"].value_counts())

df["annual_salary"] = df["Salary"] * 12
print(df)

df["experience_level"] = df["Experience"].apply(lambda x: "Senior" if x >= 5 else "Junior")

