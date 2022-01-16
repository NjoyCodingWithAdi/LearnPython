# create a disctionary with three keys and a single value
# conver the dictionary into series

import pandas as pd

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
e = pd.Series(thisdict)
print(e)