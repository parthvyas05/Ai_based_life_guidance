import pandas as pd


def load_users(path="data/users_clean.csv"):
    return pd.read_csv(path)


def load_events(path="data/events_clean_final.csv"):
    return pd.read_csv(path)


def load_guidance_rules(path="data/guidance_rules_clean.csv"):
    return pd.read_csv(path)
