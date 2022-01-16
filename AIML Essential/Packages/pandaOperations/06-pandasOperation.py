# create a disctionary with three keys and two values
# conver the same into a dataFrame using pandas

import pandas as pd

thisdict = {
  "brand": ["Ford","Maruti"],
  "model": ["Mustang","Test"],
  "year": [1964,1965]
}
e = pd.DataFrame(thisdict)
print(e)
print(type(e))