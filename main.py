from src.data_ingest import load_fire_data, fetch_vegetation_data_bhuvan, fetch_weather_for_fire_df
from src.preprocess import preprocess_fire_data, merge_with_weather_vegetation
from src.model import train_baseline_model
from src.visualize import plot_fire_map

if __name__ == "__main__":
    # Step 1: Load fire data
    fire_csv = "data/fire_nrt_J1V-C2_631066.csv"
    fire_df = load_fire_data(fire_csv)

    # Step 2: Preprocess fire data
    fire_df = preprocess_fire_data(fire_df)

    # Step 3: Fetch and merge weather and Bhuvan LULC data
    weather_api_key = "df137321da56d9f536d1b1479df49802"
    bhuvan_api_key = "c0863f725649542f9082c6c708f519da36c01907"
    district_code = "YOUR_DISTRICT_CODE"  # <-- Replace with your district code
    year = "2018"  # <-- Replace with desired year

    # Fetch weather data for a sample of fire events (to avoid API rate limits)
    weather_df = fetch_weather_for_fire_df(weather_api_key, fire_df, sample_size=10)
    # Fetch Bhuvan LULC data
    # Uncomment and set your district_code to enable Bhuvan API integration
    # lulc_df = fetch_vegetation_data_bhuvan(bhuvan_api_key, district_code, year)
    lulc_df = None  # Set to None if not using Bhuvan API

    # Merge all data
    merged_df = merge_with_weather_vegetation(fire_df, weather_df=weather_df, vegetation_df=lulc_df, district_code=district_code)

    # Step 4: Train baseline model
    clf = train_baseline_model(merged_df)

    # Step 5: Visualize fire locations
    plot_fire_map(merged_df)

    # Placeholders for weather and vegetation integration
    # TODO: Integrate weather and vegetation data when APIs are available 