from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
import geopandas as gpd
import altair as alt
import sys
import os
from datetime import datetime

# Get the absolute path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to sys.path
sys.path.append(parent_dir)

from src.preprocessing import preprocess
import src.callbacks
from src.components.sidebar import create_sidebar
from src.components.summary import summary
from src.components.charts import map_chart, timeseries_chart, bar_chart

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Data preprocessing
data, world_countries = preprocess("data/raw/data.csv")
print("Data Loading Success!")
# get the locations and years from the original dataset
data = pd.merge(data, world_countries, on='LOCATION', how='left')
locations = data['name'].unique()
times = sorted(data['TIME'].unique()) # integer type
min_year = data['TIME'].min()
max_year = data['TIME'].max()

# Create the sidebar
sidebar = create_sidebar(locations, times, min_year, max_year)

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

