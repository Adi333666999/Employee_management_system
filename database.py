import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor, conn
    try:
        conn = pymysql.connect(host='localhost',user='root',password='root')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error','Something went wrong')
        return

    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (Id VARCHAR(10), Name VARCHAR(50), Phone VARCHAR(15), Role VARCHAR(50), Gender VARCHAR(20), Salary DECIMAL(10, 2))')

def insert(id,name,phone,role,gender,salary):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)', (id,name,phone,role,gender,salary))
    conn.commit()

def id_exists(id):
    try:
        mycursor.execute('SELECT COUNT(*) FROM data WHERE Id=%s', (id,))
        result = mycursor.fetchone()
        return result[0] > 0  # Returns True if ID exists, False otherwise
    except Exception as e:
        messagebox.showerror('Error', f'Error checking ID existence: {e}')
        return False


def fetch_employees():
    try:
        mycursor.execute('SELECT * FROM data')  # Fetch all data from the 'data' table
        result = mycursor.fetchall()  # Get all rows
        return result  # Return the data fetched
    except Exception as e:
        messagebox.showerror('Error', f'Error fetching data: {e}')
        return []

def update(id, name, phone, role, gender, salary):
    try:
        mycursor.execute('UPDATE data SET Name=%s, Phone=%s, Role=%s, Gender=%s, Salary=%s WHERE Id=%s',
                         (name, phone, role, gender, salary, id))
        conn.commit()  # Commit the changes to the database
    except Exception as e:
        messagebox.showerror('Error', f'Error updating data: {e}')

def delete(id):
    mycursor.execute('DELETE FROM data WHERE id=%s', id)
    conn.commit()

def search(option, value):
    mycursor.execute(f'SELECT * FROM data WHERE {option}=%s', value)
    result=mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()



connect_database()
