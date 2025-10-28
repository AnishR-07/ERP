import sqlite3
import pandas as pd

def create_table():
   con =sqlite3.connect("student.db")
   cursor = con.cursor()

   cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENTS (Admission_no integer primary key ,
                  Student_name TEXT,
                  Class TEXT,
                  Section TEXT,
                  Age integer,
                  contact_number integer
               )
   ''')

   con.commit()
   con.close()

def add_student(Admission_no, Student_name, Class, Section, Age, contact_number):
   con =sqlite3.connect("student.db")
   cursor = con.cursor()

   cursor.execute("INSERT INTO STUDENTS (Admission_no, Student_name, Class, Section, Age, contact_number) VALUES (?,?,?,?,?,?)", 
                  (Admission_no, Student_name, Class, Section, Age, contact_number))

   con.commit()
   con.close()

def view_student():
   con =sqlite3.connect("student.db")
   cursor = con.cursor()

   cursor.execute("SELECT * FROM STUDENTS")
   data = cursor.fetchall()

   con.commit()
   return data

def update_student(Student_name, Class,Section, Age, contact_number,Admission_no):
   con =sqlite3.connect("student.db")
   cursor = con.cursor()

   cursor.execute("UPDATE STUDENTS SET Student_name= ?, Class = ?,Section = ?, Age = ?, contact_number = ? WHERE Admission_no = ? ",
                  (Student_name, Class,Section, Age, contact_number, Admission_no ))
   
   con.commit()
   con.close()

def delete_student(Admission_no):
   con =sqlite3.connect("student.db")
   cursor = con.cursor()

   cursor.execute("DELETE FROM STUDENTS WHERE Admission_no = ? ",(Admission_no,))

   con.commit()
   con.close()

def insert_data(file_path):
   df = pd.read_excel(file_path)

   con =sqlite3.connect("student.db")
   cursor = con.cursor()

   for _, row in df.iterrows():
      cursor.execute("INSERT INTO STUDENTS (Student_name, Class, Section, Age, contact_number) VALUES (?,?,?,?,?)",
                     (row["Student_name"], row["Class"],row["Section"] ,row["Age"], row["contact_number"]))
      
   con.commit()
   con.close()