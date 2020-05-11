# Python Peewee-ORM
# ORM concept with Sqlite database


# What is ORM?
--> Object Relational Mapping(ORM) is a technique for storing, retrieving, updating and deleting from an object-orinted program in relational database

1. Create a virtual Environment and install dependencies from requirements.txt file, Download DB Browser(SQLite) software to view our table structure

2. Once Python file created then type below command in python interpreter to create a database tables and columns which mentioned in the the .py file,  In thta file I have declared the classes for table name, columns structure and inherited OOPS concept.

3. Type this command in Python interpreter - import <py file name>(don't mention .py extension) e.g >>> import orm_practice
 
4. Then type >>> orm_practice.db.connect() # It will show True as a output response so we are successfully created database and connected to that.

5. Then type >>> orm_practice.Store # This Store is available in database model which we have defined by using class keyword in orm_practice.py file 

6. Then type >>> from orm_practice import *

7. And then >>> db.create_tables([Store, Warehouse, Product ]) # This command will create tables in our database with mentioned columns nane
