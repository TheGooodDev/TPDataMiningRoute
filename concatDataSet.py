import pandas as pd

part1 = pd.read_csv('Dataset/accidents-19-22_P1.csv', low_memory=False)
part2 = pd.read_csv('Dataset/accidents-19-22_P2.csv', low_memory=False)
part3 = pd.read_csv('Dataset/accidents-19-22_P3.csv', low_memory=False)
merged_df = pd.concat([part1, part2, part3])
merged_df.to_csv('accidents-19-22.csv', index=False)