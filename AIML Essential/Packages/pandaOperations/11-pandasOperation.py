# Create a data frame which contains fueltype and enginelocation

import pandas as pd
 
data = pd.read_csv("car_price.csv")

# Way 1 

dataOne = data.loc[:,['fueltype','enginelocation']]

print(dataOne.head())
print(dataOne.tail())

# Way 2

# iloc to pass column index instaed of column names

dataTwo = data.iloc[:,[3,8]]
print(dataTwo.head())
print(dataTwo.tail())


# create a dataFrame df4
# Extract column number --> 5, 9, 13 for the rows between 10-25

df4 = data.iloc[10:26,[5,9,13]]
print(df4.tail())

# Note :- Inorder to extract colunm details we would eb using loc, iloc and column name directly

# Shape of dataset using pandas
print(df4.shape)

print(df4.info())

print(df4.dtypes)

# From dataFrame --> Remove/Drop the column car_id - Drop / Pop / Del(Which is generally not used)

data.pop('car_ID')
print(data.head())

# From Data frame remove duplicate rows use function duplicated()
cleanData =  data.duplicated()
print(cleanData)