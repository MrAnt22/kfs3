import pandas as pd

def add_season_column(df: pd.DataFrame) -> pd.DataFrame:
    def get_season(month):
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Autumn'
    
    df['season'] = df['datetime'].dt.month.apply(get_season)
    return df

def add_air_quality_category(df: pd.DataFrame) -> pd.DataFrame:
    def categorize(aqi):
        if aqi <= 50:
            return 'Good'
        elif aqi <= 100:
            return 'Moderate'
        elif aqi <= 150:
            return 'Unhealthy for Sensitive Groups'
        elif aqi <= 200:
            return 'Unhealthy'
        elif aqi <= 300:
            return 'Very Unhealthy'
        else:
            return 'Hazardous'
    
    df['air_quality_category'] = df['air_quality_index'].apply(categorize)
    return df

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    if 'datetime' not in df.columns or 'air_quality_index' not in df.columns:
        df = df.rename(columns={'date': 'datetime'})
        df = df.rename(columns={'predicted_air_quality_index': 'air_quality_index'})
    df = add_season_column(df)
    df = add_air_quality_category(df)
    return df
