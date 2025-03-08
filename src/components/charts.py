from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

loading_color = "#008080"
loading_type = "dot"

map_chart = dbc.Card([
    dbc.CardHeader(html.H6(id='map_title', style={'fontWeight': 'bold', "margin": "2px", "padding": "0px"})),
    dbc.CardBody(
         dcc.Loading(  # Add loading spinner
            id="loading-map",
            type=loading_type,
            color=loading_color,
            children=[
                dcc.Graph(id='map_chart', style = {"height": "100%", "width": "100%", "padding": "0px", "overflow": "hidden"}) 
            ]
        ),
        style={"height": "350px", "padding": "0px", "overflow": "hidden"}
    ) 
], style={"width": "100%", "height": "450px", "padding": "0px", "overflow": "hidden"})

timeseries_chart = dbc.Card([
    dbc.CardHeader(html.H6(id='timeseries_title', style={'fontWeight': 'bold', "margin": "2px"})),
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
    dbc.CardHeader(html.H6(id='bar_title', style={'fontWeight': 'bold', "margin": "2px"})),
    dbc.CardBody([
        dcc.Loading(
            id="loading-bar",
            type=loading_type,
            color=loading_color,
            children=[dvc.Vega(id='bar_chart', spec={})]
        )
    ])
])