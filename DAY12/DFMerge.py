import pandas as pd

data1={
    'Name':['Sam','Sangeeth','Joseph','Arjun'],
    'Age':[8,55,20,30],
    'Birth Place':['TVM','BLR','CNN','TVM']
}


data2={
    'Name':['Sam','Sangeeth','Joseph'],
    'Work Experiance':[1,2,3],
    'Work Place':['TCR','COK','KIA']
}

df1=pd.DataFrame(data1)
print(df1)

df2=pd.DataFrame(data2)
print(df2)

df3 = pd.merge(df1,df2,on="Name", how="inner")
print(df3)

df3 = pd.merge(df1,df2,on="Name", how="left")
print(df3)

#df3.to_csv("MergedData.csv")

#df3["is_Even"] = (df3["Work Experiance"] % 2 == 0)
#print(df3)

def isEven(val):
    return val%2==0

df3["is_Even"] = df3["Work Experiance"].apply(isEven)
print(df3)