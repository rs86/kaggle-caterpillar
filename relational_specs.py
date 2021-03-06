import pandas as pd

df = pd.read_csv('raw/specs.csv')

lines = []

for i in df.index:
    row = df.loc[i]
    tube_assembly_id = row['tube_assembly_id']
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        k = 'spec' + str(j)
        if type(row[k]) == str:
            lines.append((tube_assembly_id, row[k]))

new_df = pd.DataFrame(lines, columns=['tube_assembly_id', 'spec_id'])
new_df.to_csv('processed/tube_specs.csv', index=False)
