import pandas as pd


def build_user_stress_features(events_df):
    """
    Aggregates event data per user
    """
    user_features = (
        events_df
        .groupby("user_id")
        .agg(
            total_events=("event_id", "count"),
            avg_severity=("severity_score", "mean"),
            max_severity=("severity_score", "max"),
            recent_events=("event_recency_days", lambda x: (x <= 7).sum())
        )
        .reset_index()
    )

    user_features.fillna(0, inplace=True)
    return user_features
