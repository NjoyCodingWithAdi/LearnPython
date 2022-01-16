# Important functions -  loc and iloc

import pandas as pd
 
data = pd.read_csv("car_price.csv")

# extract only car name from the above file
print(data.loc[:,'CarName']) #[rows,columns]


print((data.loc[:,'CarName']).head())
