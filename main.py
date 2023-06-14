# This is pearsonr and p-value. 
# The results is Wind Speed does have relationships with Temperature and Humidity.
import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv('climate_change_data.csv')
df.fillna(0, inplace=True)

column_list = df.columns.to_list()

results = []

for i in range(3, len(df.columns)):
    if i == len(df.columns)-1:
        continue
    for j in range(3, len(df.columns)):
        if i == j:
            continue
        column1 = df[column_list[i]]
        column2 = df[column_list[j]]
        corr, p_value = pearsonr(column1, column2)
        if p_value < .05:
            results.append(f'The relation and p-value between {column_list[i]} & {column_list[j]} are {corr}, {p_value}')

for i in results:
    print(i)