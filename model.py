import pandas as pd
import numpy as np
from sklearn import linear_model


tubes = pd.read_csv('raw/tube.csv')
materials = pd.get_dummies(tubes['material_id'])
end_x = pd.get_dummies(tubes['end_x'])
end_a = pd.get_dummies(tubes['end_a'])

tube_assembly_features = pd.concat([materials, tubes, end_a, end_x], axis=1)

train_set = pd.read_csv('raw/train_set.csv')
bracket_pricing = pd.get_dummies(train_set['bracket_pricing'])

train_set = pd.concat([bracket_pricing, train_set], axis=1)

df = pd.merge(train_set, tube_assembly_features, on='tube_assembly_id')

print df.shape
print train_set.shape

assert df.shape[0] == train_set.shape[0]

columns = list(materials.columns) + ['quantity', 'length', 'wall', 'diameter'] + list(end_x.columns) + list(end_a.columns)

train_x = df.select_dtypes([np.float64]).fillna(0).drop('cost', axis=1)

for c in train_x.columns:
    if not c in columns:
        train_x.drop(c, axis=1, inplace=True)

train_y = np.log1p(df.cost)

LR = linear_model.LinearRegression()
LR.fit(train_x, train_y)

print LR.score(train_x, train_y)
