import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor


# TRAIN AND TESTS

train_set = pd.read_csv('raw/train_set.csv', parse_dates=[2])
test_set = pd.read_csv('raw/test_set.csv', parse_dates=[3])

# ADD DATE FEATURES
def add_date_features(df):
    df['year'] = df.quote_date.dt.year
    df['month'] = df.quote_date.dt.month
    df['day'] = df.quote_date.dt.day

add_date_features(train_set)
add_date_features(test_set)

# TUBE FEATURES
tube = pd.read_csv('raw/tube.csv')
specs = pd.read_csv('processed/tube_specs.csv')
# components = pd.read_csv('processed/tube_components.csv')

train_set = pd.merge(train_set, tube, on='tube_assembly_id', how='left')
train_set = pd.merge(train_set, specs, on='tube_assembly_id', how='left').fillna(0)
# train_set = pd.merge(train_set, components, on='tube_assembly_id', how='left').fillna(0)

numeric = [np.float64, np.int64]

for c in specs.select_dtypes(numeric).columns:
    x = (train_set[c] == 1).sum()
    if x == 0:
        del train_set[c]

# for c in components.select_dtypes(numeric).columns:
#    x = (train_set[c] == 1).sum()
#    if x == 0:
#        del train_set[c]

rows = []

for c in train_set.select_dtypes(numeric).columns:
    x = train_set[c]
    rows.append((c.ljust(20), np.corrcoef(x, train_set.cost)[1][0], np.mean(x)))

rows = sorted(rows, key=lambda x: x[1], reverse=True)

for row in rows:
    print map(lambda x: str(x).ljust(20), row)
