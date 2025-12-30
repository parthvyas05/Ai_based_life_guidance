# AI Life Guidance Assignment

This repo contains a take home assignment for a 2 year experience AI and ML engineer.
The goal is to design a small life guidance system that mimics an astrology style engine without using any actual astrology data.

The system should:

* Ingest user profile data and life events from CSV files
* Build scoring or rule based logic that turns this data into "guidance" suggestions
* Experiment with at least one ML or ranking model to personalise suggestions
* Expose a simple CLI or notebook interface to generate guidance for a user
* Log basic evaluation metrics and examples

You are expected to spend about 10 to 12 hours across a week on this.


# Personalized Guidance Engine with Stress Prediction

This project builds an end-to-end personalized guidance system that combines:

Rule-based reasoning

Feature engineering from user guidance data

A lightweight ML model to predict user stress

Stress-aware re-ranking of guidance

CLI + API-ready inference pipeline

The system outputs frontend-ready structured JSON guidance for any user.

.
.
├── Clean_data/
│   ├── events_clean_final.csv
│   ├── guidance_clean.csv
│   ├── users_clean.csv
│
├── json/
│   ├── rule_engine_output.json
│   ├── rule_engine_with_stress.json
│   └── final_personalised_output.json
│
├── models/
│   └── stress_model.pkl
│
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   ├── 02_rule_engine.ipynb
│   ├── 03_stress_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   
│
├── frontend/
│   ├── streamlit_app.py
│   
│   
│
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── model_pipeline.py
│   ├── run_engine.py
│   └── evaluation.py
│
├── tests/
│   └── test_pipeline.py
│
├── requirements.txt
├── README.md
├── results.md
└── .gitignore



# System Overview

1️⃣ Rule-Based Guidance Engine

Assigns archetypes

Maps rules → guidance messages

Produces structured JSON per user

2️⃣ Stress Scoring

Stress score computed from user activity & guidance signals

Converted into categorical stress levels: Low / Medium / High

3️⃣ ML Component (Assignment Requirement)

Supervised classifier predicts High-Stress users

Model improves personalization by boosting health guidance for high-stress users

4️⃣ Inference Interface

CLI (python src/run_engine.py --user_id 12)

Notebook demo

Frontend-ready API design

# Notebooks Explanation (Step-by-Step)

📘 Notebook 01 — Data Preparation

File: notebooks/01_data_preparation.ipynb

What it does:

Loads raw CSV files

Cleans columns & datatypes

Prepares user, event, and guidance datasets

Run:

Open notebook → Run all cells top to bottom

📘 Notebook 02 — Rule Engine

File: notebooks/02_rule_engine.ipynb

What it does:

Applies rule logic to users

Assigns archetypes

Generates structured guidance JSON

Output:

final_rule_engine_output.json

📘 Notebook 03 — Stress Feature Engineering

File: notebooks/03_stress_feature_engineering.ipynb

What it does:

Computes stress score per user

Maps score → stress level

Adds stress fields into rule engine JSON

Flattens final JSON into a clean CSV

Output:

final_rule_engine_output_with_stress.json
guidance_clean.csv

📘 Notebook 04 — Model Training (ML Component)

File: notebooks/04_model_training.ipynb

What it does:

Uses guidance-level user features

Creates a high_stress label from stress_level

Trains a lightweight classifier

Evaluates accuracy

Saves trained model

Model Saved As:

models/stress_model.pkl
 
# CLI Inference (End-to-End)
Run for a single user:
python src/run_engine.py --user_id 12


Output:

{
  "user_id": 12,
  "predicted_stress": "High",
  "guidance": [
    {
      "rule_id": "R5",
      "category": "health",
      "priority": 5,
      "message": "..."
    }
  ]
}

# Frontend / API Usage
Start API:
uvicorn src.app:app --reload

Request:
GET /predict/12

Response:

Stress-aware

JSON-formatted

Frontend-ready

# Installation & Setup
1️⃣ Create environment
python -m venv venv
source venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

📦 Requirements

See requirements.txt
Includes:

pandas

numpy

scikit-learn

joblib

fastapi

uvicorn

✅ Assignment Checklist

✔ Rule-based engine
✔ Stress score computation
✔ ML model for personalization
✔ Evaluation
✔ Inference interface (CLI + Notebook)
✔ Frontend-ready output
✔ Clear documentation

https://drive.google.com/drive/folders/1JKLwgZtWQQ-8BTYMp03kExoaoyC9utOI?usp=drive_link

Notes for Reviewers

Model performance is intentionally simple (synthetic data)

Focus is on pipeline clarity, feature design, and integration

Entire system runs end-to-end with a single user ID
