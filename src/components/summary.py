import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

card_style = {
    "height": "140px",
    "backgroundColor": "#e6e6e6",  # Light gray background 
    "borderRadius": "10px",  # Rounded corners
    "padding": "5px"
}

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