from enum import unique
import pandas as pd

# file path of engagement .csv 
file_path = r"C:\Users\nhuan\Downloads\12-06-21-H-1-RHS-ENG-MR-W.csv"

# read in .csv into pandas dataframe
df = pd.read_csv(file_path)

print('---------------------------------------------------------------')
# user input of start and end intervals. This is needed bc there is dead time from when the session starts and when the session ends
start_interval = int(input("start interval: "))
end_interval = int(input("end interval: "))
# add separator
print('---------------------------------------------------------------')

# total time of the session, which is just the (end interval - start interval + 1) * 10. Bc each interval is 10 seconds
# add one because technically, we are counting interval 0 as a time point
total_time = (end_interval - start_interval + 1) * 10

# restrict dataframe (df) to start and end intervals. This is if the coder coded data before or after start and end intervals respectively
df = df[(df['Interval'] >= start_interval)
                      & (df['Interval'] <= end_interval)]

# create a column called 'time held' which has the time the button is depressed.
# which is the time released column - the time pressed column (vectorized)
df['time held'] = df['Time Released'] - df['Time Pressed']

# get the unique labels
unique_labels = df['Label'].unique()

#iterate through each label to get the total time in seconds
for label in unique_labels:
    # sum of the values of each label
    label_sum = df.loc[df['Label'] == label , 'time held'].sum()
    print(label + " total time: " + str(round(label_sum,4)) + ' seconds')
    print(label + " percentage: " + str(round((label_sum/total_time) * 100 ,4)) + ' %' )
    # add separator
    print('---------------------------------------------------------------')

# add off target label
# get off target time and peprcentage
# add separator
off_target_time = round(total_time - df['time held'].sum(),4)
off_target_percentage = round((off_target_time/total_time) * 100 ,4)
print('off target total time: ' + str(off_target_time) + ' seconds' )
print('off target percentage: ' + str(off_target_percentage) + ' %' )