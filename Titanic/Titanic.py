import pandas as pd

df = pd.read_csv(r"D:\Training\259398_PythonTraining\Titanic\titanic.csv")
#print(df[['Age','Sex']].head(5))


#Length of the result set
print("All the records count is", len(df.index))

#print(df[df['Age']<25])
print("Age less than 25 is: ",len((df[df['Age']<25])))

#Get the average age
print("Average age is : ", (df['Age'].mean()))

#Get average fare filters are -  male , age<25
filteredDf = df[(df['Age'] < 25) & (df['Sex'] == 'male')]
print(filteredDf)
print("Average fare for men is : ", (filteredDf['Fare'].mean()))

#Write the result set back to new csv
filteredDf.to_csv("FilteredCSV.csv")

#Percentage of survived passengers
SurvivedDf = df[df['Survived']==1]
print(len(SurvivedDf.index)/len(df.index)*(100))