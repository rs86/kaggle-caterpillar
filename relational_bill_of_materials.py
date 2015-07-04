import pandas as pd

df = pd.read_csv('raw/bill_of_materials.csv')

lines = []

for i in df.index:
    row = df.loc[i]
    for j in [1, 2, 3, 4, 5, 6, 7, 8]:
        cid_key = 'component_id_' + str(j)
        quantity_key = 'quantity_' + str(j)
        if type(row[cid_key]) == str:
            line = row['tube_assembly_id'], row[cid_key], row[quantity_key]
            lines.append(line)

new_df = pd.DataFrame(lines, columns=['tube_assembly_id', 'component_id', 'quantity'])
new_df.to_csv('aux/relational_bill_of_materials.csv')
