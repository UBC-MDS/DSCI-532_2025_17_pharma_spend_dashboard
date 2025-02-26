from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Side bar for global filter
sidebar = dbc.Col([
    html.H3('Global Pharmaceutical Spend Dashboard'),
    html.Br(),

    html.H5('Country'),
    dcc.Dropdown(),
    html.Br(),

    html.H5('Year'),
    html.P('From', style={'margin-bottom': '0.375rem'}),
    dcc.Dropdown(),
    html.P('To', style={'margin-top': '0.375rem'}),
    dcc.Dropdown(),
    ],
    md=3,
    style={
        'background-color': '#e6e6e6',
        'padding': 15,  # Padding top,left,right,botoom
        'padding-left': 30,
        'width': '20vw',
        'height': '100vh',  # vh = "viewport height" = 100% of the window height
        'flex-direction': 'column',  # Allow for children to be aligned to bottom
    }
) 

card_style = {'height': '100px'}

# Summary status
summary = dbc.Row(
    [
        html.H5('Summary Stats'),
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Avg % GDP"),
                ])
            ], style=card_style), width=3),  # Takes 4/12 columns

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Avg % of Health Spending"),
                ])
            ], style=card_style), width=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Avg Spend per Capita (in USD)"),
                ])
            ], style=card_style), width=3),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Total Spend (in USD m)"),
                ])
            ], style=card_style), width=3),
        ])
    ],
    style={
        'padding': 15,
    }
)

# App layout
app.layout = dbc.Container(
    [
        dbc.Row([
            sidebar,
            dbc.Col(summary)
        ]),
    ],
    fluid=True, # Expand to the full width of the window
    style={
        'padding': 0
    }  
)


if __name__ == '__main__':
    app.run()