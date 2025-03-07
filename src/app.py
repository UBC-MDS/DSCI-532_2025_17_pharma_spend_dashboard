from dash import Dash, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import sys
import os
from datetime import datetime

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)

from src.data.preprocessing import preprocess
from src.components.sidebar import create_sidebar
from src.components.summary import summary
from src.components.charts import map_chart, timeseries_chart, bar_chart
from src.callbacks.yearselection import year_selection_callback
from src.callbacks.summary import summary_callback
from src.callbacks.charts import charts_callback
import src.callbacks.countryselection

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Data preprocessing
raw_data, world_countries = preprocess("data/raw/data.csv")
print("Data Loading Success!")
# get the locations and years from the original dataset
data = pd.merge(raw_data, world_countries, on='LOCATION', how='left')
locations = data['name'].unique()
times = sorted(data['TIME'].unique()) # integer type
min_year = data['TIME'].min()
max_year = data['TIME'].max()

# Create the sidebar
sidebar = create_sidebar(locations, times, min_year, max_year)

# Callbacks
year_selection_callback(times) 
# merge data
merge_data = pd.merge(
    world_countries,
    raw_data,
    on='LOCATION',
    how='inner'
)
summary_callback(merge_data)
charts_callback(merge_data, world_countries)

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
            ], style = {'paddingLeft': '1.25rem', 'paddingRight': '2.5rem', 'paddingTop': '0.625rem'})
        ])
    ],
    fluid=True,
    style={'padding': 0}
)

if __name__ == '__main__':
    app.run()

