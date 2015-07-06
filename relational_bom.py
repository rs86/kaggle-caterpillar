# Convert bill of materials to a more tractable format

import pandas as pd

df = pd.read_csv('raw/bill_of_materials.csv')

rows_output = []

for i in range(len(df)):
    row = df.loc[i]
    ta = row['tube_assembly_id']
    for j in [1, 2, 3, 4, 5, 6, 7, 8]:

        v = row['component_id_' + str(j)]
        q = row['quantity_' + str(j)]

        if type(v) == str:
            rows_output.append((ta, v, q))
columns=['tube_assembly_id', 'component_id', 'quantity']

df = pd.DataFrame(rows_output, columns=columns)
df = pd.pivot_table(df, index='tube_assembly_id', columns='component_id', values='quantity')
df.to_csv('processed/tube_components.csv')
