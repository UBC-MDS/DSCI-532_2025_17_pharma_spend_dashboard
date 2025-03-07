from dash import html
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

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