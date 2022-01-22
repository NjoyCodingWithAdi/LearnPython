# find the shape of the dataframe "Mall_Customers.csv"
# create a datagframe --> gender = male df1 
# create a data frame--> gender = female df2
# creare a datframe --> age >=18 df3 

# average fo annual income of male , female 
# how many count of male/female 

import pandas as pd

data = pd.read_csv('Mall_Customers.csv')

print("Shape of our data frame", data.shape)

print(data.head())

print("Missing values", data.isnull().sum())

df1= pd.DataFrame(data, columns=['Gender'])
print(df1[df1['Gender'] == 'Male'])

df2= pd.DataFrame(data, columns=['Gender'])
print(df2[df2['Gender'] == 'Female'])

df3= pd.DataFrame(data, columns=['Age'])
print(df3[df3['Age'] >= 18])

df4 = df1[df1['Gender'] == 'Male']
print("Male count", df4.size )

df5 = df2[df2['Gender'] == 'Female']
print("Female count", df5.size )

print(data['Gender'].value_counts())

# Function name - groupby

print(data.groupby(['Gender'])['Age'].mean())

print("Max Age :- ",data.groupby(['Gender'])['Age'].max())
print("Min Age :- ",data.groupby(['Gender'])['Age'].min())