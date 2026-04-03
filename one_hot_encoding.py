# one hot encodng
# converts categorical variables to binary ones
# [Red, Green, Blue]
# Red: [1, 0, 0]
# Green: [0, 1, 0]
# Blue: [0, 0, 1]

# using sklearn
from sklearn.preprocessing import OneHotEncoder

data = [['Red'], ['Green'], ['Blue']]

encoder = OneHotEncoder(sparse=False)
encoded = encoder.fit_transform(data)

print(encoded)

# using pandas
import pandas as pd

df = pd.DataFrame({'Color': ['Red', 'Green', 'Blue']})

encoded = pd.get_dummies(df['Color'])
print(encoded)
