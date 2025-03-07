from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

loading_color = "#008080"

map_chart = dbc.Card([
    dbc.CardHeader(html.H5('Map Chart', style={'fontWeight': 'bold'})),
    dbc.CardBody(
         dcc.Loading(  # Add loading spinner
            id="loading-map",
            type="circle",
            color=loading_color,
            children=[
                dvc.Vega(id='map_chart', spec={})
            ]
        ),
        className="d-flex justify-content-center w-100",
        style={"height": "100%"}
    ) 
], style={"width": "100%", "height": "100%"})

timeseries_chart = dbc.Card([
    dbc.CardHeader(html.H5('Time Series Chart', style={'fontWeight': 'bold'})),
    dbc.CardBody([
        dcc.Loading(
            id="loading-timeseries",
            type="circle",
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
            type="circle",
            color=loading_color,
            children=[dvc.Vega(id='bar_chart', spec={})]
        )
    ])
])