# Create a data frame which contains fueltype and enginelocation

import pandas as pd
 
df = pd.read_csv("car_price.csv")

print(df.head())

# divide the dataframe into two set of data frames
# splitting dataframe by row index
# df_1 = data.iloc[0:51,:]
# df_2 = data.iloc[51:99,:]
# print("Shape of new dataframes - {} , {}".format(df_1.shape, df_2.shape))

#print(df_1)
#print(df_2)

df_1 = df.iloc[0:int(df.shape[0]/2),:]
df_2 = df.iloc[int(df.shape[0]/2)+1:int(df.shape[0]),:]
print("Shape of new dataframes - {} , {}".format(df_1.shape, df_2.shape))

print(df_1)
print(df_2)

# reset the index number for df_2 - Use reset_index() function

df_2 = df_2.reset_index()
print(df_2)

# create df3 --> and try to merge df1, df2 according to column names

df_3 = pd.concat([df_1,df_2], axis = 0)
print(df_3.head())