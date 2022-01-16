# create a series from 1,2,3,4,5 and index a --> e
# extract the last three elements of the series

import pandas as pd
import numpy as np

d = np.array([1,2,3,4,5])
e = pd.Series(d, index = ['a','b','c','d','e'])
print(e[-3:])