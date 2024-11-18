import sqlite3

connection = sqlite3.connect("Chinook_Sqlite.sqlite")
curr = connection.cursor()

#SQL Crud operations
#Insert new customer
NewCustomer = (1000,'Sangeeth Sudhakaran','RR','ABC','Sangeeth@ust.com','IND')

curr.execute(
    """
    insert into customer(CustomerId,FirstName,LastName,Company,Email,Country)
    values(?,?,?,?,?,?)
    """,NewCustomer)
connection.commit()
print("New customer added successfully")

#Update existing customer
CustomerId=1000
UpdatedEmail='updated@ust.com'
curr.execute(
    """
    update customer set Email = ?
    where CustomerId = ?
    """,(UpdatedEmail, CustomerId))
connection.commit()
print("Customer updated")

#Delete customer
#curr.execute("delete from customer where CustomerId = 1000"#)
#connection.commit(#)
#print("Customer del#eted")

#Print new customer/Updated customer
curr.execute("select * from customer where CustomerId = 1000")
data = curr.fetchall()

for row in data:
    print(data)