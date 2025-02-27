import pandas as pd
import geopandas as gpd

def preprocess(file_path):
    data = pd.read_csv(file_path)
    data = data.drop('FLAG_CODES', axis=1)
    
    # load geospatial data
    url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
    world_countries = gpd.read_file(url)
    world_countries = world_countries[
        ["NAME", "SOV_A3", "CONTINENT", 'geometry']
    ].rename(
        columns=lambda x: x.lower()  # Lowercase column names
    ).query(
        'continent != "Antarctica"'
    )
    
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
    
    # merge the geolocation data to the original dataset
    processed_data = pd.merge(world_countries, data, how='left', on='LOCATION')
    # get the locations from the original dataset
    locations = data['LOCATION'].unique()

    print("Data Preprocessing Success!")

    return processed_data, locations