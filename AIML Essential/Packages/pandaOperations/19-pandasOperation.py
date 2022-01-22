# car price.csv, according to doornumber & drivewheel , mean of carlength

import pandas as pd

data = pd.read_csv('car_price.csv')
print(data.head())
print(data.columns)

print("Car length mean :- ")
print(data.groupby(['doornumber','drivewheel'])['carlength'].mean())