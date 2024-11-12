import pandas as pd

data1={
    'Store':['Store1','Store2','Store3','Store1'],
    'Region':['East','West','West','West'],
    'Sales':[100,200,300,400]
}


df1=pd.DataFrame(data1)
print(df1)

df2 = df1.groupby(['Region'])
print(df2)