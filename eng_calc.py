
import pandas as pd

file_path = r"C:\Users\nhuan\Downloads\12-06-21-H-1-RHS-ENG-MR-W.csv"
df = pd.read_csv(file_path)
unique_labels = sorted(list(df['Label'].unique()))
times = {}
start_interval = int(input("start interval: "))
end_interval = int(input("end interval: "))
total_time = (end_interval - start_interval + 1) * 10
replace_list = ["bt/peers","instructor/screen/on task"]
df = df[(df['Interval'] >= start_interval)
                      & (df['Interval'] <= end_interval)]
df.replace(unique_labels, replace_list, inplace=True)

fixed_labels = sorted(list(df['Label'].unique()))
for label in fixed_labels:
    df_label = df[df['Label'] == label].copy()
    # print(df_label)
    df_label['time held'] = df_label['Time Released'] - df_label['Time Pressed'] 
    time_held = round(df_label['time held'].sum(),4)
    times[label] = time_held
times['off target'] = round(total_time - sum(times.values()),4)

total = sum(times.values(),0.0)
perc = {k: round(v/total,4) for k,v in times.items()}
print(times)
print(perc)


# 104 - 23  + 1 = 82 * 10 = 820 seconds