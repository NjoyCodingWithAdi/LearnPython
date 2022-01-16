# change the index to 100, 101, 102, 103

import pandas as pd
import numpy as np

d = np.array(['a','b','c','d'])
e = pd.Series(d, index = [100,101,102,103])
print(e)