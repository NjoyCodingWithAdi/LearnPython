# Read the name.txt file and extract data out of it

import numpy as np
import pandas as pd
 
# data = np.loadtxt('names.txt') ' problem with numpy is it only reads numbers

# Below code will take the first data as column name
data = pd.read_csv('names.txt')
print(data)

dataOne = pd.read_csv('names.txt', header=None)
print(dataOne)

# conver the dataFrame into list
names = data.values.tolist()
print(names)

# Assignment --> read the data and convert into a single list