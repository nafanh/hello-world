import pandas as pd
import os.path
from statsmodels.stats.anova import AnovaRM


csv_filepath = input("Please enter file path: ")

while not os.path.isfile(csv_filepath):        
    print("Error: That is not a valid file, try again...")
    csv_filepath = input("Please enter a valid file path: ")


df = pd.read_csv(csv_filepath)
print(df)

#2 way ANOVA
aorm2way = AnovaRM(df, 'Score', 'Child', within = ['Session', 'Instructor'])
results = aorm2way.fit()
print(results)



