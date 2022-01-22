import pandas as pd
 
df = pd.read_csv("car_price.csv")
print(df.head())

# you use 'merge' function and df_3--> df_1 df_2 column wise. 

df_1 = df.iloc[0:int(df.shape[0]/2),:]
df_2 = df.iloc[int(df.shape[0]/2)+1:int(df.shape[0]),:]

#df_3 = pd.merge(df_1, df_2, how='inner', on='car_Id')
#print(df_3)


# Use append function
df_3 = df_1.append(df_2)
print(df_3)
