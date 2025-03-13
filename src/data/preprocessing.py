# Script for preprocessing data and merging it with geodata
import pandas as pd
import geopandas as gpd
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# load and preprocess pharmaceutical spending data
file_path = "data/raw/data.csv"
data = pd.read_csv(file_path)
data = data.drop('FLAG_CODES', axis=1)

# load world geodata
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
world_countries = gpd.read_file(url)
world_countries = world_countries[
    ["NAME", "SOV_A3", "CONTINENT", "geometry"]
].rename(
    columns=lambda x: x.lower()  
).query(
    'continent != "Antarctica"'
).drop(
    'continent', axis=1
)

# replacement disctionary, to match country codes between 2 data sets
replacement = {
    'US1': 'USA', 
    'NZ1': 'NZL', 
    'FR1': 'FRA', 
    'DN1': 'DNK', 
    'IS1': 'ISR', 
    'GB1': 'GBR', 
    'NL1': 'NLD',
    'FI1': 'FIN', 
    'AU1': 'AUS'
}

world_countries = world_countries.replace(replacement)
world_countries = world_countries.rename(columns={'sov_a3': 'LOCATION'})

merged_data = pd.merge(world_countries, data, on='LOCATION', how='inner')

# Saving processed data
merged_data.to_file("data/processed/data.geojson", driver = 'GeoJSON')
merged_data.to_parquet("data/processed/data.geoparquet", engine="pyarrow")

print(f'Processed data file saved to data/processed/ as GeoJSON and Geoparquet')