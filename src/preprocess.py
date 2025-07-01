import pandas as pd

def preprocess_fire_data(df):
    """Clean and preprocess fire data."""
    # Convert acq_date and acq_time to datetime
    df['datetime'] = pd.to_datetime(df['acq_date'] + ' ' + df['acq_time'].astype(str).str.zfill(4),
                                    format='%Y-%m-%d %H%M')
    # Drop duplicates, handle missing values if any
    df = df.drop_duplicates()
    df = df.dropna(subset=['latitude', 'longitude', 'datetime'])
    return df

def merge_with_weather_vegetation(fire_df, weather_df=None, vegetation_df=None, district_code=None):
    """
    Merge fire data with weather and vegetation/LULC data.
    For demo, weather_df is joined on index (sampled rows only).
    Args:
        fire_df (pd.DataFrame): Fire data
        weather_df (pd.DataFrame): Weather data (optional)
        vegetation_df (pd.DataFrame): LULC data from Bhuvan (optional)
        district_code (str): District code for merging (optional)
    Returns:
        pd.DataFrame: Merged DataFrame
    """
    merged = fire_df.copy()
    if weather_df is not None:
        # For demo: join on index (assumes weather_df is a sample of fire_df)
        for col in ['temp', 'humidity', 'wind_speed', 'wind_deg', 'weather_main', 'weather_desc']:
            if col in weather_df.columns:
                merged.loc[weather_df.index, col] = weather_df[col]
    if vegetation_df is not None:
        if 'LULC_CLASS' in vegetation_df.columns and 'AREA' in vegetation_df.columns:
            dominant_class = vegetation_df.sort_values('AREA', ascending=False).iloc[0]['LULC_CLASS']
            merged['dominant_LULC'] = dominant_class
    return merged

if __name__ == "__main__":
    from data_ingest import load_fire_data, fetch_vegetation_data_bhuvan, fetch_weather_for_fire_df
    fire_csv = "../data/fire_nrt_J1V-C2_631066.csv"
    fire_df = load_fire_data(fire_csv)
    fire_df = preprocess_fire_data(fire_df)
    # Example usage for weather and Bhuvan API (uncomment and fill in your details):
    # weather_api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    # weather_df = fetch_weather_for_fire_df(weather_api_key, fire_df, sample_size=5)
    # bhuvan_api_key = "YOUR_BHUVAN_API_KEY"
    # district_code = "YOUR_DISTRICT_CODE"
    # year = "2018"
    # lulc_df = fetch_vegetation_data_bhuvan(bhuvan_api_key, district_code, year)
    # merged_df = merge_with_weather_vegetation(fire_df, weather_df=weather_df, vegetation_df=lulc_df, district_code=district_code)
    # print(merged_df.head())
    print(fire_df.head()) 