import pandas as pd

relational_feature_set = 'aux/relational_specs.csv'
df = pd.read_csv(relational_feature_set)
df['foo'] = 0
df_pivot = pd.pivot_table(df, index='tube_assembly_id', columns='spec_id', values='foo').fillna(0)
df_pivot.to_csv('feature_tables/specs.csv')
