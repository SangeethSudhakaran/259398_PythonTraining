import pandas as pd

data = {
    'Name': ['Sangeeth','Sam','Joseph'],
    'Age' : [31,28,32],
    'Country' : ['India','USA','UK']
}

df = pd.DataFrame(data)

for row_index, row_value in df.iterrows():
    print("Row index is : ", row_index)
    print("Row value is : ", row_value)

    print("-------------------------------")

for col_name,col_value in df.iteritems():
    print("Column name is : ", col_name)
    print("Column value is : ", col_value)