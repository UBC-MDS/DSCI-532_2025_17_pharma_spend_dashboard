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

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Data preprocessing
data, world_countries = preprocess("data/raw/data.csv")
print("Data Loading Success!")
# get the locations and years from the original dataset
locations = data['LOCATION'].unique()
times = sorted(data['TIME'].unique()) # integer type
min_year = data['TIME'].min()
max_year = data['TIME'].max()

# Side bar for global filter
sidebar = dbc.Col(
    [
        html.H3('Global Pharmaceutical Spend Dashboard', style={'fontWeight': 'bold'}),
        html.Br(),

        html.H5('Country', style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='country_select', 
            options=[{'label': country, 'value': country} for country in locations], 
            value=['CAN', 'USA', 'MEX'], 
            multi=True
        ),
        html.Br(),
        html.Br(),

        html.H5('Year', style={'fontWeight': 'bold'}),
        html.P('From', style={'marginBottom': '0.375rem'}),
        dcc.Dropdown(
            id='start_year_select',
            options=[{'label': str(year), 'value': year} for year in times],
            value=min_year,  # Default start by the minimal year
            clearable=False
        ),
        html.P('To', style={'marginTop': '0.375rem'}),
        dcc.Dropdown(
            id='end_year_select',
            options=[{'label': str(year), 'value': year} for year in times],
            value=max_year,  # Default end by the maximum year
            clearable=False
        ),
        html.Br(),
        html.Br(),
        html.Br(),

        html.H5('About:', style={'fontWeight': 'bold'}),
        html.P("This Dash app was developed by Team 17 of the MDS program to provide insights into global pharmaceutical spending.", style={'fontSize': '12px'}),
        html.P('By: Jason Lee, Daria Khon, Celine Habashy, Catherine Meng', style={'fontSize': '12px'}),
        html.P("Data: Organisation for Economic Cooperation and Development", style={'fontSize': '12px'}),
        html.P(["Source code: ", html.A("GitHub", href="https://github.com/UBC-MDS/DSCI-532_2025_17_pharma_spend_dashboard", target="_blank", style={'color': 'blue', 'fontSize': '12px'})], style={'fontSize': '12px'}),
        html.P("Last updated: {}".format(datetime.now().strftime('%B %d, %Y')), style={'fontSize': '12px'})
    ],
    md=3,
    style={
        'backgroundColor': '#e6e6e6',
        'padding': 15,  # Padding top,left,right,botoom
        'paddingLeft': 30,
        'width': '20vw',
        'minHeight': '100vh',  # vh = 'viewport height' = 100% of the window height
        'flexDirection': 'column',  # Allow for children to be aligned to bottom
    }
)

card_style = {'height': '125px'}

# Summary status (Celine)
summary = dcc.Loading(
    children=dbc.Row(
        [
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H6("Avg % GDP"),
                        html.H2(id="gdp-value", style={"fontWeight": "bold"}),  
                        html.P(id="gdp-growth", style={"color": "green", "fontSize": "14px"})  
                    ])
                ], style=card_style), width=3),

                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H6("Avg % of Health Spending"),
                        html.H2(id="health-value", style={"fontWeight": "bold"}),
                        html.P(id="health-growth", style={"color": "green", "fontSize": "14px"})
                    ])
                ], style=card_style), width=3),

                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H6("Avg Spend per Capita (USD)"),
                        html.H2(id="capita-value", style={"fontWeight": "bold"}),
                        html.P(id="capita-growth", style={"color": "green", "fontSize": "14px"})
                    ])
                ], style=card_style), width=3),

                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H6("Avg Total Spend (USD B)"),
                        html.H2(id="total-value", style={"fontWeight": "bold"}),
                        html.P(id="total-growth", style={"color": "green", "fontSize": "14px"})
                    ])
                ], style=card_style), width=3),
            ])
        ],
        style={'paddingBottom': '1rem'}
    ),
    type="cube", fullscreen=False, color="white"
)

# Metric Selector
metric_selection = dbc.Row(
    [
        dbc.Col(html.H5('Spend Metrics'), width=2),
        dbc.Col(
            dcc.RadioItems(
                id='spend_metric',
                options=[
                    {'label': '% of GDP', 'value': 'PC_GDP'},
                    {'label': '% of Healthcare', 'value': 'PC_HEALTHXP'},
                    {'label': 'Spend Per Capita (USD)', 'value': 'USD_CAP'},
                    {'label': 'Total Spend (USD B)', 'value': 'TOTAL_SPEND'},
                ],
                value='TOTAL_SPEND',  # Default selection
                labelStyle={'display': 'inline-block', 'marginRight': '0.938rem'}
            ),
        )
    ],
    style = {'paddingBottom': '1rem'}
)

# Charts
map_chart = dvc.Vega(id='map_chart', spec={})
timeseries_chart = dvc.Vega(id='timeseries_chart', spec={})
bar_chart = dvc.Vega(id='bar_chart', spec={})

# App layout
app.layout = dbc.Container(
    [
        dbc.Row([
            sidebar,
            dbc.Col([
                summary,
                metric_selection,
                dbc.Row(dbc.Col(map_chart)),
                dbc.Row([
                    dbc.Col(timeseries_chart, width=6),
                    dbc.Col(bar_chart, width=6)
                ], style = {'paddingTop': '1.25rem'})
            ], style = {'paddingLeft': '1.25rem', 'paddingTop': '0.625rem'})
        ])
    ],
    fluid=True,
    style={'padding': 0}
)

if __name__ == '__main__':
    app.run()

