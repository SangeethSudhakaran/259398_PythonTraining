import pandas as pd

data1={
    'Name':['SS','AA','TT'],
    'Age':[8,55,20],
    'Place':['TVM','BLR','CNN']
}


data2={
    'Name':['JJJ','IIII','LLLL'],
    'Age':[86,155,720],
    'Place':['TCR','COK','KIA']
}

df1=pd.DataFrame(data1)
print(df1)

df2=pd.DataFrame(data2)
print(df2)

df3 = pd.concat([df1,df2],ignore_index=True)
print(df3)

