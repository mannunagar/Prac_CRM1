import mysql
import mysql.connector

used_database1 = mysql.connector.connect (
    host= 'localhost',
    user='root',
    passwd='Manish@1234'
) 

# creating a cursor object to run sql commands
cursor_object1 = used_database1.cursor()

#creating a database using cursor object
cursor_object1.execute("create database prac_crm1")

#comming the actual changes in databse schema
used_database1.commit()

print('MySql Database prac_crm1 created successfully!!! ')
