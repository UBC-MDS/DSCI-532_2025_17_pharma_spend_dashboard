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

card_style = {
    "height": "125px",
    "backgroundColor": "#e6e6e6",  # Light gray background 
    "borderRadius": "10px",  # Rounded corners
    "padding": "5px",
    "paddingTop": "0.75rem"
}

# Create the sidebar
sidebar = create_sidebar(locations, times, min_year, max_year)

# Summary status (Celine)
summary = dcc.Loading(
    children=dbc.Row(
        [
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("Avg % GDP", style={"textAlign": "center"}),
                    html.H2(id="gdp-value", style={"fontWeight": "bold", "textAlign": "center"}),  
                    html.P(id="gdp-growth", style={"color": "green", "fontSize": "14px"})  
                ])
            ], style=card_style), md=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("Avg % of Health Spending", style={"textAlign": "center"}),
                    html.H2(id="health-value", style={"fontWeight": "bold", "textAlign": "center"}),
                    html.P(id="health-growth", style={"color": "green", "fontSize": "14px"})
                ])
            ], style=card_style), md=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("Avg Spend per Capita (USD)", style={"textAlign": "center"}),
                    html.H2(id="capita-value", style={"fontWeight": "bold", "textAlign": "center"}),
                    html.P(id="capita-growth", style={"color": "green", "fontSize": "14px"})
                ])
            ], style=card_style), md=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("Avg Total Spend (USD B)", style={"textAlign": "center"}),
                    html.H2(id="total-value", style={"fontWeight": "bold", "textAlign": "center"}),
                    html.P(id="total-growth", style={"color": "green", "fontSize": "14px"})
                ])
            ], style=card_style), md=3),
        ],
        style={'paddingBottom': '1rem', "paddingTop": "0.625rem"}
    ),
    type="cube", fullscreen=False, color="white"
)

# Metric Selector
# metric_selection = dbc.Col(
#     [
#         dbc.Col(html.H5('Spend Metrics'), width=2),
#         dbc.Col(
#             dcc.RadioItems(
#                 id='spend_metric',
#                 options=[
#                     {'label': '% of GDP', 'value': 'PC_GDP'},
#                     {'label': '% of Healthcare', 'value': 'PC_HEALTHXP'},
#                     {'label': 'Spend Per Capita (USD)', 'value': 'USD_CAP'},
#                     {'label': 'Total Spend (USD B)', 'value': 'TOTAL_SPEND'},
#                 ],
#                 value='PC_GDP',  # Default selection
#                 labelStyle={'display': 'inline-block', 'marginRight': '0.938rem'}
#             ),
#         )
#     ],
#     style = {'paddingBottom': '1rem'}
# )

# Charts
map_chart = dbc.Card([
    dbc.CardHeader(html.H5('Map Chart', style={'fontWeight': 'bold'})),
    dbc.CardBody(
        dvc.Vega(id='map_chart', spec={}),
        className="d-flex justify-content-center w-100",
        style={"height": "100%"}
    ) 
], style={"width": "100%", "height": "100%"})

timeseries_chart = dbc.Card([
    dbc.CardHeader(html.H5('Time Series Chart', style={'fontWeight': 'bold'})),
    dbc.CardBody([
        dvc.Vega(id='timeseries_chart', spec={})
    ])    
])
    
bar_chart = dbc.Card([
    dbc.CardHeader(html.H5('Bar Chart', style={'fontWeight': 'bold'})),
    dbc.CardBody([
        dvc.Vega(id='bar_chart', spec={})
    ])
])

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

