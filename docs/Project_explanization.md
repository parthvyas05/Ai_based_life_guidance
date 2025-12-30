# Personalized Stress-Aware Guidance System – Results & Pipeline Explanation

## 1. Project Overview

This project builds an end-to-end **personalized user guidance system** that combines:
- Rule-based decision logic
- A machine learning stress prediction model
- Re-ranking of guidance based on predicted stress

The system takes user behavior data and produces **frontend-ready structured guidance** for each user.



## 2. Data Used

We work with **synthetic but structured datasets**:

### 2.1 Events Data
- User activity events
- Includes severity, recency, and event types
- Used to engineer stress-related features

### 2.2 Guidance Rules Data
- Rule-based guidance templates
- Includes:
  - `rule_id`
  - `category`
  - `priority`
  - `message`
  - Matching conditions (archetype, event type, etc.)

### 2.3 Final Clean Guidance CSV
A denormalized dataset containing:
- `user_id`
- `stress_score`
- `stress_level`
- `archetypes`
- `rule_id`
- `category`
- `priority`
- `message`

This CSV represents the **final rule-engine output before ML personalization**.



## 3. Notebook Pipeline

### Notebook 01 – Data Exploration & Cleaning
- Load raw users, events, and guidance rules
- Clean columns and standardize formats
- Remove nulls and invalid records
- Save clean CSV files


### Notebook 02 – Rule-Based Guidance Engine
- Apply guidance rules per user
- Match based on:
  - User archetype
  - Event types
  - Profile attributes
- Generate structured guidance JSON per user
- Output is deterministic and explainable



### Notebook 03 – Stress Feature Engineering
- Aggregate events per user
- Create stress-related features:
  - `total_events`
  - `avg_severity`
  - `max_severity`
  - `recent_events`
- Derive `stress_score`
- Map score → `Low / Medium / High`



### Notebook 04 – Machine Learning Model
**Goal:** Add ML personalization

Steps:
1. Use engineered stress features
2. Create label:
   - `high_stress = 1` if stress_level == "High"
3. Train a simple classifier (Logistic Regression / RandomForest)
4. Evaluate performance (accuracy, precision, recall)
5. Save trained model as:



This model predicts whether a user is under **high stress**.

---

### Notebook 05 – Inference & Personalization
This notebook demonstrates **end-to-end inference**.

Steps:
- Load trained ML model (`.pkl`)
- Accept a `user_id`
- Predict stress probability
- Boost health-related guidance priority for high-stress users
- Output final JSON

Example output:
```json
{
"user_id": 5,
"stress_score": 0.87,
"stress_level": "High",
"archetypes": ["Growth_Leader"],
"guidance": [
 {
   "category": "health",
   "priority": 5,
   "message": "High work pressure detected. Prioritize rest and recovery."
 }
]
}

# CLI Pipeline

A command-line interface is provided for easy inference.

Command for run 
python src/app.py --user_id 5

# 
