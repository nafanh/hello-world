import pandas as pd
df = pd.read_csv(r"C:\Users\katie\OneDrive\Documents\dataset 1.csv")
df = df.assign(Time_Depressed = df['Time Released']- df['Time Pressed'])
print(df)