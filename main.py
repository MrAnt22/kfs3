import pandas as pd
from processing.data_cleaning import load_and_clean_data
from processing.insert_data import insert_data_to_db
from processing.feature_engineering import engineer_features
from processing.air_quality_report import generate_air_quality_report
from database.db import engine, get_db
from database.models import Base
from visualization.plots import plot_air_quality, plot_weather_trends, plot_air_quality_for_allergies

def main():
    filepath = 'data/weather_data.csv'
    df = load_and_clean_data(filepath)

    Base.metadata.create_all(bind=engine)

    db = next(get_db())
    insert_data_to_db(df, db)

    plot_air_quality(df)
    plot_weather_trends(df)

    df = engineer_features(df)

    generate_air_quality_report('2025-02-12', 7, 'Kyiv')
    plot_air_quality_for_allergies(df)

if __name__ == "__main__":
    main()
