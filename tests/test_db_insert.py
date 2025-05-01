from sqlalchemy.orm import Session
from database.db import SessionLocal
from database.models import WeatherData
from processing.insert_data import insert_data_to_db
from processing.data_cleaning import load_and_clean_data

def test_insert_data():
    db: Session = SessionLocal()

    db.query(WeatherData).delete()
    db.commit()

    df = load_and_clean_data("data/weather_data.csv")
    insert_data_to_db(df, db)

    count = db.query(WeatherData).count()
    assert count > 0, "Дані не були додані у базу"
    
    db.close()