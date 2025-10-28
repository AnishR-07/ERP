import pandas as pd
import streamlit as st
from db import create_table , add_student, view_student, update_student, delete_student, insert_data

st.set_page_config(page_title="Modern Public Schhool,Sec-37, Faridabad", layout= "centered")

USER_CREDENTIALS = {"adm":"123@Adm" , "teacher":"123@Teacher"}

def login():
    st.title("Modern Public Schhool,Sec-37, Faridabad")
    st.subheader("Enter the registered User ID and Password with school")

    username = st.text_input("User ID")
    password = st.text_input("Password", type= "password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["Logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Welcome {username}")
            st.rerun()
        else:
            st.error("Invalid Credentials")


def student_info():
    st.set_page_config(page_title="Student information")

    create_table() 

    st.title ("Modern Public Schhool,Sec-37, Faridabad")

    if st.sidebar.button ("Logout"):
        st.session_state["Logged_in"] = False
        st.rerun()

    Student_Information = ["-","STUDENT MASTER", "UPDATE STUDENT", "DELETE STUDENT","STUDENT REPORT"]
    choice = st.sidebar.selectbox('Student_Information', Student_Information)


    if choice == "STUDENT MASTER":
        st.subheader("Enter the details")
        Admission_no = st.number_input("Enter the Admission no")
        Student_name = st.text_input("Enter the Student name")
        Class = st.text_input("Enter the class")
        Section = st.text_input("Enter the section")
        Age = st.number_input("Enter the age")
        contact_number = st.number_input("Enter the contact no")


        file = st.file_uploader("Choose your file", type=["csv", "xlsx", "txt"])

            
        if st.button("save"):
            add_student(Admission_no, Student_name ,Class ,Section ,Age ,contact_number)
            st.success((f"{Student_name} saved successfully"))
            if file is not None:
                st.write("Preview")
                df = pd.read_excel(file)
                st.dataframe(df)
                insert_data(file)

    elif choice == "STUDENT REPORT":
        st.subheader("Students Details")
        details = view_student()

        if details:
            st.table(details)

        else:
            st.info("No record found")

    elif choice == "UPDATE STUDENT":
        Students = view_student()
        Students_dict = {f"{s[0]} - {s[1]}" : s for s in Students}
        selected = st.selectbox("Select the student" ,list(Students_dict.keys()))
        student = Students_dict[selected]

        Student_name = st.text_input("Student_name", student[1])
        Class = st.text_input("Class",student[2])
        Section = st.text_input("Section", student[3])
        Age = st.number_input("Age", student[4])
        contact_number = st.number_input("contact_number", student[5])

        if st.button("Update"):
            update_student(student[0], Student_name ,Class ,Section ,Age ,contact_number)
            st.success("Upddated sucessfully")

    elif choice == "DELETE STUDENT":
        Students = view_student()
        Students_dict = {f"{s[0]} - {s[1]}" : s for s in Students}
        selected = st.selectbox("select the student", list(Students_dict.keys()))
        student = Students_dict[selected]

        if st.button("Delete"):
            delete_student(student[0])
            st.error(f"{student[1]} deleted successfully")

        else:
            st.write("No record found")

def main():
    if "Logged_in" not in st.session_state:
        st.session_state["Logged_in"] = False

    if st.session_state["Logged_in"]:
        student_info()

    else:
        login()


if __name__ == "__main__":
    main()