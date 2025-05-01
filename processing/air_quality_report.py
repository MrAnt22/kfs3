import pandas as pd
from datetime import datetime, timedelta
from processing.data_cleaning import load_and_clean_data
from processing.feature_engineering import engineer_features
from visualization.plots import plot_air_quality_for_allergies

def generate_air_quality_report(start_date_str: str, days: int, location: str):
    df = load_and_clean_data("data/weather_data.csv")
    df = engineer_features(df)

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = start_date + timedelta(days=days)

    filtered_df = df[
        (df['datetime'] >= start_date) &
        (df['datetime'] < end_date) &
        (df['location'] == location)
    ]

    if filtered_df.empty:
        print(f"There's no data for {location} in period {start_date_str} + {days} days.")
    else:
        plot_air_quality_for_allergies(filtered_df)
