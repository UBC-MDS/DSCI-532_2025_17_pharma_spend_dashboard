import pandas as pd
import geopandas as gpd

def preprocess(file_path):
    """ Loads and preprocesses the data set together with geopspatial world data"""
    data = pd.read_parquet(file_path)
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
    
    print("Data Preprocessing Success!")

    return data, world_countries