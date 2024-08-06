import sqlite3
# connect to the SQLite database
# I am trying to connect to a SQLite database, if this database doesnot exist, 
# database will be created with the name student
connection= sqlite3.connect("student_test.db")

# cursor object to create a table and insert records
cursor = connection.cursor()  # this method is responsible for traversing across the table to insert records

#create the table with a schema
table_info= """
Create table STUDENT_TEST(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25))
"""

# to create the table, we have to use the cursor object 
cursor.execute(table_info)

# to insert records, 
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Shree','Data_Engineering','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Alex','Data_Engineering','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Jayanth','Gen_AI','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Pavan','Gen_AI','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Nagaraj','Gen_AI','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Vikas','Gen_AI','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Ajay','Gen_AI','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Bobby','Gen_AI','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('John','Data Analytics','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Mary','Business Intelligence','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Williams','Database_Admin','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Kevin','Data Analytics','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Anderson','DevOps','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Ricky','Data Analytics','A')''')
cursor.execute('''INSERT INTO STUDENT_TEST VALUES('Dhoni','Database_Admin','A')''')

# show the inserted records
print("The inserted records are : ")

data_given = cursor.execute('''Select * from STUDENT_TEST''')
for i in data_given:
    print(i)

connection.commit()
connection.close()





                            


