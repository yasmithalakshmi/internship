import pandas as pd

# Read an Excel file into a pandas DataFrame.
df = pd.read_excel(r"C:\Users\yasmitha\Downloads\255 (1).xlsx", header=3)

# Display the first five rows; pass a number to head(n) for a different count.
print(df.head())

# Display the last five rows; pass a number to tail(n) for a different count.
print(df.tail())

# Return the DataFrame dimensions as (number_of_rows, number_of_columns).
print(df.shape)

# Return the names of all columns in the DataFrame.
print(df.columns)

# Return the data type of every column.
print(df.dtypes)

# Display DataFrame information such as columns, non-null values, and memory use.
print(df.info())

# Select rows 0 through 5 and all columns using label-based indexing.
print(df.loc[1:2, ['Roll NO', 'Name of the Students']])


# Select rows by integer position; 0:5 includes positions 0 through 4.
print(df.iloc[0:2,1:3])

# Generate descriptive statistics for numeric columns.
print(df.describe())

print(df.isnull().sum())

df.fillna(0, inplace=True)

df.dropna(inplace=True)

df['Percentage'] = df['Percentage'].astype('int')

print(df.head())

df['Percentage'] = df['Percentage'].round().astype('int')
print(df.head())

df.drop_duplicates(inplace=True)

print(df.sort_values(by='Percentage', ascending=False).head(10))

print(df['Marks'].value_counts())

print(df.columns.tolist())

print(df.groupby('Gender')['Marks'].mean())
#feature engineering
df["eligible"] = 'no'

df.loc[(df['Marks']>=60) & (df['Percentage']>=80), 'eligible'] = 'yes'

print(df.head(5))

print(df['eligible'].value_counts())

 #pivot table
print(df.pivot_table(index='section' , columns='Gender', values='Marks', aggfunc='mean'))

#merge two dataframes
students = pd.DataFrame({
    'Roll NO': [1, 2, 3, 4, 5],
    'Name of the Students': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Marks': [85, 90, 78, 92, 88]
 })
 
marks = pd.DataFrame({
    'Roll NO': [1, 2, 2, 4, 5],
    'Percentage': [85, 90, 78, 92, 88]
 })
df_merge_inner = pd.merge(students, marks, on='Roll NO', how='inner')
 
print(df_merge_inner)

df_merge_outer = pd.merge(students, marks, on='Roll NO', how='outer')

print(df_merge_outer)
 
df_merge_inner.to_csv(r"C:\Users\yasmitha\Downloads\merged_data.csv")

 
print(df[(df['Marks']>60)&(df['Percentage']>80)])

print(df[df['Marks']>70])

print(df[df['Percentage']<75])

print(df[(df['Marks']>=60) & (df['Percentage']>=80)])

print(df[(df['Marks']>90) | (df['Backlogs']>0)])

print(df[df['Marks'].between(60, 80)])

print(df[df['Gender'].isin(['mail', 'femail'])])

print(df[df['Percentage'].between(75, 90)])

print(df[df['Name of the Students'].str.contains('a', case=False, na=False)])

print(df[df['eligible'] != 'yes'])

df2 = df.copy()

df2.rename(columns={'Marks': 'Total Marks'}, inplace=True)

df2.rename(columns={'Roll NO': 'Roll Number', 'Percentage': 'Percentage_score'}, inplace=True)

#df2.drop(columns=['Backlogs'], inplace=True)

df2.drop(columns=['Backlogs','Gender'],inplace=True)

print(df2.columns)

print(df2.head())

df['Name of the Students'] = df['Name of the Students'].str.upper()

df['Name of the Students'] = df['Name of the Students'].str.lower()

df['Name of the Students'] = df['Name of the Students'].str.strip()

df['contains_s'] = df['Name of the Students'].str.contains('s', case=False, na=False)

df['starts_with_a'] = df['Name of the Students'].str.startswith('A', na=False)

df['ends_with_n'] = df['Name of the Students'].str.endswith('n', na=False)

df['Results'] = df['Marks'].apply(lambda x: 'pass' if x >= 60 else 'fail')

df['Performance'] = df['Marks'].apply(lambda x: 'excellent' if x >= 90
                                       else 'good' if x >= 75
                                       else 'average' if x >=60
                                       else 'poor')

class_a = pd.DataFrame({
    'name': ['ravi', 'sita'],
    'marks': [80, 90]
})

class_b = pd.DataFrame({
    'name': ['kiran','priya'],
    'marks':[75, 85]
    
})

results = pd.concat([class_a, class_b],ignore_index=True)

print(results)

results_2 = pd.concat([class_a, class_b], axis = 1)

print(results_2)

print(pd.merge(students, marks, on = 'Roll NO', how = 'left'))
print(pd.merge(students, marks, on = 'Roll NO', how = 'right'))

df2.set_index('Roll Number', inplace=True)

print(df2.head(5))

df2.reset_index(inplace=True)

print(df2.head(5))

print(df['Gender'].unique())

print(df['Gender'].nunique())

print(df['section'].unique())

print(df['section'].nunique())

print(df['eligible'].unique())

print(df['eligible'].nunique())

print(df['eligible'].value_counts())
