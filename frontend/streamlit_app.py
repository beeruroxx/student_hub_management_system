import streamlit as st
import requests

API_URL = "http://localhost:5000"

st.title("📚 StudentHub – Student Dashboard")

# -------------------------
# LOAD STUDENTS
# -------------------------
def load_students():
    try:
        res = requests.get(f"{API_URL}/students")
        return res.json()
    except:
        st.error("Backend not reachable!")
        return []

students = load_students()

# -------------------------
# SHOW STUDENTS TABLE
# -------------------------
st.subheader("All Students")

if not students:
    st.info("No students found")
else:
    for student in students:
        with st.expander(f"{student['name']} ({student['course']} - Year {student['year']})"):
            
            st.write("### Subjects")

            # Convert subjects list to rows
            subject_data = {
                "Subject": [sub["name"] for sub in student["subjects"]],
                "Marks": [sub["marks"] for sub in student["subjects"]],
                "Attendance (%)": [sub["attendance"] for sub in student["subjects"]],
            }

            st.table(subject_data)



st.subheader("➕ Add New Student")

with st.form("add_student_form"):
    name = st.text_input("Student Name")
    course = st.text_input("Course (e.g., BCA, BSc)")
    year = st.number_input("Year", min_value=1, max_value=5, step=1)

    st.write("### Subjects")
    subject_count = st.number_input("How many subjects?", min_value=1, max_value=10, step=1)

    subjects = []
    for i in range(subject_count):
        st.write(f"#### Subject {i+1}")
        sub_name = st.text_input(f"Subject Name {i+1}", key=f"sub_name_{i}")
        marks = st.number_input(f"Marks {i+1}", key=f"marks_{i}", min_value=0, max_value=100)
        attendance = st.number_input(f"Attendance % {i+1}", key=f"att_{i}", min_value=0, max_value=100)
        subjects.append({
            "name": sub_name,
            "marks": marks,
            "attendance": attendance
        })

    submitted = st.form_submit_button("Add Student")

    if submitted:
        payload = {
            "name": name,
            "course": course,
            "year": year,
            "subjects": subjects
        }

        res = requests.post(f"{API_URL}/students", json=payload)

        if res.status_code == 200:
            st.success("Student added successfully!")
        else:
            st.error("Failed to add student")

