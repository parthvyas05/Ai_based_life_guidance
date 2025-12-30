import json
from src.model_pipeline import run_full_pipeline


def run_for_all_users(
    users_df,
    events_df,
    guidance_df,
    stress_model,
    output_path="final_output.json"
):
    outputs = []

    for uid in users_df["user_id"].unique():
        result = run_full_pipeline(
            uid,
            users_df,
            events_df,
            guidance_df,
            stress_model
        )
        if result:
            outputs.append(result)

    with open(output_path, "w") as f:
        json.dump(outputs, f, indent=2)

    return outputs
