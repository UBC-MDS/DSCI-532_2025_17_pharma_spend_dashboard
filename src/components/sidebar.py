from datetime import datetime
from dash import html, dcc
import dash_bootstrap_components as dbc


# Side bar for global filter
def create_sidebar(locations, times, min_year, max_year):

    collapse_button = dbc.Button(
                "About", 
                id="collapse-button",
                outline=True,
                style={
                    'width': '100px',
                    'background-color': '#008080',
                    'color': 'white',
                    'margin-top': 10
        }
    )

    collapse_section = dbc.Collapse(
    dbc.Card(
        dbc.CardBody([
            html.P(
                "This Dash app was developed by Team 17 of the MDS program to provide insights into global pharmaceutical spending.", 
                style={'fontSize': '14px', 'lineHeight': '1.5'}
            ),
            html.P([html.Strong("By: "), "Jason Lee, Daria Khon, Celine Habashy, Catherine Meng"], 
                   style={'fontSize': '14px', 'lineHeight': '1.5'}),
            html.P([html.Strong("Data: "), "Organisation for Economic Cooperation and Development"], 
                   style={'fontSize': '14px', 'lineHeight': '1.5'}),
            html.P([html.Strong("Source code: "),  html.A("GitHub", href="https://github.com/UBC-MDS/DSCI-532_2025_17_pharma_spend_dashboard", 
                   target="_blank", style={'color': 'blue', 'fontSize': '14px'})], style={'fontSize': '14px', 'lineHeight': '1.5'}),
            html.P([html.Strong("Last updated: "),  datetime.now().strftime('%B %d, %Y')
                ], style={'fontSize': '14px', 'lineHeight': '1.5'}),
        ]),
        style={
            'backgroundColor': '#ffffff',  # White background
            'padding': '5px',
            'border': '1px solid #ddd',  # Light grey border
            'borderRadius': '10px',  # Rounded corners
        }
    ),
    id="collapse",
    is_open=False
)

    sidebar = dbc.Col(
        [
            html.H1('Global Pharmaceutical Spend Dashboard', style={'fontWeight': 'bold'}),
            html.Br(),
            html.Hr(),

            html.H5('Country', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='country_select', 
                options=[{'label': country, 'value': country} for country in locations], 
                value=['Canada', 'United States of America', 'Mexico'], 
                multi=True
            ),
            html.Div(id="warning", style={"color": "red", "marginTop": "10px"}),  # Warning message
            html.Br(),
            html.Hr(),

            html.H5('Year', style={'fontWeight': 'bold'}),
            html.P('From', style={'marginBottom': '0.375rem'}),
            dcc.Dropdown(
                id='start_year_select',
                options=[{'label': str(year), 'value': year} for year in times],
                value=2000,  # Default start in 2000
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
            html.Hr(),
            
            html.H5('Spend Metrics', style={'fontWeight': 'bold'}),
            dcc.RadioItems(
                    id='spend_metric',
                    options=[
                        {'label': '% of GDP', 'value': 'PC_GDP'},
                        {'label': '% of Healthcare', 'value': 'PC_HEALTHXP'},
                        {'label': 'Spend Per Capita (USD)', 'value': 'USD_CAP'},
                        {'label': 'Total Spend (USD B)', 'value': 'TOTAL_SPEND'},
                    ],
                    value='PC_GDP',  # Default selection
                    labelStyle={'display': 'block', 'marginRight': '0.938rem'}
            ),
            
            html.Br(),
            html.Hr(),

            collapse_button,
            html.Br(),
            html.Br(),
            collapse_section

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

    return sidebar