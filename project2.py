import streamlit as st
import pandas as pd

st.title("Student Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Add Student", "View Students"]
)

if menu == "Add Student":

    st.subheader("Add Student")

    student_id = st.text_input("Student ID")
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1)
    course = st.text_input("Course")

    if st.button("Add Student"):

        new_data = {
            "ID": student_id,
            "Name": name,
            "Age": age,
            "Course": course
        }

        df = pd.read_csv("students.csv")

        df = pd.concat(
            [df, pd.DataFrame([new_data])],
            ignore_index=True
        )

        df.to_csv("students.csv", index=False)

        st.success("Student Added Successfully!")

elif menu == "View Students":

    st.subheader("Student Records")

    df = pd.read_csv("students.csv")

    st.dataframe(df)