import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    df.rename(columns={
        'last_updated': 'datetime',
        'location_name': 'location',
        'temperature_celsius': 'temperature',
        'humidity': 'humidity',
        'wind_kph': 'wind_speed',
        'air_quality_PM2.5': 'air_quality_index'
    }, inplace=True)

    df['datetime'] = pd.to_datetime(df['datetime'])
    df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
    df['humidity'] = df['humidity'].fillna(df['humidity'].mean())
    df['wind_speed'] = df['wind_speed'].fillna(df['wind_speed'].mean())
    df['air_quality_index'] = df['air_quality_index'].fillna(df['air_quality_index'].mean())
    
    return df
