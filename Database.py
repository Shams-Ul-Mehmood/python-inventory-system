import sqlite3

def create_Inventory_Management_System_Database():
    database_Connection = sqlite3.connect(database=r"Inventory_Management_System_Database.db")
    query_Cursor = database_Connection.cursor()
    query_Cursor.execute("create table if not exists Employee( employee_id Integer primary key autoincrement , employee_name text , employee_gender text , employee_age integer , employee_address text , employee_dob text , employee_contact text , employee_email text , employee_password text , employee_user_type text , employee_salary text , employee_attendence text , employee_doj text , employee_experience text )")
    database_Connection.commit()

    query_Cursor.execute("create table if not exists Supplier( supplier_invoice_id Integer primary key autoincrement , supplier_name text , supplier_description text , supplier_contact text )")
    database_Connection.commit()

    query_Cursor.execute("create table if not exists Category( category_id Integer primary key autoincrement , category_name text )")
    database_Connection.commit()

    query_Cursor.execute("create table if not exists Product( product_id Integer primary key autoincrement , category text , supplier text , name text , price integer , quantity integer , status text )")
    database_Connection.commit()


create_Inventory_Management_System_Database()