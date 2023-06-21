# This is pearsonr and p-value.

import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv('climate_change_data.csv')

column_list = df.columns.to_list()

# results = []
# if df['country'] == 
#     for i in range(3, len(df.columns)):
#         if i == len(df.columns)-1:
#             continue
#         for j in range(3, len(df.columns)):
#             if i == j:
#                 continue
#             column1 = df[column_list[i]]
#             column2 = df[column_list[j]]
#             corr, p_value = pearsonr(column1, column2)
#             if p_value < .05:
#                 results.append(f'The relation and p-value between {column_list[i]} & {column_list[j]} are {corr}, {p_value}')

# with open('Asia.txt', 'w', encoding='utf-8') as f:
#     for i in results:
#         f.write(i + '\n')
#     f.close()