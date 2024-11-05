import pandas as pd

Runs={ 
       'TCS': {'Qtr1':2100,'Qtr2':2000,'Qtr3':4000,'Qtr4':2000},
       'WIPRO': {'Qtr1':3000,'Qtr2':2400,'Qtr3':3000,'Qtr4':2500},
       'L&T': {'Qtr1':2000,'Qtr2':3000,'Qtr3':35000,'Qtr4':7000}      
      }

df=pd.DataFrame(Runs)
print(df)
print(df.loc['Qtr3',:])

print("-------------------")
print(df.loc['Qtr1':'Qtr3',:])