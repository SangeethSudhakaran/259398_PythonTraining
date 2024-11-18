import sqlite3
import pandas as pd

connection = sqlite3.connect("Chinook_Sqlite.sqlite")
curr = connection.cursor()

#select query using pandas 
# query = """
# select * from customers limit 10
# """
# df_customers = pd.read_sql_query(query,connection)
# print(df_customers)
# connection.close()

#1. Determine the total sales for each country in invoice table
# query = """
# select BillingCountry,sum(Total) as TotalSales from Invoice GROUP BY BillingCountry LIMIT 10
# """
# df_invoice = pd.read_sql_query(query,connection)
# print(df_invoice)

# connection.close()

#2. Determine the total sales for each country in invoice table
query = """
select * FROM invoice
"""
df_invoice = pd.read_sql_query(query,connection)
#print(df_invoice)
#connection.close()
df_invoice.groupby("BillingCountry")['Total'].sum().reset_index()
df_invoice.to_sql('summary_sales_by_country',connection,if_exists='replace',index=False)
print(df_invoice)
