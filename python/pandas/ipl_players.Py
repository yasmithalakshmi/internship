import pandas as pd
df = pd.read_csv(r"ipl.csv")
print(df)
#highest runs
print(df[df['Runs'] == df['Runs'].max()])
#top 5 players
print(df.nlargest(5 ,'Runs'))
#team wise average
print(df.groupby('Team')['Runs'].mean())
#highest strike rate
print(df[df['Strike Rate'] == df['Strike Rate'].max()])
#sort by runs
print(df.sort_values(by='Runs', ascending=False))