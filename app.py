import streamlit as st
import pandas as pd
import pickle

# ---------------- LOAD MODEL ----------------

model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# ---------------- TITLE ----------------

st.title("🎓 Student Performance Predictor")


st.divider()

# ---------------- USER INPUTS ----------------

Hours_Studied = st.number_input(
    "Hours Studied",
    min_value=0,
    max_value=40,
    value=10
)

Attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

Previous_Scores = st.number_input(
    "Previous Scores",
    min_value=0,
    max_value=100,
    value=70
)

Tutoring_Sessions = st.number_input(
    "Tutoring Sessions",
    min_value=0,
    max_value=10,
    value=2
)

Sleep_Hours = st.number_input(
    "Sleep Hours",
    min_value=1,
    max_value=12,
    value=7
)

Access_to_Resources = st.selectbox(
    "Access to Resources",
    ["Low", "Medium", "High"]
)

Motivation_Level = st.selectbox(
    "Motivation Level",
    ["Low", "Medium", "High"]
)

Parental_Involvement = st.selectbox(
    "Parental Involvement",
    ["Low", "Medium", "High"]
)

# ---------------- PREDICT ----------------

if st.button("Predict Performance"):

    # Hidden Default Features
    Physical_Activity = 3
    Teacher_Quality = "Medium"
    Internet_Access = "Yes"
    Family_Income = "Medium"
    School_Type = "Public"
    Peer_Influence = "Neutral"
    Parental_Education_Level = "College"
    Distance_from_Home = "Moderate"
    Gender = "Female"

    # ---------------- FEATURE ENGINEERING ----------------

    Study_Efficiency = (
        Hours_Studied /
        (Sleep_Hours + 1)
    )

    Academic_Consistency = (
        Attendance *
        Previous_Scores
    )

    Study_Commitment = (
        Hours_Studied *
        Attendance
    )

    # ---------------- INPUT DATA ----------------

    input_dict = {
        "Hours_Studied": Hours_Studied,
        "Attendance": Attendance,
        "Previous_Scores": Previous_Scores,
        "Tutoring_Sessions": Tutoring_Sessions,
        "Sleep_Hours": Sleep_Hours,
        "Physical_Activity": Physical_Activity,

        "Study_Efficiency": Study_Efficiency,
        "Academic_Consistency": Academic_Consistency,
        "Study_Commitment": Study_Commitment,

        "Access_to_Resources": Access_to_Resources,
        "Motivation_Level": Motivation_Level,
        "Teacher_Quality": Teacher_Quality,
        "Parental_Involvement": Parental_Involvement,

        "Internet_Access": Internet_Access,
        "Family_Income": Family_Income,
        "School_Type": School_Type,
        "Peer_Influence": Peer_Influence,
        "Parental_Education_Level": Parental_Education_Level,
        "Distance_from_Home": Distance_from_Home,
        "Gender": Gender
    }

    input_df = pd.DataFrame([input_dict])

    # ---------------- ENCODING ----------------

    input_df = pd.get_dummies(
        input_df,
        dtype=int
    )

    input_df = input_df.reindex(
        columns=columns,
        fill_value=0
    )

    # ---------------- PREDICTION ----------------

    # ---------------- PREDICTION ----------------

    prediction = model.predict(input_df)[0]

    prediction =round(prediction, 2)

    # ---------------- OUTPUT ----------------

    st.divider()

    st.subheader("Prediction Result")

    st.metric(
        label="Predicted Exam Score",
        value=f"{prediction}"
    )

    if prediction >= 85:
        st.success("Performance Level: Excellent 🌟")

    elif prediction >= 70:
        st.success("Performance Level: Good 👍")

    elif prediction >= 60:
        st.info("Performance Level: Average 📚")

    elif prediction >= 40:
        st.warning("Performance Level: Below Average ⚠️")

    else:
        st.error("Performance Level: Poor ❌")

    

    # Accuracy
    st.info(
        "Model Accuracy (R²): 71.2%"
    )