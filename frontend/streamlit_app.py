import streamlit as st
import pandas as pd
import joblib
import json

# ------------------------------
# Load assets (cached)
# ------------------------------
@st.cache_data
def load_data():
    users = pd.read_csv("data/users_clean.csv")
    events = pd.read_csv("data/events_clean.csv")
    rules = pd.read_csv("data/guidance_rules_clean.csv")
    return users, events, rules


@st.cache_resource
def load_model():
    return joblib.load("src/stress_model.pkl")


# ------------------------------
# Import your pipeline
# ------------------------------
from src.model_pipeline import run_full_pipeline


# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="AI Life Guidance Engine", layout="centered")

st.title("🧠 AI Life Guidance Engine")
st.write("Personalized life guidance based on profile, events & stress")

user_id = st.number_input("Enter User ID", min_value=1, step=1)

if st.button("Generate Guidance"):

    users_df, events_df, rules_df = load_data()
    model = load_model()

    output = run_full_pipeline(
        user_id=user_id,
        users_df=users_df,
        events_df=events_df,
        guidance_df=rules_df,
        stress_model=model
    )

    if output is None:
        st.error("User ID not found")
    else:
        st.success("Guidance generated successfully!")

        st.subheader("Stress Overview")
        st.metric("Stress Score", round(output["stress_score"], 2))
        st.write("Stress Level:", output["stress_level"])

        st.subheader("Life Archetypes")
        st.write(", ".join(output["archetypes"]))

        st.subheader("Guidance")
        for g in output["guidance"]:
            st.markdown(
                f"""
                **{g['category'].upper()}**  
                Priority: {g['priority']}  
                {g['message']}
                """
            )

        st.subheader("Raw JSON")
        st.json(output)
