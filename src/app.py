import argparse
import joblib

from src.data_loader import load_users, load_events, load_guidance_rules
from src.model_pipeline import run_full_pipeline


def main(user_id):
    users = load_users()
    events = load_events()
    rules = load_guidance_rules()
    model = joblib.load("src/stress_model.pkl")

    result = run_full_pipeline(
        user_id=user_id,
        users_df=users,
        events_df=events,
        guidance_df=rules,
        stress_model=model
    )

    if result is None:
        print("User not found")
    else:
        print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--user_id", type=int, required=True)
    args = parser.parse_args()

    main(args.user_id)
