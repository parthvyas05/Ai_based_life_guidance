def boost_health_guidance(guidance, stress_level):
    if stress_level != "High":
        return guidance

    for g in guidance:
        if g["category"] == "health":
            g["priority"] = min(5, g["priority"] + 1)

    return sorted(guidance, key=lambda x: -x["priority"])


def run_full_pipeline(
    user_id,
    users_df,
    events_df,
    guidance_df,
    stress_model
):
   
    # USER PROFILE
     
    user_row = users_df[users_df["user_id"] == user_id]
    if user_row.empty:
        return None

    user_row = user_row.iloc[0]
 
    # USER EVENTS
 
    user_events = events_df[events_df["user_id"] == user_id]

 
    # RULE ENGINE
    
    archetypes = set()
    guidance = []

    for _, rule in guidance_df.iterrows():
        condition_type = rule["condition_type"]
        condition_value = rule["condition_value"]

        match = False

        if condition_type in user_row and str(user_row[condition_type]) == str(condition_value):
            match = True

        if condition_type == "event_type" and condition_value in user_events["event_type"].values:
            match = True

        if match:
            archetypes.add(rule["archetype"])
            guidance.append({
                "rule_id": rule["rule_id"],
                "category": rule["recommended_category"],
                "priority": int(rule["priority"]),
                "message": rule["template_message"]
            })

  
    # STRESS PREDICTION
 
    from src.feature_engineering import build_user_stress_features

    stress_features = build_user_stress_features(events_df)
    user_stress = stress_features[stress_features["user_id"] == user_id]

    if user_stress.empty:
        stress_score = 0.0
        stress_level = "Low"
    else:
        X = user_stress[[
            "total_events",
            "avg_severity",
            "max_severity",
            "recent_events"
        ]]
        stress_score = stress_model.predict_proba(X)[0][1]

        if stress_score >= 0.6:
            stress_level = "High"
        elif stress_score >= 0.3:
            stress_level = "Medium"
        else:
            stress_level = "Low"
 
    # PERSONALIZATION
    
    guidance = boost_health_guidance(guidance, stress_level)

    return {
        "user_id": int(user_id),
        "stress_score": round(float(stress_score), 4),
        "stress_level": stress_level,
        "archetypes": list(archetypes),
        "guidance": guidance
    }
