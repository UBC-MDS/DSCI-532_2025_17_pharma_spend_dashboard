from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

loading_color = "#008080"
loading_type = "dot"

map_chart = dbc.Card([
    dbc.CardHeader(html.H5('Map Chart', style={'fontWeight': 'bold'})),
    dbc.CardBody(
         dcc.Loading(  # Add loading spinner
            id="loading-map",
            type=loading_type,
            color=loading_color,
            children=[
                dcc.Graph(id='map_chart')
            ]
        ),
        style={"height": "100%", "width":"100%"}
    ) 
], style={"width": "100%", "height": "100%"})

timeseries_chart = dbc.Card([
    dbc.CardHeader(html.H5('Time Series Chart', style={'fontWeight': 'bold'})),
    dbc.CardBody([
        dcc.Loading(
            id="loading-timeseries",
            type=loading_type,
            color=loading_color,
            children=[dvc.Vega(id='timeseries_chart', spec={})]
        )
    ])    
])
    
bar_chart = dbc.Card([
    dbc.CardHeader(html.H5('Bar Chart', style={'fontWeight': 'bold'})),
    dbc.CardBody([
        dcc.Loading(
            id="loading-bar",
            type=loading_type,
            color=loading_color,
            children=[dvc.Vega(id='bar_chart', spec={})]
        )
    ])
])