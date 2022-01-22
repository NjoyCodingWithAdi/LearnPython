# difference between conct and merge
import pandas as pd

df1 = pd.DataFrame({
'A':[1,2,3,4],
'B':[True,False,True,True],
'C':['C1','C2','C3','C4']
})
df2 = pd.DataFrame({
'A':[5,7,8,5],
'B':[False,False,True,False],
'C':['C1','C3','C5','C8']
})

print(df1)
print(df2)

# conct = is straight forward operation

df3 = pd.concat([df1,df2], axis = 1)
print(df3)

# Let's get the data which are common in C columns df1 df2

df4 = pd.merge(df1,df2,how='inner', on='C')
print(df4)

df5 = pd.merge(df1,df2,how='outer', on='C')
print(df5)