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

# left and right in merge 

df3 = df1.merge(df2, on='C', how='left')
df4 = df1.merge(df2, on='C', how='right')

print(df3)
print(df4)