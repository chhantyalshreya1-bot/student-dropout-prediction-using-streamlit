import streamlit as st
import pandas as pd
import pickle 

with open('model.pkl', 'rb') as file:
    model= pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler=pickle.load(file)

with open('feature_columns.pkl', 'rb') as file:
    features_columns=pickle.load(file)



st.title("Student Dropout Predication")
st.write("Enter the student's information to predict the dropout status.")

age= st.number_input(
    "Age",
    min_value=15,
    max_value=40,
    value=21
)

family_income = st.number_input(
    "Family Income",
    min_value=0.0,
    value=50000.0
)

study_hour =st.number_input(
    "Study Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=4.0
)


attendance=st.number_input(
    "Attendance Rate(%)",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

travel_time=st.number_input(
    "Travel Time(Minutes)",
    min_value=0.0,
    value=30.0
)


stress_index=st.number_input(
    "Stress Index",
    min_value=0.0,
    value=5.0
)

gpa=st.number_input(
    "GPA",
    min_value=0.0,
    max_value=4.0,
    value=2.5
)

semester_gap=st.number_input(
    "Semester GPA",
    min_value=0.0,
    max_value=4.0,
    value=2.5
)

cgpa=st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=4.0,
    value=2.5
)
# categorical inputs

parental_education=st.selectbox(
    "Parental Education",
    ["High School", "Bachelor", "Master", "PhD"]

)

gender=st.selectbox(
    "Gender",
    ['Female', 'Male']
)

internet_access=st.selectbox(
    "Internet Access",
    ["No","Yes"]
)

part_time_job = st.selectbox(
    "Part-Time Job",
    ["No", "Yes"]
)

scholarship = st.selectbox(
    "Scholarship",
    ["No", "Yes"]
)

semester = st.selectbox(
    "Semester",
    ["Year 1", "Year 2", "Year 3", "Year 4"]
)

department = st.selectbox(
    "Department",
    ["Arts", "Business", "CS", "Engineering", "Science"]
)


assignment_delay = st.number_input(
    "Assignment Delay Days",
    min_value=0,
    value=2
)

predict_button=st.button("Predict Dropout")

if predict_button:

    education_mapping = {
        "High School": 0,
        "Bachelor": 1,
        "Master": 2,
        "PhD": 3
    }

    parental_education_encoded = education_mapping[parental_education]

    gender_male = 1 if gender == 'Male' else 0
    internet_yes = 1 if internet_access == 'Yes' else 0
    part_time_yes = 1 if part_time_job == 'Yes' else 0
    scholarship_yes = 1 if scholarship == 'Yes' else 0

    semester_year_2 = 1 if semester == 'Year 2' else 0
    semester_year_3 = 1 if semester == 'Year 3' else 0
    semester_year_4 = 1 if semester == 'Year 4' else 0

    department_business = 1 if department == "Business" else 0
    department_cs = 1 if department == "CS" else 0
    department_engineering = 1 if department == "Engineering" else 0
    department_science = 1 if department == "Science" else 0










    input_data = pd.DataFrame([{
        'Age': age,
        'Family_Income': family_income,
        'Study_Hours_per_Day': study_hour,
        'Attendance_Rate': attendance,
        'Assignment_Delay_Days': assignment_delay,
        'Travel_Time_Minutes': travel_time,
        'Stress_Index': stress_index,
        'GPA': gpa,
        'Semester_GPA': semester_gap,
        'CGPA': cgpa,
        'Parental_Education': parental_education_encoded,
        'Gender_Male': gender_male,
        'Internet_Access_Yes': internet_yes,
        'Part_Time_Job_Yes': part_time_yes,
        'Scholarship_Yes': scholarship_yes,
        'Semester_Year 2': semester_year_2,
        'Semester_Year 3': semester_year_3,
        'Semester_Year 4': semester_year_4,
        'Department_Business': department_business,
        'Department_CS': department_cs,
        'Department_Engineering': department_engineering,
        'Department_Science': department_science
    }])



    input_data = input_data[features_columns]
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)

    dropout_probability = probability[0][1]

    st.write(f"Dropout Probability: {dropout_probability:.2%}")




    if prediction[0] == 1:
        st.error(" Student is likely to drop out.")
    else:
        st.success(" Student is likely to stay enrolled.")








