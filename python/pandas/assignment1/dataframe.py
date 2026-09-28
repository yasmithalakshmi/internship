import pandas as pd 
data = { 
"Name": ["Anu", "Ravi", "Kiran", "Sita", "Rahul"], 
"Age": [22, 25, 21, 24, 27], 
"City": ["Rajahmundry", "Hyderabad", "Chennai", "Rajahmundry", "Hyderabad"], 
"Salary": [25000, 45000, 30000, 35000, 55000], 
"Department": ["IT", "HR", "IT", "Finance", "IT"] 
} 
df = pd.DataFrame(data) 
print(df)

#filtering data
result = df[df["Salary"] > 30000] 
print(result)

#multiple conditions
result = df[ 
(df["Salary"] > 30000) & 
(df["Department"] == "IT") 
] 
print(result)

#or

result = df[ 
(df["City"] == "Hyderabad") | 
(df["City"] == "Rajahmundry") 
] 
print(result)

#filtering using isin(without need to mu)
result = df[df["City"].isin(["Hyderabad", "Chennai"])] 
print(result)

#sort the values ascending
df.sort_values("Salary")

#descending
df.sort_values("Salary", ascending=False)

#sort based on multiple values
df.sort_values( 
["Department", "Salary"], 
ascending=[True, False] 
)

#create a new column
df["Bonus"] = df["Salary"] * 0.10 
print(df) 

#calculate total salary
df["TotalSalary"] = df["Salary"] + df["Bonus"] 
print(df)

#conditional column with np.where
import numpy as np 
df["Level"] = np.where( 
df["Salary"] >= 40000, 
"Senior", 
"Junior" 
) 
print(df) 

#group by
result = df.groupby("Department")["Salary"].mean() 
print(result)

#multiple aggregations
result = df.groupby("Department")["Salary"].agg( 
["count", "sum", "mean", "min", "max"] 
) 
print(result)

#group by city
result = df.groupby("City")["Salary"].mean() 
print(result)

#group by multiple columns
result = df.groupby( 
["City", "Department"] 
)["Salary"].mean() 
print(result)

#value counts
print(df["Department"].value_counts())

#city wise count
print(df["City"].value_counts()) 

#missing values
data = { 
"Name": ["Anu", "Ravi", "Kiran", "Sita"], 
"Age": [22, None, 21, 24], 
"Salary": [25000, 45000, None, 35000] 
} 
df = pd.DataFrame(data) 
print(df)
print(df.isnull()) 

#countmissing values
print(df.isnull().sum())

#Fill Age with average age 
df["Age"] = df["Age"].fillna(df["Age"].mean()) 

#Fill Salary with 0 
df["Salary"] = df["Salary"].fillna(0)
print(df)

#remove missing rows
df.dropna(inplace=True)
print(df)

#remove duplicate data
df.drop_duplicates(inplace=True)
print(df)

#remove duplicate based on specific column
df.drop_duplicates(subset=["Name"], inplace=True)

#rename columns
df.rename( 
columns={ 
"Salary": "MonthlySalary", 
"Age": "EmployeeAge" 
}, 
inplace=True 
) 
print(df)

#for label selection 
print(df.loc[0])

#iloc for spectific index
print(df.iloc[0])







