from dash import Dash, dcc
import dash_bootstrap_components as dbc
from flask_caching import Cache
import geopandas as gpd
import pandas as pd
import sys
import os
from datetime import datetime

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)

from src.components.sidebar import create_sidebar
from src.components.summary import summary
from src.components.charts import map_chart, timeseries_chart, bar_chart
from src.callbacks.yearselection import year_selection_callback
from src.callbacks.summary import summary_callback
from src.callbacks.charts import charts_callback
from src.callbacks.buttons import toggle_collapse
import src.callbacks.countryselection

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

cache = Cache(app.server, config={
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 300  # Cache timeout in seconds
})

# Load data
data = gpd.read_parquet("data/processed/data.geoparquet")
print("Data Loading Success!")

locations = data['name'].unique()
times = sorted(data['TIME'].unique()) # integer type
min_year = data['TIME'].min()
max_year = data['TIME'].max()

# Create the sidebar
sidebar = create_sidebar(locations, times, min_year, max_year)

# Callbacks
year_selection_callback(times) 
summary_callback(data, cache)
charts_callback(data, cache)

# App layout
app.layout = dbc.Container(
    [
        dbc.Row([
            sidebar,
            dbc.Col([
                summary,
                dbc.Row(dbc.Col(map_chart, md=12)),
                dbc.Row([
                    dbc.Col(timeseries_chart, md=6),
                    dbc.Col(bar_chart, md=6)
                ], style = {'paddingTop': '1.25rem'})
            ], 
            style = {'paddingLeft': '1.25rem', 'paddingRight': '2.5rem', 'paddingTop': '0.625rem', 'width': '80vw'})
        ])
    ],
    fluid=True,
    style={'padding': 0}
)

if __name__ == '__main__':
    app.run()

