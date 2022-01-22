# merge, concat, append and join method to join two dataFrames

# Use join method and do the same thing which we did with concat 

import pandas as pd
 
df = pd.read_csv("car_price.csv")

df_1 = df.iloc[0:int(df.shape[0]/2),:]
df_2 = df.iloc[int(df.shape[0]/2)+1:int(df.shape[0]),:]

print(df_1.head())
print(df_2.head())
 