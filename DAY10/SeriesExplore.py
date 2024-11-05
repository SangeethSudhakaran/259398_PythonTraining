import pandas as pd
student_dictionary={
    "Sangeeth":30,
    "Sam":60,
    "Joseph":10,
    "Arjun":60
}

students=pd.Series(student_dictionary)
print("Sum",sum(students))
print("Max",max(students))
print('loc:',students.loc["Sangeeth"])