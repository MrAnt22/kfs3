from database.models import WeatherData

def insert_data_to_db(df, db_session):
    for _, row in df.iterrows():
        record = WeatherData(
            datetime=row['datetime'],
            location=row['location'],
            temperature=row['temperature'],
            humidity=row['humidity'],
            wind_speed=row['wind_speed'],
            air_quality_index=row['air_quality_index'],
        )
        db_session.add(record)
    db_session.commit()