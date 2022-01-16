# Read the car_price.csv file and extract data out of it

import pandas as pd
 
data = pd.read_csv("car_price.csv")

# to read first five rows
print(data.head())

# to read last five rows
print(data.tail())