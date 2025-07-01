import pandas as pd
import os
import requests
from datetime import datetime

def load_fire_data(csv_path):
    """Load satellite fire data from CSV."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"File not found: {csv_path}")
    df = pd.read_csv(csv_path)
    return df

# OpenWeatherMap API integration for weather data
def fetch_weather_data(api_key, lat, lon, date=None):
    """
    Fetch weather data for a given lat/lon (and optionally date) from OpenWeatherMap API.
    Args:
        api_key (str): OpenWeatherMap API key
        lat (float): Latitude
        lon (float): Longitude
        date (datetime, optional): Date for historical weather (not used in free tier)
    Returns:
        dict: Weather data (temp, humidity, wind, etc.)
    """
    # For demo, fetch current weather (historical requires paid plan)
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Weather API error: {response.status_code} {response.text}")
        return None
    data = response.json()
    weather = {
        'temp': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'wind_deg': data['wind'].get('deg', None),
        'weather_main': data['weather'][0]['main'],
        'weather_desc': data['weather'][0]['description']
    }
    return weather

def fetch_weather_for_fire_df(api_key, fire_df, sample_size=10):
    """
    Fetch weather data for a sample of fire events (for demo, to avoid API limits).
    Args:
        api_key (str): OpenWeatherMap API key
        fire_df (pd.DataFrame): Fire events
        sample_size (int): Number of events to fetch weather for
    Returns:
        pd.DataFrame: DataFrame with weather data for each event
    """
    records = []
    for idx, row in fire_df.head(sample_size).iterrows():
        lat, lon = row['latitude'], row['longitude']
        weather = fetch_weather_data(api_key, lat, lon)
        if weather:
            record = {**row.to_dict(), **weather}
            records.append(record)
    weather_df = pd.DataFrame(records)
    return weather_df

# Bhuvan LULC API integration for vegetation/LULC data
def fetch_vegetation_data_bhuvan(api_key, district_code, year):
    """
    Fetch vegetation/LULC data from Bhuvan LULC API.
    Args:
        api_key (str): Bhuvan API access token
        district_code (str): District code for the area of interest
        year (str): Year for LULC data (e.g., '2015', '2018')
    Returns:
        pd.DataFrame: DataFrame with LULC statistics
    """
    url = f"https://bhuvan-app1.nrsc.gov.in/api/thematic/lulc50kstat/{district_code}/{year}?key={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Bhuvan API request failed: {response.status_code} {response.text}")
    data = response.json()
    # Example: data['lulc_stats'] is a list of dicts with LULC class info
    lulc_stats = data.get('lulc_stats', [])
    df = pd.DataFrame(lulc_stats)
    return df

if __name__ == "__main__":
    fire_csv = os.path.join("data", "fire_nrt_J1V-C2_631066.csv")
    fire_df = load_fire_data(fire_csv)
    print(fire_df.head())
    # Example usage for weather API:
    # api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    # weather_df = fetch_weather_for_fire_df(api_key, fire_df, sample_size=5)
    # print(weather_df.head())
    # Example usage for Bhuvan API:
    # api_key = "YOUR_BHUVAN_API_KEY"
    # district_code = "YOUR_DISTRICT_CODE"
    # year = "2018"
    # lulc_df = fetch_vegetation_data_bhuvan(api_key, district_code, year)
    # print(lulc_df.head()) 