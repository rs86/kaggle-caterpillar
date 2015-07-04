import pandas as pd

df = pd.read_csv('raw/bill_of_materials.csv')

# What are al the components, and where can we find information about them?
component_columns = []
for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    component_columns.append(df['component_id_' + str(i)])

components = set().union(*component_columns)

print "There are " + str(len(components)) + " components in bill_of_materials.csv"
