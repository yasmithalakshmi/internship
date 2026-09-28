import pandas as pd
df=pd.read_csv("ipl dataset.csv")
print(df)
print("highest run player row:",df.loc[df["Runs"].idxmax()])   #loc for complete row and idx for inde of that  row
print("highest run player :",df["Runs"].max())   #it just returns the highest number
print("top 5 players:",df.head())
print("team wise average :",df.groupby("Team")["Average"].mean())   #groupby is used to group the data based on team and then we are calculating the average of runs for each team])
print("highest strike rate :",df.loc[df["Strike Rate"].idxmax()])   #loc for complete row and idx for inde of that  row
print("Sort by runs : ",df.sort_values("Runs",ascending=False))   #sort the data based on runs in descending order
