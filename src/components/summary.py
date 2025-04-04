from dash import html, dcc
import dash_bootstrap_components as dbc

card_style = {
    "height": "70px",
    "backgroundColor": "#e6e6e6",  # Light gray background 
    "borderRadius": "10px",  # Rounded corners
    "padding": "0px",
    "alignItems": "center",  # Align everything vertically
    "justifyContent": "center",  # Center content inside
    "textAlign": "center"
}

summary = dcc.Loading(
    children=dbc.Row(
        [
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("Avg % GDP", style={"textAlign": "center"}),
                    html.H3(id="gdp-value", style={"fontWeight": "bold", "textAlign": "center"}),  
                    html.P(id="gdp-growth", style={"color": "green", "fontSize": "14px"})  
                ], style={"padding": "5px"})
            ], id='card-gdp', style=card_style), md=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("Avg % of Health Spending", style={"textAlign": "center"}),
                    html.H3(id="health-value", style={"fontWeight": "bold", "textAlign": "center"}),
                    html.P(id="health-growth", style={"color": "green", "fontSize": "14px"})
                ], style={"padding": "5px"})
            ], id= 'card-health', style=card_style), md=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("Avg Spend per Capita (USD)", style={"textAlign": "center"}),
                    html.H3(id="capita-value", style={"fontWeight": "bold", "textAlign": "center"}),
                    html.P(id="capita-growth", style={"color": "green", "fontSize": "14px"})
                ], style={"padding": "5px"})
            ], id='card-capita', style=card_style), md=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H6("Avg Total Spend (USD B)", style={"textAlign": "center"}),
                    html.H3(id="total-value", style={"fontWeight": "bold", "textAlign": "center"}),
                    html.P(id="total-growth", style={"color": "green", "fontSize": "14px"})
                ], style={"padding": "5px"})
            ], id='card-total', style=card_style), md=3),
        ],
        style={'paddingBottom': '1rem', "paddingTop": "0.5rem"}
    ),
    type="dot", 
    color="#008080"
)