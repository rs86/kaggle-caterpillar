# Convert bill of materials to a more tractable format

import pandas as pd

df = pd.read_csv('raw/specs.csv')

rows_output = []

for i in range(len(df)):
    row = df.loc[i]
    ta = row['tube_assembly_id']
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:

        v = row['spec' + str(j)]

        if type(v) == str:
            rows_output.append((ta, v))

columns=['tube_assembly_id', 'component_id']

df = pd.DataFrame(rows_output, columns=columns)
df['x'] = 1
df = pd.pivot_table(df, index='tube_assembly_id', columns='component_id', values='x').fillna(0)
df.to_csv('processed/tube_specs.csv')
