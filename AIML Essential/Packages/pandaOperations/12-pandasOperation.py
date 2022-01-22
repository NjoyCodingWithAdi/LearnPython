# Create a data frame which contains fueltype and enginelocation

import pandas as pd
 
data = pd.read_csv("car_price.csv")

# From Data frame remove duplicate rows use function duplicated()
# cleanData =  data.duplicated()
# print(cleanData)

cleanDataOne =  data[data.duplicated()]
print(cleanDataOne)