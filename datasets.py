import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor


# TRAIN AND TESTS

train_set = pd.read_csv('raw/train_set.csv', parse_dates=[2])
test_set = pd.read_csv('raw/test_set.csv', parse_dates=[3])










train_set = pd.concat([pd.get_dummies(train_set.bracket_pricing), train_set], axis=1)

train_set['year'] = train_set.quote_date.dt.year
train_set['month'] = train_set.quote_date.dt.month
train_set['day'] = train_set.quote_date.dt.day

# data from tube.csv w/ dummies
tube = pd.read_csv('raw/tube.csv')
tube_components = pd.read_csv('processed/tube_components.csv')
dummies_material = pd.get_dummies(tube['material_id'])
dummies_end_a = pd.get_dummies(tube['end_a'])
dummies_end_x = pd.get_dummies(tube['end_x'])
tube_specs = pd.read_csv('processed/tube_specs.csv')

df_train = pd.concat([dummies_end_x, dummies_end_a, dummies_material, tube], axis=1)
df_train = pd.merge(df_train, tube_components, on='tube_assembly_id', how='left')
df_train = pd.merge(df_train, tube_specs, on='tube_assembly_id', how='left')

df_train = pd.merge(train_set, df_train, on='tube_assembly_id', how='left')

numeric = [np.float64, np.int64]

train_x = df_train.drop('cost', axis=1).select_dtypes(numeric).fillna(0)
train_y = df_train.cost

RF = RandomForestRegressor(random_state=0, n_estimators=100)
RF.fit(train_x, np.log1p(train_y))

print RF.score(train_x, np.log1p(train_y))

# PREDIT TEST SET

test_set = pd.concat([pd.get_dummies(test_set.bracket_pricing), test_set], axis=1)

test_set['year'] = test_set.quote_date.dt.year
test_set['month'] = test_set.quote_date.dt.month
test_set['day'] = test_set.quote_date.dt.day

# data from tube.csv w/ dummies
df_test = pd.concat([dummies_end_x, dummies_end_a, dummies_material, tube], axis=1)
df_test = pd.merge(df_test, tube_components, on='tube_assembly_id', how='left')
df_test = pd.merge(df_test, tube_specs, on='tube_assembly_id', how='left')

df_test = pd.merge(test_set, df_test, on='tube_assembly_id', how='left')

print df_train.shape
print df_test.shape

numeric = [np.float64, np.int64]

test_x = df_test.select_dtypes(numeric).fillna(0).drop('id', axis=1)

predictions = [(i+1, p) for i, p in enumerate(np.expm1(RF.predict(test_x)))]

f = open('submission.csv','w')
f.write("id,cost\n")

for i, p in predictions:
    f.write(str(i) + "," + str(p) + "\n")

f.close()


