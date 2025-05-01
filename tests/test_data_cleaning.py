import pandas as pd
from processing.data_cleaning import load_and_clean_data

def test_load_and_clean_data():
    df = load_and_clean_data("data/weather_data.csv")
    
    assert not df.isnull().values.any(), "У датафреймі не повинно бути пропущених значень"
    assert "datetime" in df.columns
    assert "temperature" in df.columns
    assert isinstance(df['datetime'].iloc[0], pd.Timestamp)
