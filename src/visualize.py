import folium
import pandas as pd

def plot_fire_map(df, map_file="fire_map.html"):
    """Plot fire locations on a map and save as HTML."""
    # Center map on mean location
    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=6)
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=3,
            color='red',
            fill=True,
            fill_opacity=0.7
        ).add_to(m)
    m.save(map_file)
    print(f"Map saved to {map_file}")

# Placeholder for advanced visualizations (heatmaps, animation, etc.)
def plot_advanced_visualizations(df):
    """Create advanced visualizations (to be implemented)."""
    # TODO: Implement advanced visualizations
    pass

if __name__ == "__main__":
    from preprocess import preprocess_fire_data
    from data_ingest import load_fire_data
    fire_csv = "../data/fire_nrt_J1V-C2_631066.csv"
    fire_df = load_fire_data(fire_csv)
    fire_df = preprocess_fire_data(fire_df)
    plot_fire_map(fire_df) 