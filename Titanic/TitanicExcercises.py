import pandas as pd

df = pd.read_csv(r"D:\Training\259398_PythonTraining\Titanic\titanic.csv")

#compare the average age of passengers who survived those who didn't
df.fillna(0,inplace=True)

avg_age_survived = df[df['Survived']==1]['Age'].mean()
print(avg_age_survived)

avg_age_not_survived = df[df['Survived']==0]['Age'].mean()
print(avg_age_not_survived)

survived_by_age_df = df.groupby('Sex')['Survived'].mean()
print(survived_by_age_df)

df_familySize = df['FamilySize'] = df['SibSp'] + df['Parch']
print(df[['SibSp','Parch','FamilySize']])

family_survival_rate = df.groupby('FamilySize')['Survived'].mean()
df.merge(df,df_familySize,on="FamilySize")
print(df)