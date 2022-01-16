# pandas: pandas is an external package <mainly used for mathematical calculations >
# pandas :- Python Data Analysis Library
# https://pandas.pydata.org/
# Reference :- https://pandas.pydata.org/docs/reference/index.html

a = [5,6,7]

# conver the above into series

import pandas as pd
import numpy as np

b = pd.Series(a)

print(b)

d = np.array(['a','b','c','d'])
e = pd.Series(d)
print(e)